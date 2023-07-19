import os
import io
import calendar
import time


import logging
import xml.dom.minidom
import xml.etree.ElementTree as ET

from dotenv import dotenv_values

env = dotenv_values('.env')


# Model variable
ns_url = env['NS_URL']
ns_vs = env['NS_VS']
ns_typ = env['NS_TYP']
ns_key = env['NS_KEY']

def make_url(operation):
    url = ns_url
    url_parts = [url, operation]
    url = ''.join(url_parts)
    return url

def get_timestamp():
    current_GMT = time.gmtime()
    timestamp = calendar.timegm(current_GMT)
    return str(timestamp)

def check_file(folderpath, filepath):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        open(filepath, "w")
        print('Created new file')
    else:
        print('File already exists')


def count_occurances(filepath, divider):
    if not os.path.exists(filepath):
        check_file(filepath)
    print('Directory Exists')
    target = open(filepath, 'r')
    data = target.read()
    occurance = data.count(divider)
    return str(occurance)


def prettyprintxml(dom, pxml, root):
    pxml = xml.dom.minidom.parseString(dom).toprettyxml()
    if not os.path.exists('output'):
        os.makedirs('output')
    print(dom, file=open('output/dom.xml', 'w'))
    print(pxml, file=open('output/pxml.xml', 'w'))
    print(root, file=open('output/root.xml', 'w'))
