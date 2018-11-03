import socket
import pistas
import calculator_pb2
import calculator_pb2_grpc


HOST, PORT = '', 10000
alturas=set()
pistas=[1,0,1]
wait_queue=[]
ip_airport=dict()
arrivals=[]
departures=[]

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    http_response =str(pistas[0])
    client_connection.sendall(http_response)
    client_connection.close()
