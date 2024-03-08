from ably_platform_python_sdk.paths.push_channel_subscriptions.get import ApiForget
from ably_platform_python_sdk.paths.push_channel_subscriptions.post import ApiForpost
from ably_platform_python_sdk.paths.push_channel_subscriptions.delete import ApiFordelete


class PushChannelSubscriptions(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
