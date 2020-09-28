import socket
import struct

server = "time-c-g.nist.gov"
port = 37
receive_buffer_size = 2**10
mysocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

mysocket.connect( ( server, port ) )

response_string = mysocket.recv( receive_buffer_size )


data1,= struct.unpack('!I' , response_string)


mysocket.close




server2 = "time-c-wwv.nist.gov"

mysocket2 = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

mysocket2.connect( ( server2, port ) )

response_string2 = mysocket2.recv( receive_buffer_size )

data2, = struct.unpack('!I', response_string2)


mysocket2.close



print("The IP address of server1 is:", socket.gethostbyname(server))
print("The IP address of server2 is:", socket.gethostbyname(server2))
print("Time of server1:",data1,"s")
print("Time of server2:",data2,"s")
print("The time difference between the 2 times:",abs(data1-data2))

