import json

REQUIRED_FIELDS = ['name', 'gender', 'birthDate']


def read_fhir_bundle(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    print("Reading FHIR Bundle...\n")

    for entry in data.get('entry', []):
        resource = entry.get('resource', {})

        if resource.get('resourceType') == 'Patient':
            print(f"Validating patient ID: {resource.get('id')}\n")

            for field in REQUIRED_FIELDS:
                if field not in resource:
                    print(f"  MISSING FIELD: {field}")
                else:
                    print(f"  {field} found")

            print("_" * 40)  # Separator line


if __name__ == "__main__":
    read_fhir_bundle('input/Bundle.json')