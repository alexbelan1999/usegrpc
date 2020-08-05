import grpc

import datahash_pb2
import datahash_pb2_grpc
from matplotlib import pyplot as plt


def get_image(stub, text):
    path = datahash_pb2.Text(data=text)
    response = stub.get_image(path)
    save_path = '/home/alex/PycharmProjects/usegrpc/client_img/icon.jpg'
    with open(save_path, 'wb') as image:
        image.write(response.img)
    img = plt.imread(save_path)
    plt.imshow(img)
    plt.show()


def simle_rcp(stub, text):
    to_hello = datahash_pb2.Text(data=text)
    response = stub.hello(to_hello)
    print(response.data)

    to_md5 = datahash_pb2.Text(data=text)
    response = stub.hash_md5(to_md5)
    print(response.data)

    to_sha256 = datahash_pb2.Text(data=text)
    response = stub.hash_sha256(to_sha256)
    print(response.data)


def resp_stream_rcp(stub, text):
    to_list = datahash_pb2.Text(data=text)
    items = stub.stream_text(to_list)
    for item in items:
        print(item.data)


def generator(info: list):
    for i in info:
        yield i


def req_stream_rcp(stub, person, text):
    name = datahash_pb2.Text(data=person)
    mesg = datahash_pb2.Text(data=text)
    result_list = [name, mesg]

    text_iterator = generator(result_list)
    response = stub.input_stream(text_iterator)
    print(response.data)


def bidirect_stream_rcp(stub, person, text):
    name = datahash_pb2.Text(data=person)
    mesg = datahash_pb2.Text(data=text)
    result_list = [name, mesg]

    text_iterator = generator(result_list)
    response = stub.dual_stream(text_iterator)
    for resp in response:
        print(resp.data)


def client():
    with grpc.insecure_channel('localhost:64000') as channel:
        stub = datahash_pb2_grpc.DataHashStub(channel)
        person = input('Input your name: ')
        text = input('Input message: ')
        print("------------------------Simple RPC---------------")
        simle_rcp(stub, text)
        print("------------------------Response-streaming RPC---------------")
        resp_stream_rcp(stub, text)
        print("------------------------Request-streaming RPC---------------")
        req_stream_rcp(stub, person, text)
        print("------------------------Bidirectional streaming RPC---------------")
        bidirect_stream_rcp(stub, person, text)
        path = input("Введите путь до файла: ")
        get_image(stub, path)


if __name__ == '__main__':
    client()
