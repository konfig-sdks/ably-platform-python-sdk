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
from ably_platform_python_sdk.model.presence_message import PresenceMessage as PresenceMessageSchema

from ably_platform_python_sdk.type.error import Error
from ably_platform_python_sdk.type.presence_message import PresenceMessage

from ...api_client import Dictionary
from ably_platform_python_sdk.pydantic.presence_message import PresenceMessage as PresenceMessagePydantic
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
ClientIdSchema = schemas.StrSchema
ConnectionIdSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'format': typing.Union[FormatSchema, str, ],
        'clientId': typing.Union[ClientIdSchema, str, ],
        'connectionId': typing.Union[ConnectionIdSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
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
request_query_client_id = api_client.QueryParameter(
    name="clientId",
    style=api_client.ParameterStyle.FORM,
    schema=ClientIdSchema,
    explode=True,
)
request_query_connection_id = api_client.QueryParameter(
    name="connectionId",
    style=api_client.ParameterStyle.FORM,
    schema=ConnectionIdSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
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
# Path params
ChannelIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'channel_id': typing.Union[ChannelIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_channel_id = api_client.PathParameter(
    name="channel_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ChannelIdSchema,
    required=True,
)


class LinkSchema(
    schemas.StrSchema
):
    pass
XAblyServeridSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PresenceMessageSchema']:
            return PresenceMessageSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PresenceMessage'], typing.List['PresenceMessage']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PresenceMessage':
        return super().__getitem__(i)


class SchemaFor200ResponseBodyApplicationXMsgpack(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PresenceMessageSchema']:
            return PresenceMessageSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PresenceMessage'], typing.List['PresenceMessage']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyApplicationXMsgpack':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PresenceMessage':
        return super().__getitem__(i)
SchemaFor200ResponseBodyTextHtml = schemas.StrSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'link': LinkSchema,
        'x-ably-serverid': XAblyServeridSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.List[PresenceMessage]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.List[PresenceMessage]


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/x-msgpack': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXMsgpack),
        'text/html': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextHtml),
    },
    headers=[
        link_parameter,
        x_ably_serverid_parameter,
    ]
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

    def _get_presence_of_channel_mapped_args(
        self,
        channel_id: str,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        connection_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        if format is not None:
            _query_params["format"] = format
        if client_id is not None:
            _query_params["clientId"] = client_id
        if connection_id is not None:
            _query_params["connectionId"] = connection_id
        if limit is not None:
            _query_params["limit"] = limit
        if x_ably_version is not None:
            _header_params["X-Ably-Version"] = x_ably_version
        if channel_id is not None:
            _path_params["channel_id"] = channel_id
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aget_presence_of_channel_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get presence of a channel
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_channel_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
            request_query_client_id,
            request_query_connection_id,
            request_query_limit,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/channels/{channel_id}/presence',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_presence_of_channel_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get presence of a channel
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_channel_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
            request_query_client_id,
            request_query_connection_id,
            request_query_limit,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/channels/{channel_id}/presence',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetPresenceOfChannelRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_presence_of_channel(
        self,
        channel_id: str,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        connection_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_presence_of_channel_mapped_args(
            channel_id=channel_id,
            x_ably_version=x_ably_version,
            format=format,
            client_id=client_id,
            connection_id=connection_id,
            limit=limit,
        )
        return await self._aget_presence_of_channel_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get_presence_of_channel(
        self,
        channel_id: str,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        connection_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_presence_of_channel_mapped_args(
            channel_id=channel_id,
            x_ably_version=x_ably_version,
            format=format,
            client_id=client_id,
            connection_id=connection_id,
            limit=limit,
        )
        return self._get_presence_of_channel_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class GetPresenceOfChannel(BaseApi):

    async def aget_presence_of_channel(
        self,
        channel_id: str,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        connection_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> typing.List[PresenceMessage]Pydantic:
        raw_response = await self.raw.aget_presence_of_channel(
            channel_id=channel_id,
            x_ably_version=x_ably_version,
            format=format,
            client_id=client_id,
            connection_id=connection_id,
            limit=limit,
            **kwargs,
        )
        if validate:
            return typing.List[PresenceMessage]Pydantic(**raw_response.body)
        return api_client.construct_model_instance(typing.List[PresenceMessage]Pydantic, raw_response.body)
    
    
    def get_presence_of_channel(
        self,
        channel_id: str,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        connection_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> typing.List[PresenceMessage]Pydantic:
        raw_response = self.raw.get_presence_of_channel(
            channel_id=channel_id,
            x_ably_version=x_ably_version,
            format=format,
            client_id=client_id,
            connection_id=connection_id,
            limit=limit,
        )
        if validate:
            return typing.List[PresenceMessage]Pydantic(**raw_response.body)
        return api_client.construct_model_instance(typing.List[PresenceMessage]Pydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        channel_id: str,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        connection_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_presence_of_channel_mapped_args(
            channel_id=channel_id,
            x_ably_version=x_ably_version,
            format=format,
            client_id=client_id,
            connection_id=connection_id,
            limit=limit,
        )
        return await self._aget_presence_of_channel_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        channel_id: str,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        connection_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_presence_of_channel_mapped_args(
            channel_id=channel_id,
            x_ably_version=x_ably_version,
            format=format,
            client_id=client_id,
            connection_id=connection_id,
            limit=limit,
        )
        return self._get_presence_of_channel_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

