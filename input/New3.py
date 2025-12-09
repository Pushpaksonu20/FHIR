import csv
import json

def load_csv_ids(file_path):
    # set = unordered collection of unique values
    ids = set()
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids.add(row["id"])
    return ids


def find_matching_patients(json_path, patient_ids):

    with open(json_path, "r") as f:
        bundle = json.load(f)

    print("Matching Patients:\n")

    for entry in bundle.get("entry", []):
        resource = entry.get("resource", {})

        # Match by Patient ID
        if resource.get("resourceType") == "Patient" and resource.get("id") in patient_ids:

            name = resource.get("name", [{}])[0]
            given = name.get("given", [""])[0]
            family = name.get("family", "")

            print(f"Matched: {given} {family}  (ID: {resource.get('id')})")

    print("-" * 40)


if __name__ == "__main__":
    patient_ids = load_csv_ids("input/patients.csv")
    find_matching_patients("input/Bundle.json", patient_ids)