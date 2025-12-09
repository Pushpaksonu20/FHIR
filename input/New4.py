import json

# newline delimited json
def read_ndjson(file_path):
    with open(file_path, "r") as f:
        for line in f:
            resource = json.loads(line)

            # Only process Patient resources
            if resource.get("resourceType") == "Patient":

                name = resource.get("name", [{}])[0]
                given = name.get("given", [""])[0]
                family = name.get("family", "")

                print(
                    f"Patient: {given} {family}, Gender: {resource.get('gender', 'N/A')}"
                )


if __name__ == "__main__":
    read_ndjson("input/patients.ndjson")