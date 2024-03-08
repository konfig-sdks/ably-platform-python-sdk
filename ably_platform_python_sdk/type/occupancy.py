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


class RequiredOccupancy(TypedDict):
    pass

class OptionalOccupancy(TypedDict, total=False):
    # The number of connections that are authorised to enter members into the presence channel.
    presenceConnections: int

    # The number of members currently entered into the presence channel.
    presenceMembers: int

    # The number of connections that are authorised to subscribe to presence messages.
    presenceSubscribers: int

    # The number of connections attached to the channel that are authorised to publish.
    publishers: int

    # The number of connections attached that are authorised to subscribe to messages.
    subscribers: int

class Occupancy(RequiredOccupancy, OptionalOccupancy):
    pass
