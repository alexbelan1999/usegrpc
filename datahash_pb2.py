# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datahash.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='datahash.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x64\x61tahash.proto\"\x14\n\x04Text\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x14\n\x05Image\x12\x0b\n\x03img\x18\x01 \x01(\x0c\x32\xe2\x01\n\x08\x44\x61taHash\x12\x1c\n\tget_image\x12\x05.Text\x1a\x06.Image\"\x00\x12\x1a\n\x08hash_md5\x12\x05.Text\x1a\x05.Text\"\x00\x12\x1d\n\x0bhash_sha256\x12\x05.Text\x1a\x05.Text\"\x00\x12\x17\n\x05hello\x12\x05.Text\x1a\x05.Text\"\x00\x12\x1f\n\x0bstream_text\x12\x05.Text\x1a\x05.Text\"\x00\x30\x01\x12 \n\x0cinput_stream\x12\x05.Text\x1a\x05.Text\"\x00(\x01\x12!\n\x0b\x64ual_stream\x12\x05.Text\x1a\x05.Text\"\x00(\x01\x30\x01\x62\x06proto3'
)




_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Text.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=38,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='img', full_name='Image.img', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=60,
)

DESCRIPTOR.message_types_by_name['Text'] = _TEXT
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), {
  'DESCRIPTOR' : _TEXT,
  '__module__' : 'datahash_pb2'
  # @@protoc_insertion_point(class_scope:Text)
  })
_sym_db.RegisterMessage(Text)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'datahash_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  })
_sym_db.RegisterMessage(Image)



_DATAHASH = _descriptor.ServiceDescriptor(
  name='DataHash',
  full_name='DataHash',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=63,
  serialized_end=289,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_image',
    full_name='DataHash.get_image',
    index=0,
    containing_service=None,
    input_type=_TEXT,
    output_type=_IMAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='hash_md5',
    full_name='DataHash.hash_md5',
    index=1,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='hash_sha256',
    full_name='DataHash.hash_sha256',
    index=2,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='hello',
    full_name='DataHash.hello',
    index=3,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stream_text',
    full_name='DataHash.stream_text',
    index=4,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='input_stream',
    full_name='DataHash.input_stream',
    index=5,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='dual_stream',
    full_name='DataHash.dual_stream',
    index=6,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAHASH)

DESCRIPTOR.services_by_name['DataHash'] = _DATAHASH

# @@protoc_insertion_point(module_scope)
