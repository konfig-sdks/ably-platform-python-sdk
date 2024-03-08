# coding: utf-8

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

from ably_platform_python_sdk.paths.stats.get import GetStats
from ably_platform_python_sdk.paths.time.get import GetTime
from ably_platform_python_sdk.apis.tags.stats_api_raw import StatsApiRaw


class StatsApi(
    GetStats,
    GetTime,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: StatsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = StatsApiRaw(api_client)
