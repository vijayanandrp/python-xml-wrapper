# CREATE XML from Schema
import xmlschema
import json
from xml.etree.ElementTree import ElementTree

my_xsd = '<?xml version="1.0"?> <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"> <xs:element name="note" type="xs:string"/> </xs:schema>'
schema = xmlschema.XMLSchema(my_xsd)
data = json.dumps({'note': 'this is a Note text'})
xml = xmlschema.from_json(data, schema=schema, preserve_root=True)
ElementTree(xml).write('xmlschema_example.xml')
