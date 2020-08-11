import grpc

import personinfo_pb2
import personinfo_pb2_grpc


def person_info(stub, name, surname, age):
    person = personinfo_pb2.Person(name=name, surname=surname, age=age)
    response = stub.person(person)
    print(response.text)


def client():
    with grpc.insecure_channel('localhost:64000') as channel:
        stub = personinfo_pb2_grpc.PersonInfoStub(channel)
        name = input('Input your name: ')
        surname = input('Input your surname: ')
        age = int(input('Input your age: '))
        person_info(stub, name, surname, age)


if __name__ == '__main__':
    client()
