import grpc

import datahash_pb2
import datahash_pb2_grpc

channel = grpc.insecure_channel('localhost:64000')
stub = datahash_pb2_grpc.DataHashStub(channel)

person = input('Input your name: ')
text = input('Input message: ')

print("------------------------Simple RPC---------------")
to_hello = datahash_pb2.Text(data=text)
response = stub.hello(to_hello)
print(response.data)

to_md5 = datahash_pb2.Text(data=text)
response = stub.hash_md5(to_md5)
print(response.data)

to_sha256 = datahash_pb2.Text(data=text)
response = stub.hash_sha256(to_sha256)
print(response.data)

print("------------------------Response-streaming RPC---------------")
to_list = datahash_pb2.Text(data=text)
items = stub.stream_text(to_list)
for item in items:
    print(item.data)

print("------------------------Request-streaming RPC---------------")


def generator(info: list):
    for i in info:
        yield i


name = datahash_pb2.Text(data=person)
mesg = datahash_pb2.Text(data=text)
result_list = [name, mesg]

text_iterator = generator(result_list)
response = stub.input_stream(text_iterator)
print(response.data)

print("------------------------Bidirectional streaming RPC---------------")
name = datahash_pb2.Text(data=person)
mesg = datahash_pb2.Text(data=text)
result_list = [name, mesg]

text_iterator = generator(result_list)
response = stub.dual_stream(text_iterator)
for resp in response:
    print(resp.data)
