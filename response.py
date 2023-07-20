import requests

from conveniences import make_url, ns_key, ns_typ, ns_vs


def request(operation, payload):
    url = make_url(operation=operation,)
    resp = requests.get(url=url, params=payload)
    return resp


def getContact():
    operation = 'contactList'
    vs = ns_vs
    typ = ns_typ
    key = ns_key
    payload = {'version': vs, 'type': typ, 'key': key}
    resp = request(operation, payload)

    return resp


def deleteContact(contact_id):
    operation = 'contactDelete'
    vs = ns_vs
    typ = ns_typ
    key = ns_key
    cid = contact_id
    payload = {'version': vs, 'type': typ, "contact_id": cid, 'key': key}
    resp = request(operation, payload)

    return resp
