# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ably_platform_python_sdk.paths.push_channel_subscriptions import Api

from ably_platform_python_sdk.paths import PathValues

path = PathValues.PUSH_CHANNEL_SUBSCRIPTIONS