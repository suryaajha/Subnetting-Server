import socket
import time
import json
import common_socket as cs

def load_network_data_from_db():

	decodedata = {}

	with open("data_file.json", "r") as read_file:
	    decodedata = json.load(read_file)

	cs.print_db_data(decodedata) 
	
	return decodedata


def create_valid_ip_configuration(network):
	'''
		Search for Valid IP address and create a dict configuration
		Return dict configuration
	'''
	configuration = {
		'ip_address_interface' : '192.168.2.12/25',
		'status' : '200'
	}

	return configuration

load_network_data_from_db() 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 9999))	

'''
	Protocol
	Step 1: Client Will connect to Server
	Step 1: Client Will Send Discover Message to Server
	Step 2: Server will send all the network list to client to choose the desired network
	Step 3: Client Will choose one subnet or network and send to client
	Step 4: Server will find One Valid IP and send to client
	Step 5: Client will accept the IP and setup IP and send ACK
	Step 6: Accept ACK and Mark done with client
'''

while True:

	# Accept Discover Message from Server
	disc_msg, address_of_client = server_socket.recvfrom(1024)

	# Send network list
	db_data = bytes(load_network_data_from_db())
	server_socket.sendto(db_data, address_of_client) 

	# Accept subnet or network from client
	client_nw_choice, address_of_client = server_socket.recvfrom(1024)
	print(client_nw_choice)

	# Find Valid IP and send to Client 
	configuration = bytes(create_valid_ip_configuration(client_nw_choice.decode('utf-8')))
	server_socket.sendto(configuration, address_of_client)

	# Recieve Ack and stop this 
	ack, address_of_client = server_socket.recvfrom(1024)
	print(ack)
	if(ack['status'] == '200'):
		print('Done with this client Start New Process Now')
   

server_socket.close() 