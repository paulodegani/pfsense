import xml.etree.ElementTree as ET

tree = ET.parse('config.xml')
root = tree.getroot()
print(ET.tostring(root))
print(root.attrib)
root.set("canal","PyTAX")
tree.write("config.xml")
inf = root.get("canal")
print(f" o nome do canal é {inf}")
for desc in tree.findall('.//name'):
	print(desc.text)
