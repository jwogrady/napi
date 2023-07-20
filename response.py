import requests

from conveniences import make_url, ns_key, ns_typ, ns_vs


def request(operation, payload):
    url = make_url(operation=operation,)
    resp = requests.get(url=url, params=payload)
    return resp

request.__doc__="""Generic request builder
Convenience method that passes `operation` and `payload` to make_url 
"""


def getContact():
    operation = 'contactList'
    vs = ns_vs
    typ = ns_typ
    key = ns_key
    payload = {'version': vs, 'type': typ, 'key': key}
    resp = request(operation, payload)

    return resp


getContact.__doc__ = """View contact profiles

Get a list of all contact profiles within your account.

Note: the maximum number of contacts that can be returned per request is limited to 1000, 
please use offset parameter to navigate through your contacts dataset.

Additional parameters:

contact_id: You can optionally pass the ID number for a specific contact record to look up. All contacts associated with your account will be returned if you do not provide this parameter.

offset: You can optionally pass the offset to navigate through your contacts dataset.

sample request: https://www.namesilo.com/api/contactList?version=1&type=xml&key=12345

Full reference: https://www.namesilo.com/api-reference#contact/contact-list
"""


def deleteContact(contact_id):
    operation = 'contactDelete'
    vs = ns_vs
    typ = ns_typ
    key = ns_key
    cid = contact_id
    payload = {'version': vs, 'type': typ, "contact_id": cid, 'key': key}
    resp = request(operation, payload)

    return resp


deleteContact.__doc__ = """Delete a contact profile

Delete a contact profile Delete a contact profile in your account.
Please remember that the only contact profiles that can be deleted are those that are not the account 
default and are not associated with any active domains or order profiles.

parameter:

contact_id: The internal NameSilo ID for the contact profile record to update

sample request: https://www.namesilo.com/api/contactDelete?version=1&type=xml&key=12345&contact_id=111111

contact_id: The internal NameSilo ID for the contact profile record to update
"""
