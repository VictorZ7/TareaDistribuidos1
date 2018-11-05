import grpc
import trafico_aereo_pb2 as pb


def main():
    """Python Client for Employee leave days"""

    # Create channel and stub to server's address and port.
    channel = grpc.insecure_channel('localhost:50050')
    stub = pb.EmployeeLeaveDaysServiceStub(channel)

    # Exception handling.
    
    try:
        # Check if the Employee is eligible or not.
        response = stub.EligibleForLeave(pb.Request(ip_client = "ip client"))
        print(response)

    # Catch any raised errors by grpc.
    except grpc.RpcError as e:
        print("Error raised: " + e.details())

if __name__ == '__main__':
    main()
