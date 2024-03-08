# coding: utf-8

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

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


class TokenDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            capability = schemas.StrSchema
            expires = schemas.IntSchema
            issued = schemas.IntSchema
            keyName = schemas.StrSchema
            token = schemas.StrSchema
            __annotations__ = {
                "capability": capability,
                "expires": expires,
                "issued": issued,
                "keyName": keyName,
                "token": token,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capability"]) -> MetaOapg.properties.capability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires"]) -> MetaOapg.properties.expires: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issued"]) -> MetaOapg.properties.issued: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyName"]) -> MetaOapg.properties.keyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["capability", "expires", "issued", "keyName", "token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capability"]) -> typing.Union[MetaOapg.properties.capability, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires"]) -> typing.Union[MetaOapg.properties.expires, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issued"]) -> typing.Union[MetaOapg.properties.issued, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyName"]) -> typing.Union[MetaOapg.properties.keyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["capability", "expires", "issued", "keyName", "token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        capability: typing.Union[MetaOapg.properties.capability, str, schemas.Unset] = schemas.unset,
        expires: typing.Union[MetaOapg.properties.expires, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        issued: typing.Union[MetaOapg.properties.issued, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        keyName: typing.Union[MetaOapg.properties.keyName, str, schemas.Unset] = schemas.unset,
        token: typing.Union[MetaOapg.properties.token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TokenDetails':
        return super().__new__(
            cls,
            *args,
            capability=capability,
            expires=expires,
            issued=issued,
            keyName=keyName,
            token=token,
            _configuration=_configuration,
            **kwargs,
        )