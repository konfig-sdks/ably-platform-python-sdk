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

from ably_platform_python_sdk.pydantic.channel_status import ChannelStatus

class ChannelDetails(BaseModel):
    # The required name of the channel including any qualifier, if any.
    channel_id: str = Field(alias='channelId')

    # In events relating to the activity of a channel in a specific region, this optionally identifies whether or not that region is responsible for global coordination of the channel.
    is_global_master: typing.Optional[bool] = Field(None, alias='isGlobalMaster')

    # In events relating to the activity of a channel in a specific region, this optionally identifies the region.
    region: typing.Optional[str] = Field(None, alias='region')

    status: typing.Optional[ChannelStatus] = Field(None, alias='status')
    class Config:
        arbitrary_types_allowed = True
