import os
import xml.dom.minidom
import xml.etree.ElementTree as ET


from conveniences import prettyprintxml, get_timestamp, check_file, count_occurrences
from response import getContact


# request response content
dom = getContact().content

# one way to load
root = ET.fromstring(dom)

# another way
pxml = xml.dom.minidom.parseString(dom).toprettyxml()


def create_contact_ids_list():
    cids = []
    for x in root.iter('contact_id'):
        # print(x.text)
        cids.append(x.text)
    return cids


def output_content_ids(filepath, timestamp, occurrences, divider, cids):
    print(divider + timestamp + ' ] [ Run instance: ' +
          occurrences + ' ] ->', file=open(filepath, 'a'))
    for x in cids:
        print(x, file=open(filepath, 'a'))
    '''    
    # uncomment to output as list.

    print(divider + timestamp + ' ] [ Run instance: ' +
          occurrences + ' ] -> \n', str(cids), file=open(filepath, 'a'))
    '''


# helpers

# url building
folders = ['output', 'loops', 'contact_ids']
folderpath = os.path.join(*folders)
filename = '/loop_contact_ids.txt'

# make the folder and file
filepath = folderpath + filename
check_file(folderpath, filepath)

# format and output variables
divider = '<-/~/~/~/~/ [ current GMT timestamp: '
timestamp = get_timestamp()
occurrences = count_occurrences(filepath, divider)

# create list of contact ids
cids = create_contact_ids_list()

# call the methods
output_content_ids(filepath, timestamp, occurrences, divider, cids)

prettyprintxml(dom, root, pxml)

# playground

print(root[1][2][0].text)

print('THE END')
