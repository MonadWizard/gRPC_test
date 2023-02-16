import grpc

from fromprotobuffer import test2_pb2
from fromprotobuffer import test2_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        number = test2_pb2.Number(value=15)
        stub = test2_pb2_grpc.CalculatorStub(channel)
        # response = stub.SquareRoot(number)
        response = stub.Addition(number)
        # response = stub.Multiplication(number)

        print("Square root of " + str(number.value) + " is " + str(response.value))

run()
