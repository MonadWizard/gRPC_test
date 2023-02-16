import time

import grpc

from message_pb2 import DataResponse
from message_pb2_grpc import DataServiceServicer, add_DataServiceServicer_to_server
from concurrent.futures import ThreadPoolExecutor

class DataService(DataServiceServicer):
    def GetData(self, request, context):
        # Validate the access token
        if request.token != "secret_token":
            context.set_code(grpc.StatusCode.UNAUTHORIZED)
            context.set_details("Invalid access token")
            return DataResponse()
        
        return DataResponse(data="Hello, this is some data from the server!")

def run_server():
    server = grpc.server(thread_pool=ThreadPoolExecutor(max_workers=10))
    add_DataServiceServicer_to_server(DataService(), server)
    print("Starting server. Listening on port 50051.")
    server.add_insecure_port("[::]:50051")
    server.start()

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

run_server()