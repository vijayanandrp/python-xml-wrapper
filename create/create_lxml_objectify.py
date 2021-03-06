"""
<?xml version="1.0" ?>
<zAppointments reminder="15">
    <appointment>
        <begin>1181251680</begin>
        <uid>040000008200E000</uid>
        <alarmTime>1181572063</alarmTime>
        <state></state>
        <location></location>
        <duration>1800</duration>
        <subject>Bring pizza home</subject>
    </appointment>
    <appointment>
        <begin>1234360800</begin>
        <duration>1800</duration>
        <subject>Check MS Office website for updates</subject>
        <location></location>
        <uid>604f4792-eb89-478b-a14f-dd34d3cc6c21-1234360800</uid>
        <state>dismissed</state>
  </appointment>
</zAppointments>
"""

# RECREATE
from lxml import etree, objectify


def create_appt(data):
    """
    Create an appointment XML element
    """
    appt = objectify.Element("appointment")
    appt.begin = data["begin"]
    appt.uid = data["uid"]
    appt.alarmTime = data["alarmTime"]
    appt.state = data["state"]
    appt.location = data["location"]
    appt.duration = data["duration"]
    appt.subject = data["subject"]
    return appt


def create_xml():
    """
    Create an XML file
    """

    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <zAppointments>
    </zAppointments>
    '''
    parser = etree.XMLParser(remove_blank_text=True)

    root = objectify.fromstring(xml.encode('utf-8'), parser=parser)
    root.set("reminder", "15")

    appt = create_appt({"begin": 1181251680,
                        "uid": "040000008200E000",
                        "alarmTime": 1181572063,
                        "state": "",
                        "location": "",
                        "duration": 1800,
                        "subject": "Bring pizza home"}
                       )
    root.append(appt)

    uid = "604f4792-eb89-478b-a14f-dd34d3cc6c21-1234360800"
    appt = create_appt({"begin": 1234360800,
                        "uid": uid,
                        "alarmTime": 1181572063,
                        "state": "dismissed",
                        "location": "",
                        "duration": 1800,
                        "subject": "Check MS Office website for updates"}
                       )
    root.append(appt)

    # remove lxml annotation
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)

    # create the xml string
    obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True).decode("utf-8")
    print(obj_xml)

    try:
        with open("lxml_objectify_example.xml", "w") as xml_writer:
            xml_writer.write(obj_xml)
    except IOError:
        pass


if __name__ == "__main__":
    create_xml()
