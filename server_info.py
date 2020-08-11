import time
from concurrent import futures
import grpc

import personinfo_pb2
import personinfo_pb2_grpc


class PersonInfo(personinfo_pb2_grpc.PersonInfoServicer):

    def person(self, request, context):
        response = personinfo_pb2.Info()
        name = request.name
        surname = request.surname
        age = request.age
        response.text = "Ваше имя: " + name + " фамилия: " + surname + " возраст: " + str(age)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    personinfo_pb2_grpc.add_PersonInfoServicer_to_server(PersonInfo(), server)
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
