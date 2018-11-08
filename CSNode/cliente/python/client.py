import grpc
import trafico_aereo_pb2 as pb
import time

def main():

    id=raw_input("Ingrese IP del Avion:")
    torre=raw_input("Ingrese Destino:")
    pasajeros=524
    comb=200
    # Create channel and stub to server's address and port.
    channel = grpc.insecure_channel('localhost:'+torre)
    stub = pb.ServicioAereoStub(channel)

    # Exception handling.

    try:
        response = stub.IP(pb.Request(ip_cliente=id))
        print(response)
    # Catch any raised errors by grpc.
    except grpc.RpcError as e:
        print("Error raised: " + e.details())

    try:
        response2 = stub.Aterrizaje(pb.Request_Aterrizar())
        while(response2.pos==-1):
                print("No hay pistas disponibles de aterrizaje debe esperar")
                time.sleep(5)
                response2 = stub.Aterrizaje(pb.Request_Aterrizar())
        print("Puede aterrizar en pista"+str(response2.pos+1))

    # Catch any raised errors by grpc.
    except grpc.RpcError as e:
        print("Error raised: " + e.details())

    time.sleep(2)
    try:
        response3 = stub.Despegue(pb.Request_Despegar())
        while(response3.pos_d==-1):
            print("No hay pistas disponibles de despegue debe esperar")
            time.sleep(5)
            response3 = stub.Despegue(pb.Request_Despegar())
        print("Puede despegar en pista"+str(response3.pos_d+1))
        time.sleep(3)


    # Catch any raised errors by grpc.
    except grpc.RpcError as e:
        print("Error raised: " + e.details())
    try:
        response4 = stub.Dejar_air(pb.r_estado_avion(fuel=comb,psj=pasajeros,ip_a=id))


        # Catch any raised errors by grpc.
    except grpc.RpcError as e:
            print("Error raised: " + e.details())
    try:
        channel = grpc.insecure_channel('localhost:'+str(response4.fuel))
        print response4.fuel
        stub = pb.ServicioAereoStub(channel)
    except grpc.RpcError as e:
        print("Error raised: " + e.details())
if __name__ == '__main__':
    main()
