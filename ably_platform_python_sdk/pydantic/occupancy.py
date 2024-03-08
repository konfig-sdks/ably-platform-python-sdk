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


class Occupancy(BaseModel):
    # The number of connections that are authorised to enter members into the presence channel.
    presence_connections: typing.Optional[int] = Field(None, alias='presenceConnections')

    # The number of members currently entered into the presence channel.
    presence_members: typing.Optional[int] = Field(None, alias='presenceMembers')

    # The number of connections that are authorised to subscribe to presence messages.
    presence_subscribers: typing.Optional[int] = Field(None, alias='presenceSubscribers')

    # The number of connections attached to the channel that are authorised to publish.
    publishers: typing.Optional[int] = Field(None, alias='publishers')

    # The number of connections attached that are authorised to subscribe to messages.
    subscribers: typing.Optional[int] = Field(None, alias='subscribers')
    class Config:
        arbitrary_types_allowed = True
