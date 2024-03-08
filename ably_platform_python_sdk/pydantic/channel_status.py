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

from ably_platform_python_sdk.pydantic.occupancy import Occupancy

class ChannelStatus(BaseModel):
    # A required boolean value indicating whether the channel that is the subject of the event is active. For events indicating regional activity of a channel this indicates activity in that region, not global activity.
    is_active: bool = Field(alias='isActive')

    occupancy: typing.Optional[Occupancy] = Field(None, alias='occupancy')
    class Config:
        arbitrary_types_allowed = True
