import os
import calendar
import time
import xml.dom.minidom
import xml.etree.ElementTree as ET
from dotenv import dotenv_values


env = dotenv_values('.env')

# Model variables
ns_url = env['NS_URL']
ns_vs = env['NS_VS']
ns_typ = env['NS_TYP']
ns_key = env['NS_KEY']


def make_url(operation):
    url = ns_url
    url_parts = [url, operation]
    url = ''.join(url_parts)
    return url

make_url.__doc__="""Make the base url

Joins the base url parts.

type:
string

exp.) 'https://www.namesilo.com/api/contactAdd'
"""

def make_timestamp():
    current_GMT = time.gmtime()
    timestamp = calendar.timegm(current_GMT)
    return str(timestamp)

make_timestamp.__doc__="""Makes a timestamp string

type:
string 

exp.) '1689815434'
"""


def check_file(folderpath, filepath):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        open(filepath, "w")
        print('Created new file')
    else:
        print('File already exists')

check_file.__doc__="""Creates folder amd file if one doesn't already exist"""


def count_occurrences(filepath, divider):
    if not os.path.exists(filepath):
        check_file(filepath)
    print('Directory Exists')
    target = open(filepath, 'r')
    data = target.read()
    occurrence = data.count(divider)
    return str(occurrence)

count_occurrences.__doc__="""Counts the number of occourances of 'divider' str variable in a output file

type: str
exp.) '9'
"""

def prettyprintxml(dom, pxml, root):
    if not os.path.exists('output'):
        os.makedirs('output')
    print(dom, file=open('output/dom.xml', 'w'))
    print(pxml, file=open('output/pxml.xml', 'w'))
    print(root, file=open('output/root.xml', 'w'))
