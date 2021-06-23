from lxml import etree
doc = etree.parse('movies.xml')

memoryElem = doc.find('movie')
print(memoryElem.text)        # element text
print(memoryElem.get('name')) # attribute

from lxml import etree

doc = etree.parse('file.xml')
memoryElem = doc.xpath('(//BodyNum)[1]/text()')
print(memoryElem)   # ['6168']


from lxml import etree

root_elem = etree.Element('html')
etree.SubElement(root_elem, 'head')
etree.SubElement(root_elem, 'title')
etree.SubElement(root_elem, 'body')
print(etree.tostring(root_elem, pretty_print=True).decode("utf-8"))

