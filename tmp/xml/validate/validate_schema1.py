import xmlschema


def validate(schema: xmlschema.XMLSchema, filename):
    try:
        # validate(self, source, path=None, schema_path=None, use_defaults=True,
        #          namespaces=None, max_depth=None, extra_validator=None):
        # schema.validate(filename)
        for error in schema.iter_errors(filename):
            print(error)
        return True
    except Exception as err:
        print(err)
        return False


file_names = [f'sample{i}.xml' for i in range(6)]
schema = xmlschema.XMLSchema("sample_schema.xsd")

for file_name in file_names:
    # if '3' not in file_name:
    #     continue
    if validate(schema, file_name):
        print(f"{file_name} validates")
    else:
        print(f"{file_name} doesn't validates")
    print('---' * 25)
