import xmlschema


def get_validation_errors(xml_file, xsd_file):
    schema = xmlschema.XMLSchema(xsd_file)
    validation_error_iterator = schema.iter_errors(xml_file)
    errors = list()
    for idx, validation_error in enumerate(validation_error_iterator, start=1):
        err = validation_error.__str__()
        errors.append(err)
        print(err)
    return errors

errors = get_validation_errors('sample3.xml', 'sample_schema.xsd')

errors = get_validation_errors('stackover.xml', 'stackover.xsd')

# print(errors)


# ------------------------------------------- +++++++++ ______________________________________

def validate(schema: xmlschema.XMLSchema, filename):
    try:
        for error in schema.iter_errors(filename):
            print(error)
        return True
    except Exception as err:
        print(err)
        return False


file_names = [f'sample{i}.xml' for i in range(6)]
schema = xmlschema.XMLSchema("sample_schema.xsd")

for file_name in file_names:
    if validate(schema, file_name):
        print(f"{file_name} validates")
    else:
        print(f"{file_name} doesn't validates")
    print('---' * 25)


