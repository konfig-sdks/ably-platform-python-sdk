# coding: utf-8
"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

import typing
import inspect
from datetime import date, datetime
from ably_platform_python_sdk.client_custom import ClientCustom
from ably_platform_python_sdk.configuration import Configuration
from ably_platform_python_sdk.api_client import ApiClient
from ably_platform_python_sdk.type_util import copy_signature
from ably_platform_python_sdk.apis.tags.authentication_api import AuthenticationApi
from ably_platform_python_sdk.apis.tags.history_api import HistoryApi
from ably_platform_python_sdk.apis.tags.publishing_api import PublishingApi
from ably_platform_python_sdk.apis.tags.push_api import PushApi
from ably_platform_python_sdk.apis.tags.stats_api import StatsApi
from ably_platform_python_sdk.apis.tags.status_api import StatusApi



class Ably(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.authentication: AuthenticationApi = AuthenticationApi(api_client)
        self.history: HistoryApi = HistoryApi(api_client)
        self.publishing: PublishingApi = PublishingApi(api_client)
        self.push: PushApi = PushApi(api_client)
        self.stats: StatsApi = StatsApi(api_client)
        self.status: StatusApi = StatusApi(api_client)
