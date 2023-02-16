import grpc

from message_pb2 import AccessToken
from message_pb2_grpc import DataServiceStub

def run_client():
    channel = grpc.insecure_channel("localhost:50051")
    stub = DataServiceStub(channel)
    response = stub.GetData(AccessToken(token="secret_token1"))
    print(response.data)

run_client()
