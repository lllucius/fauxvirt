#!/usr/bin/python3

import re

from flask import Flask, request, make_response, session
from flask_httpauth import HTTPBasicAuth
from importlib import import_module
from lxml import etree
from io import StringIO
from pprint import pprint

from sdk import services as services
from sdk.types import get_root_tag

from utils import *

USER_DATA = {"admin": "pass"}

auth = HTTPBasicAuth()

app = Flask(__name__)
app.secret_key = "super secret"
app.session_cookie_name = "JSESSIONID"
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True

xml_parser = etree.ETCompatXMLParser()

provider = import_module("providers.sim")
services.init(provider)
prov = provider.Provider()

@app.before_request
def log_request():
    print("==============================================================")
    print("Request:")
    print("  Method", request.method)
    print("  Base URL", request.base_url)
    print("  Full Path", request.full_path)
    print("  Path", request.path)
    print("  url", request.url)
    print("  blueprint", request.blueprint)
    print("  endpoint", request.endpoint)
    print("  url_rule", request.url_rule)
    print("  Headers:\n", request.headers)
    print("  Cookies:\n", request.cookies)
    print("  Args:\n", request.args)
    print("  Data:\n", request.data)
    print("  Form:\n", request.form)
    print("  Environ:")
    pprint(request.environ)
    return None

@auth.verify_password
def verify_password(username, password):
    print("ASDFASDFASDF")
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

method_map = {
    True: {
        "DELETE": "delete",
        "GET": "get",
        "POST": "add"
    },
    False: {
        "DELETE": "delete",
        "GET": "get",
        "PUT": "update"
    }
}

@app.route("/api", methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/api/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
#@auth.login_required
def dispatch(path = ""):
    print("path", path)

    service, obj, guid, action = services.follow(path)

    print(request.method)

    if action is None:
        if request.method not in method_map[service.is_collection]:
            raise BadRequest()
        action = method_map[service.is_collection][request.method]
    elif request.method != "POST":
        raise BadRequest()

    func = service.functions[action]

    if len(request.data) > 0:
        if func["req"] is None:
            raise BadRequest()

        try:
            rootnode = etree.fromstring(request.data, parser=xml_parser)
        except Exception as e:
            print(e)
            raise BadRequest()

        _, rootclass = get_root_tag(rootnode)
        if rootclass is None or rootclass.__name__ != func["req"]:
            raise BadRequest()

        in_obj = rootclass.factory()
        in_obj.build(rootnode)
        s = StringIO()
        in_obj.export(s, 0)
        print(s.getvalue())
        rootnode = None
    else:
        if func["req"] is not None:
            raise BadRequest()
        in_obj = None

    print("PARMS", in_obj)

    if action == "add":
        out_obj = obj.add(in_obj)
    elif action == "delete":
        out_obj = obj.delete(guid, in_obj)
    elif action == "get":
        out_obj = obj
    elif action == "update":
        out_obj = obj.update(guid, in_obj)
    else:
        out_obj = obj.action(in_obj)

    if out_obj == None and func["ret"] is not None:
        raise InternalServerError()

    print("FINAL", out_obj)

    out = StringIO()
    out_obj.export(out, 0)

    xml = out.getvalue()
    xml = xml.replace("{{APIBASE}}", "/api")
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' + xml

#provider.initialize()
app.run(debug=True, host="0.0.0.0", port=80)

