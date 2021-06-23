from lxml import etree
from lxml import etree as et

# create 0
root_elem = etree.Element('html')
etree.SubElement(root_elem, 'head')
etree.SubElement(root_elem, 'title')
etree.SubElement(root_elem, 'body')
print(etree.tostring(root_elem, pretty_print=True).decode("utf-8"))

# test
print(etree.iselement(root_elem))
print('\n\n')

# Create 1
html = etree.Element("html", lang="en_GB")
html.set("best", "JournalDev")
print(html.get("best"))
print(html.get("lang"))
etree.SubElement(html, "head").text = "Head of HTML"
etree.SubElement(html, "title").text = "I am the title!"
etree.SubElement(html, "body").text = "Here is the body"
print(etree.tostring(html, pretty_print=True).decode("utf-8"))
print('\n\n')

# create 3
html = etree.XML('<html><head>Head of HTML</head><title>I am the title!</title><body>Here is the body</body></html>')
print(etree.tostring(html, xml_declaration=True, pretty_print=True).decode('utf-8'))
print('\n\n')

# create 4
root = et.Element('html', version="5.0")
root.set('newAttribute', 'attributeValue')
# Pass the parent node, name of the child node,
# and any number of optional attributes
et.SubElement(root, 'head')
et.SubElement(root, 'title', bgcolor="red", fontsize='22')
et.SubElement(root, 'body', fontsize="15")

# Add text to the Elements and SubElements
root.text = "This is an HTML file"
root[0].text = "This is the head of that file"
root[1].text = "This is the title of that file"
root[2].text = "This is the body of that file and would contain paragraphs etc"

# Use pretty_print=True to indent the HTML output
print(et.tostring(root, pretty_print=True).decode("utf-8"))

print(root.get('newAttribute'))
print(root[1].get('alpha'))  # root[1] accesses the `title` element
print(root[1].get('bgcolor'))
print('\n\n')

# create 5

xml = '<html><body>Hello</body></html>'
root = etree.fromstring(xml)
etree.dump(root)
print('\n\n')

from lxml import etree

root = etree.Element("html")
head = etree.SubElement(root, "head")
title = etree.SubElement(head, "title")
title.text = "This is Page Title"
body = etree.SubElement(root, "body")
heading = etree.SubElement(body, "h1", style="font-size:20pt", id="head")
heading.text = "Hello World!"
para = etree.SubElement(body, "p", id="firstPara")
para.text = "This HTML is XML Compliant!"
para = etree.SubElement(body, "p", id="secondPara")
para.text = "This is the second paragraph."

etree.dump(root)  # prints everything to console. Use for debug only