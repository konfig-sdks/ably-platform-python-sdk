import typing_extensions

from ably_platform_python_sdk.apis.tags import TagValues
from ably_platform_python_sdk.apis.tags.authentication_api import AuthenticationApi
from ably_platform_python_sdk.apis.tags.history_api import HistoryApi
from ably_platform_python_sdk.apis.tags.publishing_api import PublishingApi
from ably_platform_python_sdk.apis.tags.push_api import PushApi
from ably_platform_python_sdk.apis.tags.stats_api import StatsApi
from ably_platform_python_sdk.apis.tags.status_api import StatusApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.PUBLISHING: PublishingApi,
        TagValues.PUSH: PushApi,
        TagValues.STATS: StatsApi,
        TagValues.STATUS: StatusApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.PUBLISHING: PublishingApi,
        TagValues.PUSH: PushApi,
        TagValues.STATS: StatsApi,
        TagValues.STATUS: StatusApi,
    }
)
