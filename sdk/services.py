#!/usr/bin/python3

import os
import re
import untangle
import uuid

from datetime import datetime
from werkzeug.exceptions import NotFound, NotImplemented, BadRequest

from sdk import types as sdk

class Service(object):
    def __init__(self, *arg, **kwargs):
        self.href = None
        self.label = None
        self.service_type = None
        self.child_type = None
        self.child_label = None
        self.is_collection = False
        self.actions = []
        self.links = {}
        self.functions = {}

labels = {}
classes = {}
provider = None

def init(prov):
    global labels, classes, API, provider

    provider = prov

    path = os.path.dirname(os.path.realpath(__file__))
    d = untangle.parse(os.path.join(path, "rsdl.xml"))

    API = Service()
    API.href = "api"
    API.label = "api"
    API.service_type = "API"
    API.functions["get"] = {}
    API.functions["get"]["req"] = None
    API.functions["get"]["ret"] = "API"

    classes["API"] = API
    labels["api"] = API

    #
    # Build all of the classes and path cross reference
    #
    for link in d.rsdl.links.children:
        if link["rel"] != "get":
            continue

        href = link["href"]

        node = href.split("/")[-1]

        service = Service()
        service.href = href
        service.label = re.sub("{(.*?):.*?}", "\g<1>", node)
        service.service_type = get_rettype(link)
        service.is_collection = (node[0] != '{')

        classes[service.service_type] = service
        labels[href] = service

    #
    # Gather the actions, functions, and links
    #
    for link in d.rsdl.links.children:
        href = link["href"]
        rel = link["rel"]

        # Is it an action?
        if rel not in ["add", "delete", "get", "update"]:
            # Must use the parent
            href, _ = href.rsplit("/", 1)

            # Add it to the parent service
            if rel not in labels[href].actions:
                labels[href].actions.append(rel)

        service = labels[href]

        if rel not in service.functions:
            service.functions[rel] = {}
            service.functions[rel]["req"] = get_reqtype(link)
            service.functions[rel]["ret"] = get_rettype(link)

        if rel == "get":
            nodes = href.rsplit("/", 1)
            if len(nodes) > 1:
                parent = labels[nodes[0]]
            else:
                parent = API

            if service.is_collection:
                if service.label not in parent.links:
                    parent.links[service.label] = service
            else:
                parent.child_type = service.service_type
                parent.child_label = service.label

    for name in sorted(classes.keys()):
        value = classes[name]
        showservice(value)

def showservice(service):
    href = service.href
    is_col = service.is_collection
    label = service.label
    acts = sorted(service.actions)
    links = service.links
    funcs = service.functions
    service_type = service.service_type
    child_type = service.child_type
    child_label = service.child_label

    print("%s:" % service.label)
    print("    href = '%s'" % href)
    print("    label = '%s'" % label)
    print("    service_type = '%s'" % service_type)
    print("    child_type = '%s'" % child_type)
    print("    child_label = '%s'" % child_label)
    print("    is_collection =", is_col)
    if funcs:
        print("    functions = {")
        for func in sorted(funcs):
            print("        '%s': %s," % (func, funcs[func]))
        print("    }")
    else:
        print("    functions = {}")
    if acts:
        print("    actions = [")
        for act in sorted(acts):
            print("        '%s'," % act)
        print("    ]")
    else:
        print("    actions = []")
    if links:
        print("    links = {")
        for link in sorted(links):
            print("        '%s': '%s'," % (link, links[link].service_type))
        print("    }")
    else:
        print("    links = {}")
    print()

def get_reqtype(link):
    if getattr(link.request, "body", None) is not None:
        if getattr(link.request.body, "type", None) is not None:
            return link.request.body.type.cdata
    return None

def get_rettype(link):
    if getattr(link, "response", None) is not None:
        if getattr(link.response, "type", None) is not None:
            return link.response.type.cdata
    return None

def follow(path):
    print("PATH", path)
    parents = []
    obj = None
    service = API
    action = None
    guid = None

    nodes = path.split("/")
    print("NODES", nodes, len(nodes))
    for node in nodes:
        print("NODE", node, service.label, service.service_type)
        if node in service.actions:
            print("ACTION")
            if node != nodes[-1]:
                raise NotFound()
            action = node
            break

        if node in service.links:
            print("LINK")
            service = service.links[node]
            guid = None
        elif service.is_collection:
            print("COL")
            service = classes[service.child_type]
            guid = node
        elif len(nodes) == 1 and node == "":
            print("API")
            pass        
        else:
            print("ELSE")
            raise NotFound()

        cls = getattr(provider, service.service_type, None)
        if cls is None or not hasattr(cls, "get"):
            raise NotImplemented()

        obj = cls.get(obj, guid)
        if obj is None:
            raise NotFound()

    print("OBJ", obj)
    print("SERVICE", service.label, "GUID", guid, "ACTION", action)

    return service, obj, guid, action

def base_href(name, guid):
    return "{{APIBASE}}/" + classes[name].label + "/" + guid

def path_href(this):
    href = ""
    while this is not None:
        if hasattr(this, "get_id"):
            name = this.get_id()
        else:
            name = classes[this.__class__.__name__].label

        if name is not None:
            href = "/" + name + href
        this = this.get_parent()

    return "{{APIBASE}}" + href

def base_link(name, guid):
    label = classes[name].label
    href = "{{APIBASE}}/" + classes[name].label + "/" + guid

    return getattr(sdk, classes[name].child_type)(href=href, id=guid)

def add_links(obj):
    name = obj.__class__.__name__
    if len(classes[name].links) == 0:
        return None

    do_links(obj, obj, classes[name].links.keys())

def add_actions(obj):
    name = obj.__class__.__name__
    if len(classes[name].actions) == 0:
        return None

    actions = provider.Actions()
    obj.set_actions(actions)

    do_links(actions, obj, classes[name].actions)

def do_links(parent, obj, links):
    objid = None
    if hasattr(parent, "get_id"):
        objid = parent.get_id()

    if objid is not None:
        objid = "/" + objid
    else:
        objid = ""

    href = path_href(obj)

    for link in sorted(links):
        parent.add_link(provider.Link(href=href + "/" + link, rel=link))

def get_guid(url):
    return str(uuid.uuid3(uuid.NAMESPACE_URL, url))

def make_guid(base, suffix):
    return get_guid(base.strip("/") + "/" + suffix.strip("/"))

def get_date():
    return datetime.utcnow().isoformat() + "+00:00"

