# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/domain/service/get_remaining_budget_service.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/node/domain/service/get_remaining_budget_service.proto",
    package="syft.core.node.common.service",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nAproto/core/node/domain/service/get_remaining_budget_service.proto\x12\x1dsyft.core.node.common.service\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\x93\x01\n\x19GetRemainingBudgetMessage\x12%\n\x06msg_id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x7f\n\x1eGetRemainingBudgetReplyMessage\x12\x0e\n\x06\x62udget\x18\x01 \x01(\x02\x12%\n\x06msg_id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Addressb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_GETREMAININGBUDGETMESSAGE = _descriptor.Descriptor(
    name="GetRemainingBudgetMessage",
    full_name="syft.core.node.common.service.GetRemainingBudgetMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.GetRemainingBudgetMessage.msg_id",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.GetRemainingBudgetMessage.address",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.core.node.common.service.GetRemainingBudgetMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=169,
    serialized_end=316,
)


_GETREMAININGBUDGETREPLYMESSAGE = _descriptor.Descriptor(
    name="GetRemainingBudgetReplyMessage",
    full_name="syft.core.node.common.service.GetRemainingBudgetReplyMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="budget",
            full_name="syft.core.node.common.service.GetRemainingBudgetReplyMessage.budget",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.GetRemainingBudgetReplyMessage.msg_id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.GetRemainingBudgetReplyMessage.address",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=318,
    serialized_end=445,
)

_GETREMAININGBUDGETMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETREMAININGBUDGETMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETREMAININGBUDGETMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETREMAININGBUDGETREPLYMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETREMAININGBUDGETREPLYMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name[
    "GetRemainingBudgetMessage"
] = _GETREMAININGBUDGETMESSAGE
DESCRIPTOR.message_types_by_name[
    "GetRemainingBudgetReplyMessage"
] = _GETREMAININGBUDGETREPLYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRemainingBudgetMessage = _reflection.GeneratedProtocolMessageType(
    "GetRemainingBudgetMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETREMAININGBUDGETMESSAGE,
        "__module__": "proto.core.node.domain.service.get_remaining_budget_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.GetRemainingBudgetMessage)
    },
)
_sym_db.RegisterMessage(GetRemainingBudgetMessage)

GetRemainingBudgetReplyMessage = _reflection.GeneratedProtocolMessageType(
    "GetRemainingBudgetReplyMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETREMAININGBUDGETREPLYMESSAGE,
        "__module__": "proto.core.node.domain.service.get_remaining_budget_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.GetRemainingBudgetReplyMessage)
    },
)
_sym_db.RegisterMessage(GetRemainingBudgetReplyMessage)


# @@protoc_insertion_point(module_scope)
