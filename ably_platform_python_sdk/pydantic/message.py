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

class Message(BaseModel):
    # The [client ID](https://www.ably.io/documentation/core-features/authentication#identified-clients) of the publisher of this message.
    client_id: typing.Optional[str] = Field(None, alias='clientId')

    # The connection ID of the publisher of this message.
    connection_id: typing.Optional[str] = Field(None, alias='connectionId')

    # The string encoded payload, with the encoding specified below.
    data: typing.Optional[str] = Field(None, alias='data')

    # This will typically be empty as all messages received from Ably are automatically decoded client-side using this value. However, if the message encoding cannot be processed, this attribute will contain the remaining transformations not applied to the data payload.
    encoding: typing.Optional[str] = Field(None, alias='encoding')

    extras: typing.Optional[Extras] = Field(None, alias='extras')

    # A Unique ID that can be specified by the publisher for [idempotent publishing](https://www.ably.io/documentation/rest/messages#idempotent).
    id: typing.Optional[str] = Field(None, alias='id')

    # The event name, if provided.
    name: typing.Optional[str] = Field(None, alias='name')

    # Timestamp when the message was received by the Ably, as milliseconds since the epoch.
    timestamp: typing.Optional[int] = Field(None, alias='timestamp')
    class Config:
        arbitrary_types_allowed = True
