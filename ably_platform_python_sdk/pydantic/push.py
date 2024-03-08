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

from ably_platform_python_sdk.pydantic.notification import Notification
from ably_platform_python_sdk.pydantic.push_apns import PushApns
from ably_platform_python_sdk.pydantic.push_fcm import PushFcm
from ably_platform_python_sdk.pydantic.push_web import PushWeb

class Push(BaseModel):
    apns: typing.Optional[PushApns] = Field(None, alias='apns')

    # Arbitrary [key-value string-to-string payload](https://www.ably.io/documentation/general/push/publish#channel-broadcast-example).
    data: typing.Optional[str] = Field(None, alias='data')

    fcm: typing.Optional[PushFcm] = Field(None, alias='fcm')

    notification: typing.Optional[Notification] = Field(None, alias='notification')

    web: typing.Optional[PushWeb] = Field(None, alias='web')
    class Config:
        arbitrary_types_allowed = True
