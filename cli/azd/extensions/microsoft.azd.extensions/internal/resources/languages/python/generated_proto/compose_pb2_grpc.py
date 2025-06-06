# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import compose_pb2 as compose__pb2
import models_pb2 as models__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in compose_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ComposeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListResources = channel.unary_unary(
                '/azdext.ComposeService/ListResources',
                request_serializer=models__pb2.EmptyRequest.SerializeToString,
                response_deserializer=compose__pb2.ListResourcesResponse.FromString,
                _registered_method=True)
        self.GetResource = channel.unary_unary(
                '/azdext.ComposeService/GetResource',
                request_serializer=compose__pb2.GetResourceRequest.SerializeToString,
                response_deserializer=compose__pb2.GetResourceResponse.FromString,
                _registered_method=True)
        self.ListResourceTypes = channel.unary_unary(
                '/azdext.ComposeService/ListResourceTypes',
                request_serializer=models__pb2.EmptyRequest.SerializeToString,
                response_deserializer=compose__pb2.ListResourceTypesResponse.FromString,
                _registered_method=True)
        self.GetResourceType = channel.unary_unary(
                '/azdext.ComposeService/GetResourceType',
                request_serializer=compose__pb2.GetResourceTypeRequest.SerializeToString,
                response_deserializer=compose__pb2.GetResourceTypeResponse.FromString,
                _registered_method=True)
        self.AddResource = channel.unary_unary(
                '/azdext.ComposeService/AddResource',
                request_serializer=compose__pb2.AddResourceRequest.SerializeToString,
                response_deserializer=compose__pb2.AddResourceResponse.FromString,
                _registered_method=True)


class ComposeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListResources(self, request, context):
        """ListResources retrieves all configured composability resources in the current project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetResource(self, request, context):
        """GetResource retrieves the configuration of a specific named composability resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListResourceTypes(self, request, context):
        """ListResourceTypes retrieves all supported composability resource types.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetResourceType(self, request, context):
        """GetResourceType retrieves the schema of a specific named composability resource type.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddResource(self, request, context):
        """AddResource adds a new composability resource to the current project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComposeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListResources': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResources,
                    request_deserializer=models__pb2.EmptyRequest.FromString,
                    response_serializer=compose__pb2.ListResourcesResponse.SerializeToString,
            ),
            'GetResource': grpc.unary_unary_rpc_method_handler(
                    servicer.GetResource,
                    request_deserializer=compose__pb2.GetResourceRequest.FromString,
                    response_serializer=compose__pb2.GetResourceResponse.SerializeToString,
            ),
            'ListResourceTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResourceTypes,
                    request_deserializer=models__pb2.EmptyRequest.FromString,
                    response_serializer=compose__pb2.ListResourceTypesResponse.SerializeToString,
            ),
            'GetResourceType': grpc.unary_unary_rpc_method_handler(
                    servicer.GetResourceType,
                    request_deserializer=compose__pb2.GetResourceTypeRequest.FromString,
                    response_serializer=compose__pb2.GetResourceTypeResponse.SerializeToString,
            ),
            'AddResource': grpc.unary_unary_rpc_method_handler(
                    servicer.AddResource,
                    request_deserializer=compose__pb2.AddResourceRequest.FromString,
                    response_serializer=compose__pb2.AddResourceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'azdext.ComposeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('azdext.ComposeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ComposeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/azdext.ComposeService/ListResources',
            models__pb2.EmptyRequest.SerializeToString,
            compose__pb2.ListResourcesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/azdext.ComposeService/GetResource',
            compose__pb2.GetResourceRequest.SerializeToString,
            compose__pb2.GetResourceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListResourceTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/azdext.ComposeService/ListResourceTypes',
            models__pb2.EmptyRequest.SerializeToString,
            compose__pb2.ListResourceTypesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetResourceType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/azdext.ComposeService/GetResourceType',
            compose__pb2.GetResourceTypeRequest.SerializeToString,
            compose__pb2.GetResourceTypeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/azdext.ComposeService/AddResource',
            compose__pb2.AddResourceRequest.SerializeToString,
            compose__pb2.AddResourceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
