#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint


def count_tags(filename):
    tags = {}

    for i, elem in ET.iterparse(filename):
        if elem.tag not in tags:
            tags[elem.tag] = 1
        else:
            tags[elem.tag] += 1
    return tags


def test():

    tags = count_tags('../datasets/miami_florida.osm')
    pprint.pprint(tags)

    assert tags == {'bounds': 1,
                     'member': 41318,
                     'nd': 1528978,
                     'node': 1287549,
                     'osm': 1,
                     'relation': 1324,
                     'tag': 1381493,
                     'way': 169992}

if __name__ == "__main__":
    test()