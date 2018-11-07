# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trafico_aereo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trafico_aereo.proto',
  package='trafico_aereo',
  syntax='proto3',
  serialized_pb=_b('\n\x13trafico_aereo.proto\x12\rtrafico_aereo\"\x1d\n\x07Request\x12\x12\n\nip_cliente\x18\x01 \x01(\t\"\x1d\n\x08Response\x12\x11\n\tip_server\x18\x01 \x01(\t\" \n\x11Request_Aterrizar\x12\x0b\n\x03pos\x18\x01 \x01(\x05\")\n\x0c\x65stado_avion\x12\x0c\n\x04\x66uel\x18\x01 \x01(\x05\x12\x0b\n\x03psj\x18\x02 \x01(\x05\"5\n\x12Response_Aterrizar\x12\x0b\n\x03pos\x18\x01 \x01(\x05\x12\x12\n\nip_cliente\x18\x02 \x01(\t\"!\n\x10Request_Despegar\x12\r\n\x05pos_d\x18\x01 \x01(\x05\"\"\n\x11Response_Despegar\x12\r\n\x05pos_d\x18\x01 \x01(\x05\x32\xb0\x02\n\rServicioAereo\x12\x35\n\x02IP\x12\x16.trafico_aereo.Request\x1a\x17.trafico_aereo.Response\x12Q\n\nAterrizaje\x12 .trafico_aereo.Request_Aterrizar\x1a!.trafico_aereo.Response_Aterrizar\x12M\n\x08\x44\x65spegue\x12\x1f.trafico_aereo.Request_Despegar\x1a .trafico_aereo.Response_Despegar\x12\x46\n\tDejar_air\x12\x16.trafico_aereo.Request\x1a!.trafico_aereo.Response_Aterrizarb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='trafico_aereo.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_cliente', full_name='trafico_aereo.Request.ip_cliente', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=67,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='trafico_aereo.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_server', full_name='trafico_aereo.Response.ip_server', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=98,
)


_REQUEST_ATERRIZAR = _descriptor.Descriptor(
  name='Request_Aterrizar',
  full_name='trafico_aereo.Request_Aterrizar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='trafico_aereo.Request_Aterrizar.pos', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=132,
)


_ESTADO_AVION = _descriptor.Descriptor(
  name='estado_avion',
  full_name='trafico_aereo.estado_avion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fuel', full_name='trafico_aereo.estado_avion.fuel', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='psj', full_name='trafico_aereo.estado_avion.psj', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=175,
)


_RESPONSE_ATERRIZAR = _descriptor.Descriptor(
  name='Response_Aterrizar',
  full_name='trafico_aereo.Response_Aterrizar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='trafico_aereo.Response_Aterrizar.pos', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip_cliente', full_name='trafico_aereo.Response_Aterrizar.ip_cliente', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=230,
)


_REQUEST_DESPEGAR = _descriptor.Descriptor(
  name='Request_Despegar',
  full_name='trafico_aereo.Request_Despegar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_d', full_name='trafico_aereo.Request_Despegar.pos_d', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=265,
)


_RESPONSE_DESPEGAR = _descriptor.Descriptor(
  name='Response_Despegar',
  full_name='trafico_aereo.Response_Despegar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_d', full_name='trafico_aereo.Response_Despegar.pos_d', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=301,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Request_Aterrizar'] = _REQUEST_ATERRIZAR
DESCRIPTOR.message_types_by_name['estado_avion'] = _ESTADO_AVION
DESCRIPTOR.message_types_by_name['Response_Aterrizar'] = _RESPONSE_ATERRIZAR
DESCRIPTOR.message_types_by_name['Request_Despegar'] = _REQUEST_DESPEGAR
DESCRIPTOR.message_types_by_name['Response_Despegar'] = _RESPONSE_DESPEGAR

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'trafico_aereo_pb2'
  # @@protoc_insertion_point(class_scope:trafico_aereo.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'trafico_aereo_pb2'
  # @@protoc_insertion_point(class_scope:trafico_aereo.Response)
  ))
_sym_db.RegisterMessage(Response)

Request_Aterrizar = _reflection.GeneratedProtocolMessageType('Request_Aterrizar', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_ATERRIZAR,
  __module__ = 'trafico_aereo_pb2'
  # @@protoc_insertion_point(class_scope:trafico_aereo.Request_Aterrizar)
  ))
_sym_db.RegisterMessage(Request_Aterrizar)

estado_avion = _reflection.GeneratedProtocolMessageType('estado_avion', (_message.Message,), dict(
  DESCRIPTOR = _ESTADO_AVION,
  __module__ = 'trafico_aereo_pb2'
  # @@protoc_insertion_point(class_scope:trafico_aereo.estado_avion)
  ))
_sym_db.RegisterMessage(estado_avion)

Response_Aterrizar = _reflection.GeneratedProtocolMessageType('Response_Aterrizar', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_ATERRIZAR,
  __module__ = 'trafico_aereo_pb2'
  # @@protoc_insertion_point(class_scope:trafico_aereo.Response_Aterrizar)
  ))
_sym_db.RegisterMessage(Response_Aterrizar)

Request_Despegar = _reflection.GeneratedProtocolMessageType('Request_Despegar', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_DESPEGAR,
  __module__ = 'trafico_aereo_pb2'
  # @@protoc_insertion_point(class_scope:trafico_aereo.Request_Despegar)
  ))
_sym_db.RegisterMessage(Request_Despegar)

Response_Despegar = _reflection.GeneratedProtocolMessageType('Response_Despegar', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_DESPEGAR,
  __module__ = 'trafico_aereo_pb2'
  # @@protoc_insertion_point(class_scope:trafico_aereo.Response_Despegar)
  ))
_sym_db.RegisterMessage(Response_Despegar)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ServicioAereoStub(object):
  """Service. define the methods that the grpc server can expose to the client.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.IP = channel.unary_unary(
        '/trafico_aereo.ServicioAereo/IP',
        request_serializer=Request.SerializeToString,
        response_deserializer=Response.FromString,
        )
    self.Aterrizaje = channel.unary_unary(
        '/trafico_aereo.ServicioAereo/Aterrizaje',
        request_serializer=Request_Aterrizar.SerializeToString,
        response_deserializer=Response_Aterrizar.FromString,
        )
    self.Despegue = channel.unary_unary(
        '/trafico_aereo.ServicioAereo/Despegue',
        request_serializer=Request_Despegar.SerializeToString,
        response_deserializer=Response_Despegar.FromString,
        )
    self.Dejar_air = channel.unary_unary(
        '/trafico_aereo.ServicioAereo/Dejar_air',
        request_serializer=Request.SerializeToString,
        response_deserializer=Response_Aterrizar.FromString,
        )


class ServicioAereoServicer(object):
  """Service. define the methods that the grpc server can expose to the client.
  """

  def IP(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Aterrizaje(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Despegue(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Dejar_air(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServicioAereoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'IP': grpc.unary_unary_rpc_method_handler(
          servicer.IP,
          request_deserializer=Request.FromString,
          response_serializer=Response.SerializeToString,
      ),
      'Aterrizaje': grpc.unary_unary_rpc_method_handler(
          servicer.Aterrizaje,
          request_deserializer=Request_Aterrizar.FromString,
          response_serializer=Response_Aterrizar.SerializeToString,
      ),
      'Despegue': grpc.unary_unary_rpc_method_handler(
          servicer.Despegue,
          request_deserializer=Request_Despegar.FromString,
          response_serializer=Response_Despegar.SerializeToString,
      ),
      'Dejar_air': grpc.unary_unary_rpc_method_handler(
          servicer.Dejar_air,
          request_deserializer=Request.FromString,
          response_serializer=Response_Aterrizar.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'trafico_aereo.ServicioAereo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaServicioAereoServicer(object):
  """Service. define the methods that the grpc server can expose to the client.
  """
  def IP(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Aterrizaje(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Despegue(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Dejar_air(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaServicioAereoStub(object):
  """Service. define the methods that the grpc server can expose to the client.
  """
  def IP(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  IP.future = None
  def Aterrizaje(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Aterrizaje.future = None
  def Despegue(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Despegue.future = None
  def Dejar_air(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Dejar_air.future = None


def beta_create_ServicioAereo_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('trafico_aereo.ServicioAereo', 'Aterrizaje'): Request_Aterrizar.FromString,
    ('trafico_aereo.ServicioAereo', 'Dejar_air'): Request.FromString,
    ('trafico_aereo.ServicioAereo', 'Despegue'): Request_Despegar.FromString,
    ('trafico_aereo.ServicioAereo', 'IP'): Request.FromString,
  }
  response_serializers = {
    ('trafico_aereo.ServicioAereo', 'Aterrizaje'): Response_Aterrizar.SerializeToString,
    ('trafico_aereo.ServicioAereo', 'Dejar_air'): Response_Aterrizar.SerializeToString,
    ('trafico_aereo.ServicioAereo', 'Despegue'): Response_Despegar.SerializeToString,
    ('trafico_aereo.ServicioAereo', 'IP'): Response.SerializeToString,
  }
  method_implementations = {
    ('trafico_aereo.ServicioAereo', 'Aterrizaje'): face_utilities.unary_unary_inline(servicer.Aterrizaje),
    ('trafico_aereo.ServicioAereo', 'Dejar_air'): face_utilities.unary_unary_inline(servicer.Dejar_air),
    ('trafico_aereo.ServicioAereo', 'Despegue'): face_utilities.unary_unary_inline(servicer.Despegue),
    ('trafico_aereo.ServicioAereo', 'IP'): face_utilities.unary_unary_inline(servicer.IP),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_ServicioAereo_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('trafico_aereo.ServicioAereo', 'Aterrizaje'): Request_Aterrizar.SerializeToString,
    ('trafico_aereo.ServicioAereo', 'Dejar_air'): Request.SerializeToString,
    ('trafico_aereo.ServicioAereo', 'Despegue'): Request_Despegar.SerializeToString,
    ('trafico_aereo.ServicioAereo', 'IP'): Request.SerializeToString,
  }
  response_deserializers = {
    ('trafico_aereo.ServicioAereo', 'Aterrizaje'): Response_Aterrizar.FromString,
    ('trafico_aereo.ServicioAereo', 'Dejar_air'): Response_Aterrizar.FromString,
    ('trafico_aereo.ServicioAereo', 'Despegue'): Response_Despegar.FromString,
    ('trafico_aereo.ServicioAereo', 'IP'): Response.FromString,
  }
  cardinalities = {
    'Aterrizaje': cardinality.Cardinality.UNARY_UNARY,
    'Dejar_air': cardinality.Cardinality.UNARY_UNARY,
    'Despegue': cardinality.Cardinality.UNARY_UNARY,
    'IP': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'trafico_aereo.ServicioAereo', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
