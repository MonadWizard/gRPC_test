import grpc
import time
import psycopg2

from concurrent import futures

import example_pb2
import example_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ExampleService(example_pb2_grpc.ExampleServiceServicer):

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="secret"
        )

    def GetData(self, request, context):
        cur = self.conn.cursor()
        cur.execute("SELECT data FROM example_table WHERE id = %s", (request.id,))
        result = cur.fetchone()
        return example_pb2.Data(data=result[0])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
