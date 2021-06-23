from lxml import etree

root_elem = etree.Element('html')
etree.SubElement(root_elem, 'head')
etree.SubElement(root_elem, 'title')
etree.SubElement(root_elem, 'body')
print(etree.tostring(root_elem, pretty_print=True).decode("utf-8"))

print(etree.iselement(root_elem))

from lxml import etree

html = etree.Element("html", lang="en_GB")
html.set("best", "JournalDev")
print(html.get("best"))
print(html.get("lang"))
etree.SubElement(html, "head").text = "Head of HTML"
etree.SubElement(html, "title").text = "I am the title!"
etree.SubElement(html, "body").text = "Here is the body"
print(etree.tostring(html, pretty_print=True).decode("utf-8"))

html = etree.XML('<html><head>Head of HTML</head><title>I am the title!</title><body>Here is the body</body></html>')
print(etree.tostring(html, pretty_print=True).decode('utf-8'))

html = etree.XML('<html><head>Head of HTML</head><title>I am the title!</title><body>Here is the body</body></html>')
print(etree.tostring(html, xml_declaration=True).decode('utf-8'))
