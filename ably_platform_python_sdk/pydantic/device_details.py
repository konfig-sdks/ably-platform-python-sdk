# coding: utf-8

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from ably_platform_python_sdk.pydantic.recipient import Recipient

class DeviceDetails(BaseModel):
    # Optional trusted client identifier for the device.
    client_id: typing.Optional[str] = Field(None, alias='clientId')

    # Secret value for the device.
    device_secret: typing.Optional[str] = Field(None, alias='deviceSecret')

    # Form factor of the push device.
    form_factor: typing.Optional[Literal["phone", "tablet", "desktop", "tv", "watch", "car", "embedded"]] = Field(None, alias='formFactor')

    # Unique identifier for the device generated by the device itself.
    id: typing.Optional[str] = Field(None, alias='id')

    # Optional metadata object for this device. The metadata for a device may only be set by clients with push-admin privileges and will be used more extensively in the future with smart notifications.
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    # Platform of the push device.
    platform: typing.Optional[Literal["ios", "android"]] = Field(None, alias='platform')

    push.recipient_: typing.Optional[Recipient] = Field(None, alias='push.recipient')

    # the current state of the push device.
    push.state_: typing.Optional[Literal["Active", "Failing", "Failed"]] = Field(None, alias='push.state')
    class Config:
        arbitrary_types_allowed = True
