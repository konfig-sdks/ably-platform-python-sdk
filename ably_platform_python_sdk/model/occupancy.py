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


class Occupancy(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An Occupancy instance indicating the occupancy of a channel. For events indicating regional activity of a channel this indicates activity in that region, not global activity.
    """


    class MetaOapg:
        
        class properties:
            presenceConnections = schemas.IntSchema
            presenceMembers = schemas.IntSchema
            presenceSubscribers = schemas.IntSchema
            publishers = schemas.IntSchema
            subscribers = schemas.IntSchema
            __annotations__ = {
                "presenceConnections": presenceConnections,
                "presenceMembers": presenceMembers,
                "presenceSubscribers": presenceSubscribers,
                "publishers": publishers,
                "subscribers": subscribers,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["presenceConnections"]) -> MetaOapg.properties.presenceConnections: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["presenceMembers"]) -> MetaOapg.properties.presenceMembers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["presenceSubscribers"]) -> MetaOapg.properties.presenceSubscribers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publishers"]) -> MetaOapg.properties.publishers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscribers"]) -> MetaOapg.properties.subscribers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["presenceConnections", "presenceMembers", "presenceSubscribers", "publishers", "subscribers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["presenceConnections"]) -> typing.Union[MetaOapg.properties.presenceConnections, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["presenceMembers"]) -> typing.Union[MetaOapg.properties.presenceMembers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["presenceSubscribers"]) -> typing.Union[MetaOapg.properties.presenceSubscribers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publishers"]) -> typing.Union[MetaOapg.properties.publishers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscribers"]) -> typing.Union[MetaOapg.properties.subscribers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["presenceConnections", "presenceMembers", "presenceSubscribers", "publishers", "subscribers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        presenceConnections: typing.Union[MetaOapg.properties.presenceConnections, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        presenceMembers: typing.Union[MetaOapg.properties.presenceMembers, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        presenceSubscribers: typing.Union[MetaOapg.properties.presenceSubscribers, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        publishers: typing.Union[MetaOapg.properties.publishers, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        subscribers: typing.Union[MetaOapg.properties.subscribers, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Occupancy':
        return super().__new__(
            cls,
            *args,
            presenceConnections=presenceConnections,
            presenceMembers=presenceMembers,
            presenceSubscribers=presenceSubscribers,
            publishers=publishers,
            subscribers=subscribers,
            _configuration=_configuration,
            **kwargs,
        )
