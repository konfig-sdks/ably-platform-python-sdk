# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ably_platform_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CHANNELS = "/channels"
    CHANNELS_CHANNEL_ID = "/channels/{channel_id}"
    CHANNELS_CHANNEL_ID_MESSAGES = "/channels/{channel_id}/messages"
    CHANNELS_CHANNEL_ID_PRESENCE = "/channels/{channel_id}/presence"
    CHANNELS_CHANNEL_ID_PRESENCE_HISTORY = "/channels/{channel_id}/presence/history"
    KEYS_KEY_NAME_REQUEST_TOKEN = "/keys/{keyName}/requestToken"
    PUSH_CHANNEL_SUBSCRIPTIONS = "/push/channelSubscriptions"
    PUSH_CHANNELS = "/push/channels"
    PUSH_DEVICE_REGISTRATIONS = "/push/deviceRegistrations"
    PUSH_DEVICE_REGISTRATIONS_DEVICE_ID = "/push/deviceRegistrations/{device_id}"
    PUSH_DEVICE_REGISTRATIONS_DEVICE_ID_RESET_UPDATE_TOKEN = "/push/deviceRegistrations/{device_id}/resetUpdateToken"
    PUSH_PUBLISH = "/push/publish"
    STATS = "/stats"
    TIME = "/time"
