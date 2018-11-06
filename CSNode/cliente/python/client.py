import grpc
import trafico_aereo_pb2 as pb


def main():
    

    # Create channel and stub to server's address and port.
    channel = grpc.insecure_channel('localhost:50050')
    stub = pb.ServicioAereoStub(channel)

    # Exception handling.
    
    try:
        response = stub.Despegue(pb.Request(ip_cliente = "ip_cliente"))
        print(response)
    # Catch any raised errors by grpc.
    except grpc.RpcError as e:
        print("Error raised: " + e.details())

    try:
        response2 = stub.Aterrizaje(pb.Employee(pos=0))
        print(response2.pos)
    # Catch any raised errors by grpc.
    except grpc.RpcError as e:
        print("Error raised: " + e.details())

if __name__ == '__main__':
    main()
