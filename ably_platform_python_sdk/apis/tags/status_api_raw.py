# coding: utf-8

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

from ably_platform_python_sdk.paths.channels.get import GetMetadataOfAllChannelsRaw
from ably_platform_python_sdk.paths.channels_channel_id.get import GetMetadataOfChannelRaw
from ably_platform_python_sdk.paths.channels_channel_id_presence.get import GetPresenceOfChannelRaw


class StatusApiRaw(
    GetMetadataOfAllChannelsRaw,
    GetMetadataOfChannelRaw,
    GetPresenceOfChannelRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
