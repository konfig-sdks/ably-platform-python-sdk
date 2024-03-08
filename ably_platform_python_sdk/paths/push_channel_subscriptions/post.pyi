# coding: utf-8

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from ably_platform_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from ably_platform_python_sdk.api_response import AsyncGeneratorResponse
from ably_platform_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ably_platform_python_sdk import schemas  # noqa: F401

from ably_platform_python_sdk.model.error import Error as ErrorSchema

from ably_platform_python_sdk.type.error import Error

from ...api_client import Dictionary
from ably_platform_python_sdk.pydantic.error import Error as ErrorPydantic

# Query params


class FormatSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def JSON(cls):
        return cls("json")
    
    @schemas.classproperty
    def JSONP(cls):
        return cls("jsonp")
    
    @schemas.classproperty
    def MSGPACK(cls):
        return cls("msgpack")
    
    @schemas.classproperty
    def HTML(cls):
        return cls("html")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'format': typing.Union[FormatSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
# Header params
XAblyVersionSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'X-Ably-Version': typing.Union[XAblyVersionSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_ably_version = api_client.HeaderParameter(
    name="X-Ably-Version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAblyVersionSchema,
)
# body param


class SchemaForRequestBodyApplicationJson(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class one_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    channel = schemas.StrSchema
                    deviceId = schemas.StrSchema
                    __annotations__ = {
                        "channel": channel,
                        "deviceId": deviceId,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["deviceId"]) -> MetaOapg.properties.deviceId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel", "deviceId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["deviceId"]) -> typing.Union[MetaOapg.properties.deviceId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel", "deviceId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
                deviceId: typing.Union[MetaOapg.properties.deviceId, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *args,
                    channel=channel,
                    deviceId=deviceId,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    channel = schemas.StrSchema
                    clientId = schemas.StrSchema
                    __annotations__ = {
                        "channel": channel,
                        "clientId": clientId,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel", "clientId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> typing.Union[MetaOapg.properties.clientId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel", "clientId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
                clientId: typing.Union[MetaOapg.properties.clientId, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *args,
                    channel=channel,
                    clientId=clientId,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaForRequestBodyApplicationXMsgpack(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class one_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    channel = schemas.StrSchema
                    deviceId = schemas.StrSchema
                    __annotations__ = {
                        "channel": channel,
                        "deviceId": deviceId,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["deviceId"]) -> MetaOapg.properties.deviceId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel", "deviceId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["deviceId"]) -> typing.Union[MetaOapg.properties.deviceId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel", "deviceId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
                deviceId: typing.Union[MetaOapg.properties.deviceId, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *args,
                    channel=channel,
                    deviceId=deviceId,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    channel = schemas.StrSchema
                    clientId = schemas.StrSchema
                    __annotations__ = {
                        "channel": channel,
                        "clientId": clientId,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel", "clientId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> typing.Union[MetaOapg.properties.clientId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel", "clientId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
                clientId: typing.Union[MetaOapg.properties.clientId, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *args,
                    channel=channel,
                    clientId=clientId,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationXMsgpack':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaForRequestBodyApplicationXWwwFormUrlencoded(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class one_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    channel = schemas.StrSchema
                    deviceId = schemas.StrSchema
                    __annotations__ = {
                        "channel": channel,
                        "deviceId": deviceId,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["deviceId"]) -> MetaOapg.properties.deviceId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel", "deviceId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["deviceId"]) -> typing.Union[MetaOapg.properties.deviceId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel", "deviceId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
                deviceId: typing.Union[MetaOapg.properties.deviceId, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *args,
                    channel=channel,
                    deviceId=deviceId,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    channel = schemas.StrSchema
                    clientId = schemas.StrSchema
                    __annotations__ = {
                        "channel": channel,
                        "clientId": clientId,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["channel", "clientId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> typing.Union[MetaOapg.properties.clientId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channel", "clientId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
                clientId: typing.Union[MetaOapg.properties.clientId, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *args,
                    channel=channel,
                    clientId=clientId,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationXWwwFormUrlencoded':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


request_body_typing_any = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/x-msgpack': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXMsgpack),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
)


@dataclass
class ApiResponseFor2XX(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor2XXAsync(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_2XX = api_client.OpenApiResponse(
    response_cls=ApiResponseFor2XX,
    response_cls_async=ApiResponseFor2XXAsync,
)
XAblyErrorcodeSchema = schemas.IntSchema
XAblyErrormessageSchema = schemas.StrSchema
XAblyServeridSchema = schemas.StrSchema
SchemaFor0ResponseBodyApplicationJson = ErrorSchema
SchemaFor0ResponseBodyApplicationXMsgpack = ErrorSchema
SchemaFor0ResponseBodyTextHtml = ErrorSchema
ResponseHeadersFor0 = typing_extensions.TypedDict(
    'ResponseHeadersFor0',
    {
        'x-ably-errorcode': XAblyErrorcodeSchema,
        'x-ably-errormessage': XAblyErrormessageSchema,
        'x-ably-serverid': XAblyServeridSchema,
    }
)


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Error


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
        'application/x-msgpack': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationXMsgpack),
        'text/html': api_client.MediaType(
            schema=SchemaFor0ResponseBodyTextHtml),
    },
    headers=[
        x_ably_errorcode_parameter,
        x_ably_errormessage_parameter,
        x_ably_serverid_parameter,
    ]
)
_all_accept_content_types = (
    'application/json',
    'application/x-msgpack',
    'text/html',
)


class BaseApi(api_client.Api):

    def _subscribe_push_device_to_channel_mapped_args(
        self,
        channel: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        body: typing.Optional[typing.Any] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _body = {}
        if channel is not None:
            _body["channel"] = channel
        if device_id is not None:
            _body["deviceId"] = device_id
        if client_id is not None:
            _body["clientId"] = client_id
        args.body = body if body is not None else _body
        if format is not None:
            _query_params["format"] = format
        if x_ably_version is not None:
            _header_params["X-Ably-Version"] = x_ably_version
        args.query = _query_params
        args.header = _header_params
        return args

    async def _asubscribe_push_device_to_channel_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor2XXAsync,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Subscribe a device to a channel
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_ably_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/push/channelSubscriptions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_typing_any.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _subscribe_push_device_to_channel_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor2XX,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Subscribe a device to a channel
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_ably_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/push/channelSubscriptions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_typing_any.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class SubscribePushDeviceToChannelRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asubscribe_push_device_to_channel(
        self,
        channel: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        body: typing.Optional[typing.Any] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor2XXAsync,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._subscribe_push_device_to_channel_mapped_args(
            body=body,
            channel=channel,
            device_id=device_id,
            client_id=client_id,
            x_ably_version=x_ably_version,
            format=format,
        )
        return await self._asubscribe_push_device_to_channel_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def subscribe_push_device_to_channel(
        self,
        channel: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        body: typing.Optional[typing.Any] = None,
    ) -> typing.Union[
        ApiResponseFor2XX,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._subscribe_push_device_to_channel_mapped_args(
            body=body,
            channel=channel,
            device_id=device_id,
            client_id=client_id,
            x_ably_version=x_ably_version,
            format=format,
        )
        return self._subscribe_push_device_to_channel_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

class SubscribePushDeviceToChannel(BaseApi):

    async def asubscribe_push_device_to_channel(
        self,
        channel: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        body: typing.Optional[typing.Any] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.asubscribe_push_device_to_channel(
            body=body,
            channel=channel,
            device_id=device_id,
            client_id=client_id,
            x_ably_version=x_ably_version,
            format=format,
            **kwargs,
        )
    
    
    def subscribe_push_device_to_channel(
        self,
        channel: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        body: typing.Optional[typing.Any] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.subscribe_push_device_to_channel(
            body=body,
            channel=channel,
            device_id=device_id,
            client_id=client_id,
            x_ably_version=x_ably_version,
            format=format,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        channel: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        body: typing.Optional[typing.Any] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor2XXAsync,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._subscribe_push_device_to_channel_mapped_args(
            body=body,
            channel=channel,
            device_id=device_id,
            client_id=client_id,
            x_ably_version=x_ably_version,
            format=format,
        )
        return await self._asubscribe_push_device_to_channel_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        channel: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        body: typing.Optional[typing.Any] = None,
    ) -> typing.Union[
        ApiResponseFor2XX,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._subscribe_push_device_to_channel_mapped_args(
            body=body,
            channel=channel,
            device_id=device_id,
            client_id=client_id,
            x_ably_version=x_ably_version,
            format=format,
        )
        return self._subscribe_push_device_to_channel_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

