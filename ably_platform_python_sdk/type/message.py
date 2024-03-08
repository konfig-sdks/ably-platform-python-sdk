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

from ably_platform_python_sdk.type.extras import Extras

class RequiredMessage(TypedDict):
    pass

class OptionalMessage(TypedDict, total=False):
    # The [client ID](https://www.ably.io/documentation/core-features/authentication#identified-clients) of the publisher of this message.
    clientId: str

    # The connection ID of the publisher of this message.
    connectionId: str

    # The string encoded payload, with the encoding specified below.
    data: str

    # This will typically be empty as all messages received from Ably are automatically decoded client-side using this value. However, if the message encoding cannot be processed, this attribute will contain the remaining transformations not applied to the data payload.
    encoding: str

    extras: Extras

    # A Unique ID that can be specified by the publisher for [idempotent publishing](https://www.ably.io/documentation/rest/messages#idempotent).
    id: str

    # The event name, if provided.
    name: str

    # Timestamp when the message was received by the Ably, as milliseconds since the epoch.
    timestamp: int

class Message(RequiredMessage, OptionalMessage):
    pass
