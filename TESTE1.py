import xml.etree.ElementTree as ET

tree = ET.parse('config1.xml')
root = tree.getroot()

filtro = "*"
for child in root.iter(filtro):
    print(child.tag, child.text)

# print("\n")

# for child in root.findall("alias"):
#    for esse in child.findall("address"):
#        print(esse.text)


for child in root.findall("aliases/alias"):
    for title in child.findall("address"):
        print(title.text)
        print("\n")
