import json




# Deserialization -> vice versa of serialization
json_string='{"name":"Pushpak L","id":1}'

python_dict=json.loads(json_string)
print(python_dict)

print(python_dict.get('name'))
print(python_dict.keys())
print(type(python_dict))

# serialization -> convert other format data (like object datas like class,list etc)
# to json etc format

serialize=json.dumps(python_dict,indent=6)
print(serialize)
print(type(serialize))

person = {
    "name": {
        "first": "John",
        "last": "Doe"
    },
    "contacts": [
        {"type": "email", "value": "john@example.com"},
        {"type": "phone", "value": "+91-1234567890"}
    ]
}

print('first Name: ',person['name']['first'])
print('Last Name: ',person['name']['last'])

for contact in person['contacts']:
    print(f"{contact['type']} : {contact['value']}")

with open('Patient.json','r') as file:
    stringy=json.load(file)
print(stringy)

with open('Output.json','w') as file:
    json.dump(stringy,file,indent=2)



