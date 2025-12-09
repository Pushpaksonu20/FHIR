import json 

# with open('Patient.json','r') as file:
#     python_obj=json.load(file)

# print(python_obj)
# print(python_obj['name'])
# print(type(python_obj['name']))

# print(python_obj['value'])
# print(type(python_obj['value']))

# print(python_obj)
# dict2={"name":"Rajesh","value":83}
# list1=[python_obj,dict2]
# with open('storing_json.json','w',newline='') as file:
#     json.dump(list1,file,indent=4)
        

# print("New json file has been successfully created")

with open('Bundle.json','r') as file:
    python_obj=json.load(file)

print(python_obj)
print('-'*150)
print(python_obj['entry']) # list of resources
print('-'*150)
for entry in python_obj['entry']:
    print(entry['fullUrl'])
    print(entry['resource']['name'])
    names=entry['resource']['name'] # single list of a dictionary
    for name in names:
        print(name.get('family'))
        print(name.get('given')[0])
    print('-'*150)
    
    

