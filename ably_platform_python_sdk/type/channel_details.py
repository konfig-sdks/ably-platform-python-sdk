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

from ably_platform_python_sdk.type.channel_status import ChannelStatus

class RequiredChannelDetails(TypedDict):
    # The required name of the channel including any qualifier, if any.
    channelId: str

class OptionalChannelDetails(TypedDict, total=False):
    # In events relating to the activity of a channel in a specific region, this optionally identifies whether or not that region is responsible for global coordination of the channel.
    isGlobalMaster: bool

    # In events relating to the activity of a channel in a specific region, this optionally identifies the region.
    region: str

    status: ChannelStatus

class ChannelDetails(RequiredChannelDetails, OptionalChannelDetails):
    pass
