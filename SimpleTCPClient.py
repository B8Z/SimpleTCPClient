import socket

##
#   Author: Adam Bates
#   Date: 2/28/2020
#   Project: SimpleTCPClient -
#   Sends and receives messages from a server using sockets
##

#create vars to hold connection info
port_to_connect = 3223
host_to_connect = "enigma.pcs.cnu.edu"
BUFFER_SIZE = 256
name = "Adam Bates"

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Try catch ensures a failed network connection error is handled
try:
    #Connect to correct host / port
    s.connect((host_to_connect, port_to_connect))
    print("Connected to server")
except socket.error:
    print("Failed to connect")

#Get number response from server
response = s.recv(BUFFER_SIZE)
print(response)

#Increment number by one
send_response = int(response) + 1
send_response_string = str(send_response)
print (send_response)

#Send number back
s.send(send_response_string + "\n")
print("sending incremented integer response")

#Receive name request from server
response_name = s.recv(BUFFER_SIZE)
print (response_name)

#Send name to server
s.send(name + "\n")
print("sending name to server")

#Receive final ACK
ack = s.recv(BUFFER_SIZE)
print (ack)

#Close the socket, connection finished
print "closing socket"
s.close()
