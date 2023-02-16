import grpc
from concurrent import futures
import time
from fromprotobuffer import test2_pb2
from fromprotobuffer import test2_pb2_grpc
import utilities.calculator as calculator


class CalculatorServicer(test2_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        print("Received request for square root of " + str(request.value))
        response = test2_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

    def Addition(self, request, context):
        print("Received request for addition of " + str(request.value))
        response = test2_pb2.Number()
        response.value = calculator.addition(request.value)
        return response

    def Multiplication(self, request, context):
        print("Received request for multiplication of " + str(request.value))
        response = test2_pb2.Number()
        response.value = calculator.multiplication(request.value)
        return response



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test2_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    print("Starting server. Listening on port 50051.")
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

serve()