import grpc

import datahash_pb2
import datahash_pb2_grpc

channel = grpc.insecure_channel('localhost:64000')
stub = datahash_pb2_grpc.DataHashStub(channel)

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

print("------------------------Response-streaming RPC ---------------")
to_list = datahash_pb2.Text(data=text)
items = stub.stream_text(to_list)
for item in items:
    print(item.data)
