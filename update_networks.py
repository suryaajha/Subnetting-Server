import common_socket as cs 
import json

#print(cs.pint_to_destination('localhost'))

#cs.create_network() 

with open("data_file.json", "r") as read_file:
    decodedata = json.load(read_file)
    configuration = cs.create_network() 

    configuration = {
		"name" : name_of_network,
		"main_network_address" : main_network,
		"num_of_subnets" : num_of_subnets,
		"netmask" : str(network.netmask),
		"subnets_network_address" : subnets,
		"subnets_network_netmask" : subnets[0].netmask
	}

    new_entry = {
    	configuration['main_network_address'] : { 
    		"name" : configuration['name'],
    		"subnet_mask" : configuration['netmask'],
    		"subnets" : [],
    		"ip_used" : [],
    		"num_of_subnets" : configuration['']
    	}
    }

# with open("data_file.json", "w") as write_file:
#     json.dump(db_data, write_file, indent=4)

 

# with open("data_file.json", "r") as read_file:
#     decodedata = json.load(read_file)
#     print(decodedata)