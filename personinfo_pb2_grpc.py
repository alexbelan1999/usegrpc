# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import personinfo_pb2 as personinfo__pb2


class PersonInfoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.person = channel.unary_unary(
                '/PersonInfo/person',
                request_serializer=personinfo__pb2.Person.SerializeToString,
                response_deserializer=personinfo__pb2.Info.FromString,
                )


class PersonInfoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def person(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonInfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'person': grpc.unary_unary_rpc_method_handler(
                    servicer.person,
                    request_deserializer=personinfo__pb2.Person.FromString,
                    response_serializer=personinfo__pb2.Info.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PersonInfo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonInfo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def person(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonInfo/person',
            personinfo__pb2.Person.SerializeToString,
            personinfo__pb2.Info.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)