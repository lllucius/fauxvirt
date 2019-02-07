
from datetime import datetime
import uuid

def get_guid(url):
    return str(uuid.uuid3(uuid.NAMESPACE_URL, url))

def make_guid(base, suffix):
    return get_guid(base.strip("/") + "/" + suffix.strip("/"))

def get_date():
    return datetime.utcnow().isoformat() + "+00:00"

