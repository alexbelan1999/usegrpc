import time
from concurrent import futures

import grpc

import datahash
import datahash_pb2
import datahash_pb2_grpc


class DataHashServicer(datahash_pb2_grpc.DataHashServicer):

    def hash_md5(self, request, context):
        response = datahash_pb2.Text()
        response.data = datahash.hash_md5(request.data)
        return response

    def hash_sha256(self, request, context):
        response = datahash_pb2.Text()
        response.data = datahash.hash_sha256(request.data)
        return response

    def hello(self, request, context):
        response = datahash_pb2.Text()
        response.data = datahash.hello(request.data)
        return response

    def stream_text(self, request, context):
        hello = datahash.hello(request.data)
        hash_md5 = datahash.hash_md5(request.data)
        sha256 = datahash.hash_sha256(request.data)
        result = [hello, hash_md5, sha256]

        feature_list = []
        for item in result:
            feature = datahash_pb2.Text(data=item)
            feature_list.append(feature)

        for feature in feature_list:
            yield feature

    def input_stream(self, request_iterator, context):
        point_count = 0
        prev_point = None
        points = []

        for point in request_iterator:
            point_count += 1
            points.append(point.data)
            prev_point = point

        result = datahash.hello_person(points[0], points[1])
        return datahash_pb2.Text(data=result)

    def dual_stream(self, request_iterator, context):
        point_count = 0
        prev_point = None
        points = []

        for point in request_iterator:
            point_count += 1
            points.append(point.data)
            prev_point = point

        hello = datahash.hello_person(points[0], points[1])
        hash_md5 = datahash.hash_md5(points[1])
        sha256 = datahash.hash_sha256(points[1])
        result = [hello, hash_md5, sha256]

        feature_list = []
        for item in result:
            feature = datahash_pb2.Text(data=item)
            feature_list.append(feature)

        for feature in feature_list:
            yield feature


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    datahash_pb2_grpc.add_DataHashServicer_to_server(DataHashServicer(), server)
    print('Starting server on port 64000.')
    server.add_insecure_port('[::]:64000')
    server.start()

    try:
        while True:
            time.sleep(360)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
