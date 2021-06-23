import xml.etree.ElementTree as ET

# create the file structure
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

# create a new XML file with the results
mydata = ET.tostring(data,encoding='unicode')
myfile = open("items2.xml", "w")
myfile.write(mydata)

import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()
# changing a field text
for elem in root.iter('item'):
    elem.text = 'new text'
# modifying an attribute
for elem in root.iter('item'):
    elem.set('name', 'newitem')
# adding an attribute
for elem in root.iter('item'):
    elem.set('name2', 'newitem2')
tree.write('newitems.xml')