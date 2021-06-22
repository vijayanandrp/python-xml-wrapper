from lxml import etree

# CREATE XML from Schema
import xmlschema
import json
from xml.etree.ElementTree import ElementTree

my_xsd = '<?xml version="1.0"?> <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"> <xs:element name="note" type="xs:string"/> </xs:schema>'
schema = xmlschema.XMLSchema(my_xsd)
data = json.dumps({'note': 'this is a Note text'})
xml = xmlschema.from_json(data, schema=schema, preserve_root=True)
ElementTree(xml).write('my_xml.xml')

# Read
# read the file and load it into a DOM tree
tree = etree.parse('IF_Generic.arxml')

# Fetch Values
for elem in tree.iterfind("//*"):
    # find elements that contain only text
    if len(elem) == 0 and elem.text and elem.text.strip() > '':
        # do your replacements ...
        elem.text = "new text"

# Update Text
from lxml import etree
import sys

tower_name = "Tower one"
meeting_room = "ABC"
timestamp = "2018-05-31 00:45:00"


def update_xml(to_update, params):
    try:
        node = to_update.xpath("/root/Towers/Tower[TowerName='{}']/MeetingRooms/*/"
                               "MeetingRoom[MeetingRoomName='{}']/"
                               "MeetingRoomAvailabilityInfo[MeetingRoomTimeStamp='{}']/isMeetingRoomAvailable"
                               .format(params.get("TowerName"), params.get("MeetingRoom"), params.get("timestamp")))[0]
    except IndexError:
        sys.exit("cant find the xpath to update")
    else:
        node.text = "1"


tree = etree.parse("test.xml")
update_xml(tree, {"TowerName": tower_name, "MeetingRoom": meeting_room, "timestamp": timestamp})

print(etree.tostring(tree, encoding="unicode", pretty_print=True))

# Update Tag

# Add Node
tree = etree.parse('books.xml')
new_entry = etree.fromstring('''<book category="web" cover="paperback">
<title lang="en">Learning XML 2</title>
<author>Erik Ray</author>
<year>2006</year>
<price>49.95</price>
</book>''')
root = tree.getroot()
root.append(new_entry)

# Write
# serialize the DOM tree and write it to file
tree.write('IF_Genericnew.arxml', pretty_print=True)
