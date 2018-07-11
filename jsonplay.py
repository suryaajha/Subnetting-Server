import json 

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

db_data = {
    "networks": [
        {
            "192.168.1.0/24": {
                "name" : "Printer 101 Hack network",
                "subnets" : [
                    {
                        "192.168.1.128/25":{
                            "name" : "Subnet1",
                        }
                    }
                ],
                "ip_used" : [],
                "subnet_mask" : "255.255.255.0",
                "first_addr" : "",
                "last_addr" : "" ,
            }
        }, 
        {
            "192.168.1.0/24": {
                "name" : "Hacking Class network",
                "subnets" : [],
                "ip_used" : [],
                "subnet_mask" : "255.255.255.0",
                "first_addr" : "",
                "last_addr" : "" ,
            }
        },
    ],
}

print(db_data['networks'][0]['192.168.1.0/24']['name'])

print()
print()
print()

print(json.loads(json.dumps(db_data)) ) 

print(db_data)

decodedata = {} 

with open("data_file.json", "w") as write_file:
    json.dump(db_data, write_file, indent=4)

 

with open("data_file.json", "r") as read_file:
    decodedata = json.load(read_file)
    print(decodedata)

print(decodedata)