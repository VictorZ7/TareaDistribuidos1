import socket

HOST, PORT = '', 10000
alturas=set()
pistas=[1,2,3]
busy_pistas=[]
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
    elementos=request.split(" ")
    print elementos[0],elementos[1],elementos[2]
    http_response =str(pistas[0])
    client_connection.sendall(http_response)
    client_connection.close()
