import json

def read_fhir_bundle(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    print("Reading FHIR Bundle...\n")

    # get() ensures safe access
    for entry in data.get('entry', []):
        resource = entry.get('resource', {})

        # Check only Patient resources
        if resource.get('resourceType') == 'Patient':
            # Safe extraction of name
            name_info = resource.get('name', [{}])
            name = name_info[0]

            given = name.get('given', [''])[0]
            family = name.get('family', '')

            print(f"Patient Name : {given} {family}")
            print(f"Gender       : {resource.get('gender', 'N/A')}")
            print(f"Birth Date   : {resource.get('birthDate', 'N/A')}")
            print("-" * 30)


if __name__ == "__main__":
    read_fhir_bundle('input/Bundle.json')