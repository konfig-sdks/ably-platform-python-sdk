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

from ably_platform_python_sdk.pydantic.extras import Extras

class PresenceMessage(BaseModel):
    # The event signified by a PresenceMessage.
    action: typing.Optional[Literal["ABSENT", "PRESENT", "ENTER", "LEAVE", "UPDATE"]] = Field(None, alias='action')

    # The client ID of the publisher of this presence update.
    client_id: typing.Optional[str] = Field(None, alias='clientId')

    # The connection ID of the publisher of this presence update.
    connection_id: typing.Optional[str] = Field(None, alias='connectionId')

    # The presence update payload, if provided.
    data: typing.Optional[str] = Field(None, alias='data')

    # This will typically be empty as all presence updates received from Ably are automatically decoded client-side using this value. However, if the message encoding cannot be processed, this attribute will contain the remaining transformations not applied to the data payload.
    encoding: typing.Optional[str] = Field(None, alias='encoding')

    extras: typing.Optional[Extras] = Field(None, alias='extras')

    # Unique ID assigned by Ably to this presence update.
    id: typing.Optional[str] = Field(None, alias='id')

    # Timestamp when the presence update was received by Ably, as milliseconds since the epoch.
    timestamp: typing.Optional[int] = Field(None, alias='timestamp')
    class Config:
        arbitrary_types_allowed = True
