import socket
import common_socket as cs 
import ast

server_addr = HOST, PORT = "255.255.255.255", 9999

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

try:
    # Send Discovery Message to Server
    bytesdata = bytes('Discovery Message', 'utf-8')
    sock.sendto(bytesdata,server_addr)

    # Accept the Network DB from server and print
    db_data, server_addr = sock.recvfrom(1024)
    cs.print_db_data( ast.literal_eval(db_data.decode('utf-8')) ) 

    # Accept what user chooses and send to Server
    user_nw_choice = bytes(str(input('Enter Your Subnet/Network Choice : ')), 'utf-8')
    sock.sendto(user_nw_choice,server_addr)

    # Accept Configuration 
    configuration, server_addr = sock.recvfrom(1024)
    configuration = ast.literal_eval(configuration.decode('utf-8'))
    
    status_word = '404'

    if(configuration['status'] == '200'):
    	print(configuration)
    	status_word = '200'
    	cs.setup_ip_configuration(configuration)


    # Send Acknowledgment and close the Protocol
    ack = bytes({
    		"status" : status_word,
    	})
    sock.sendto(ack,server_addr) 

    sock.close()


finally:
    # shut down
    sock.close()


