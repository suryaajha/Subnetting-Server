import ipaddress 
import math
from os import system

def print_db_data(db_data):
	for network in db_data['networks']:
		network_addr = next(iter(network))
		print(network_addr)
		for subnet in network[next(iter(network))]['subnets']:
			network_addr = next(iter(subnet))
			print('\t' + network_addr)


def create_network():

	name_of_network = input('Enter Name Of Network : ')
	main_network = input('Enter Main Network : ')
	num_of_subnets = int(input('Enter Number of Subnets you want to make : '))

	network = ipaddress.ip_network(main_network)

	prefixlen = math.ceil(math.log(num_of_subnets,2))

	subnets = list(network.subnets(prefixlen_diff=prefixlen))

	configuration = {
		"name" : name_of_network,
		"main_network_address" : main_network,
		"num_of_subnets" : num_of_subnets,
		"netmask" : str(network.netmask),
		"subnets_network_address" : subnets,
		"subnets_network_netmask" : subnets[0].netmask
	}

	if(subnets[0].netmask == subnets[1].netmask):
		print('Superb')

	print(configuration)

	print(main_network, num_of_subnets)

	return configuration


def setup_ip_configuration(configuration):
	pass

def pint_to_destination(destination):
	if system('ping ' + destination + ' -c 1'):
		return False
	else:
		return True