import xml.etree.ElementTree as ET 
  
tree = ET.parse('config1.xml') 
root = tree.getroot() 


for child in root.findall("aliases/alias"):
    for title in child.findall("address"):
        print(title.text)
        print("\n")  
print(root) 
print(root[1].attrib) 
  
print(root[2][0].text) 
