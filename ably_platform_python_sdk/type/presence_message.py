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

class RequiredPresenceMessage(TypedDict):
    pass

class OptionalPresenceMessage(TypedDict, total=False):
    # The event signified by a PresenceMessage.
    action: str

    # The client ID of the publisher of this presence update.
    clientId: str

    # The connection ID of the publisher of this presence update.
    connectionId: str

    # The presence update payload, if provided.
    data: str

    # This will typically be empty as all presence updates received from Ably are automatically decoded client-side using this value. However, if the message encoding cannot be processed, this attribute will contain the remaining transformations not applied to the data payload.
    encoding: str

    extras: Extras

    # Unique ID assigned by Ably to this presence update.
    id: str

    # Timestamp when the presence update was received by Ably, as milliseconds since the epoch.
    timestamp: int

class PresenceMessage(RequiredPresenceMessage, OptionalPresenceMessage):
    pass
