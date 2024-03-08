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
from ably_platform_python_sdk.model.channel_details import ChannelDetails as ChannelDetailsSchema

from ably_platform_python_sdk.type.channel_details import ChannelDetails
from ably_platform_python_sdk.type.error import Error

from ...api_client import Dictionary
from ably_platform_python_sdk.pydantic.error import Error as ErrorPydantic
from ably_platform_python_sdk.pydantic.channel_details import ChannelDetails as ChannelDetailsPydantic

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
LimitSchema = schemas.IntSchema
PrefixSchema = schemas.StrSchema


class BySchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def VALUE(cls):
        return cls("value")
    
    @schemas.classproperty
    def ID(cls):
        return cls("id")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'format': typing.Union[FormatSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'prefix': typing.Union[PrefixSchema, str, ],
        'by': typing.Union[BySchema, str, ],
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
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_prefix = api_client.QueryParameter(
    name="prefix",
    style=api_client.ParameterStyle.FORM,
    schema=PrefixSchema,
    explode=True,
)
request_query_by = api_client.QueryParameter(
    name="by",
    style=api_client.ParameterStyle.FORM,
    schema=BySchema,
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


class LinkSchema(
    schemas.StrSchema
):
    pass


class SchemaFor2XXResponseBodyApplicationJson(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class one_of_0(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                
                @staticmethod
                def items() -> typing.Type['ChannelDetailsSchema']:
                    return ChannelDetailsSchema
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple['ChannelDetails'], typing.List['ChannelDetails']],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> 'ChannelDetails':
                return super().__getitem__(i)
        
        
        class one_of_1(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                items = schemas.StrSchema
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> MetaOapg.items:
                return super().__getitem__(i)
        
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
    ) -> 'SchemaFor2XXResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class SchemaFor2XXResponseBodyApplicationXMsgpack(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class one_of_0(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                
                @staticmethod
                def items() -> typing.Type['ChannelDetailsSchema']:
                    return ChannelDetailsSchema
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple['ChannelDetails'], typing.List['ChannelDetails']],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> 'ChannelDetails':
                return super().__getitem__(i)
        
        
        class one_of_1(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                items = schemas.StrSchema
        
            def __new__(
                cls,
                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                _configuration: typing.Optional[schemas.Configuration] = None,
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    arg,
                    _configuration=_configuration,
                )
        
            def __getitem__(self, i: int) -> MetaOapg.items:
                return super().__getitem__(i)
        
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
    ) -> 'SchemaFor2XXResponseBodyApplicationXMsgpack':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
SchemaFor2XXResponseBodyTextHtml = schemas.StrSchema
ResponseHeadersFor2XX = typing_extensions.TypedDict(
    'ResponseHeadersFor2XX',
    {
        'link': LinkSchema,
    }
)


@dataclass
class ApiResponseFor2XX(api_client.ApiResponse):
    body: typing.Union[typing.List[ChannelDetails], typing.List[str]]


@dataclass
class ApiResponseFor2XXAsync(api_client.AsyncApiResponse):
    body: typing.Union[typing.List[ChannelDetails], typing.List[str]]


_response_for_2XX = api_client.OpenApiResponse(
    response_cls=ApiResponseFor2XX,
    response_cls_async=ApiResponseFor2XXAsync,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor2XXResponseBodyApplicationJson),
        'application/x-msgpack': api_client.MediaType(
            schema=SchemaFor2XXResponseBodyApplicationXMsgpack),
        'text/html': api_client.MediaType(
            schema=SchemaFor2XXResponseBodyTextHtml),
    },
    headers=[
        link_parameter,
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

    def _get_metadata_of_all_channels_mapped_args(
        self,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        prefix: typing.Optional[str] = None,
        by: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if format is not None:
            _query_params["format"] = format
        if limit is not None:
            _query_params["limit"] = limit
        if prefix is not None:
            _query_params["prefix"] = prefix
        if by is not None:
            _query_params["by"] = by
        if x_ably_version is not None:
            _header_params["X-Ably-Version"] = x_ably_version
        args.query = _query_params
        args.header = _header_params
        return args

    async def _aget_metadata_of_all_channels_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor2XXAsync,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Enumerate all active channels of the application
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
            request_query_limit,
            request_query_prefix,
            request_query_by,
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
            path_template='/channels',
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


    def _get_metadata_of_all_channels_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor2XX,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Enumerate all active channels of the application
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
            request_query_limit,
            request_query_prefix,
            request_query_by,
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
            path_template='/channels',
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


class GetMetadataOfAllChannelsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_metadata_of_all_channels(
        self,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        prefix: typing.Optional[str] = None,
        by: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor2XXAsync,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_metadata_of_all_channels_mapped_args(
            x_ably_version=x_ably_version,
            format=format,
            limit=limit,
            prefix=prefix,
            by=by,
        )
        return await self._aget_metadata_of_all_channels_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get_metadata_of_all_channels(
        self,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        prefix: typing.Optional[str] = None,
        by: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor2XX,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_metadata_of_all_channels_mapped_args(
            x_ably_version=x_ably_version,
            format=format,
            limit=limit,
            prefix=prefix,
            by=by,
        )
        return self._get_metadata_of_all_channels_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class GetMetadataOfAllChannels(BaseApi):

    async def aget_metadata_of_all_channels(
        self,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        prefix: typing.Optional[str] = None,
        by: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> typing.Union[typing.List[ChannelDetails], typing.List[str]]:
        raw_response = await self.raw.aget_metadata_of_all_channels(
            x_ably_version=x_ably_version,
            format=format,
            limit=limit,
            prefix=prefix,
            by=by,
            **kwargs,
        )
        if validate:
            return RootModel[typing.Union[typing.List[ChannelDetails], typing.List[str]]](raw_response.body).root
        return raw_response.body
    
    
    def get_metadata_of_all_channels(
        self,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        prefix: typing.Optional[str] = None,
        by: typing.Optional[str] = None,
        validate: bool = False,
    ) -> typing.Union[typing.List[ChannelDetails], typing.List[str]]:
        raw_response = self.raw.get_metadata_of_all_channels(
            x_ably_version=x_ably_version,
            format=format,
            limit=limit,
            prefix=prefix,
            by=by,
        )
        if validate:
            return RootModel[typing.Union[typing.List[ChannelDetails], typing.List[str]]](raw_response.body).root
        return raw_response.body


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        prefix: typing.Optional[str] = None,
        by: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor2XXAsync,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_metadata_of_all_channels_mapped_args(
            x_ably_version=x_ably_version,
            format=format,
            limit=limit,
            prefix=prefix,
            by=by,
        )
        return await self._aget_metadata_of_all_channels_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        x_ably_version: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        prefix: typing.Optional[str] = None,
        by: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor2XX,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_metadata_of_all_channels_mapped_args(
            x_ably_version=x_ably_version,
            format=format,
            limit=limit,
            prefix=prefix,
            by=by,
        )
        return self._get_metadata_of_all_channels_oapg(
            query_params=args.query,
            header_params=args.header,
        )

