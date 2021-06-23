from lxml.etree import parse, XMLSchema, XMLParser, fromstring


def validate1(xmlschema: XMLSchema, xmlfilename):
    try:
        xmlschema.assertValid(parse(xmlfilename))
        return True
    except Exception as err:
        print(err)
        return False


def validate(xmlparser, xmlfilename):
    try:
        with open(xmlfilename, 'rb') as fp:
            fromstring(fp.read(), xmlparser)
        return True
    except Exception as err:
        print(err)
        return False


file_names = [f'sample{i}.xml' for i in range(6)]

schema = XMLSchema(file="sample_schema.xsd")
parser = XMLParser(schema=schema)

for file_name in file_names:
    # if validate(parser, file_name):
    if validate1(schema, file_name):
        print(f"{file_name} validates")
    else:
        print(f"{file_name} doesn't validates")
