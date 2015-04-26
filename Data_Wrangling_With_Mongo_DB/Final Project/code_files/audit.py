"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "../datasets/miami_florida.osm"

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) #last word
#street_type_re = re.compile(r'([a-z]{1,4}\/)|(^\S*\.?)', re.IGNORECASE) #first word

street_types = defaultdict(set)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons",
            "Bend", "Circle", "Highway", "Lane", "Manor", "Parkway", "South", "Terrace", "Way"]

# UPDATE THIS VARIABLE
mapping = {"St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            "N.": "North",
            "S.": "South",
            "Rd": "Road",
            "Trl": "Trail",
            "Pkwy": "Parkway",
            "Ct": "Court",
            "Pl": "Place",
            "Ln": "Lane",
            "Blvd": "Boulevard",
            "BLVD": "Boulevard",
            "Bnd": "Bend",
            "Mnr": "Manor",
            "Hwy": "Highway",
            "Ter": "Terrace"}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)

    if m:
        street_type = m.group()

        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return elem.attrib['k'] == "addr:street"


def audit(osmfile):
    osm_file = open(osmfile, "r")


    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types

'''
def update_name(name, mapping):
    for s in mapping.keys():
        p = re.compile(s)
        if p.search(name):
            name = p.sub(mapping[s], name)
            return name

    return name
'''


# Modified to return street type
def update_name(name, mapping):

    if street_type_re.search(name) is not None:
        st_type = street_type_re.search(name).group()

        if st_type in mapping.keys():
            new_type = mapping[st_type]
            name = name.replace(st_type, new_type)
            return name, new_type
        return name, st_type
    else:
        return name, ""


def test():
    st_types = audit(OSMFILE)
    assert len(st_types) == 91
    # pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name, st_type = update_name(name, mapping)
            print name, "=>", better_name

if __name__ == '__main__':
    test()