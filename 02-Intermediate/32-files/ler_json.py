import json

with open('teste3.json','r') as file:
    d1_json = file.read()
    print(d1_json)
    back_dict = json.loads(d1_json) # converter json para dict
    print(back_dict)

for k,v in back_dict.items():
    print(k)
    for k1,v1 in v.items():
        print(k1,v1)