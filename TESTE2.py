from os import path
import xml.etree.ElementTree as ET
from os import path

tree = ET.parse('config1.xml')
root = tree.getroot()

for x in root:
    print(x.tag, x.attrib)
    for y in x.getchildren():
        print("\t", y.tag, ":", y.text)
