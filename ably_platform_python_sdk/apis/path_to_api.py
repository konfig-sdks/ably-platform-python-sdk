import typing_extensions

from ably_platform_python_sdk.paths import PathValues
from ably_platform_python_sdk.apis.paths.channels import Channels
from ably_platform_python_sdk.apis.paths.channels_channel_id import ChannelsChannelId
from ably_platform_python_sdk.apis.paths.channels_channel_id_messages import ChannelsChannelIdMessages
from ably_platform_python_sdk.apis.paths.channels_channel_id_presence import ChannelsChannelIdPresence
from ably_platform_python_sdk.apis.paths.channels_channel_id_presence_history import ChannelsChannelIdPresenceHistory
from ably_platform_python_sdk.apis.paths.keys_key_name_request_token import KeysKeyNameRequestToken
from ably_platform_python_sdk.apis.paths.push_channel_subscriptions import PushChannelSubscriptions
from ably_platform_python_sdk.apis.paths.push_channels import PushChannels
from ably_platform_python_sdk.apis.paths.push_device_registrations import PushDeviceRegistrations
from ably_platform_python_sdk.apis.paths.push_device_registrations_device_id import PushDeviceRegistrationsDeviceId
from ably_platform_python_sdk.apis.paths.push_device_registrations_device_id_reset_update_token import PushDeviceRegistrationsDeviceIdResetUpdateToken
from ably_platform_python_sdk.apis.paths.push_publish import PushPublish
from ably_platform_python_sdk.apis.paths.stats import Stats
from ably_platform_python_sdk.apis.paths.time import Time

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CHANNELS: Channels,
        PathValues.CHANNELS_CHANNEL_ID: ChannelsChannelId,
        PathValues.CHANNELS_CHANNEL_ID_MESSAGES: ChannelsChannelIdMessages,
        PathValues.CHANNELS_CHANNEL_ID_PRESENCE: ChannelsChannelIdPresence,
        PathValues.CHANNELS_CHANNEL_ID_PRESENCE_HISTORY: ChannelsChannelIdPresenceHistory,
        PathValues.KEYS_KEY_NAME_REQUEST_TOKEN: KeysKeyNameRequestToken,
        PathValues.PUSH_CHANNEL_SUBSCRIPTIONS: PushChannelSubscriptions,
        PathValues.PUSH_CHANNELS: PushChannels,
        PathValues.PUSH_DEVICE_REGISTRATIONS: PushDeviceRegistrations,
        PathValues.PUSH_DEVICE_REGISTRATIONS_DEVICE_ID: PushDeviceRegistrationsDeviceId,
        PathValues.PUSH_DEVICE_REGISTRATIONS_DEVICE_ID_RESET_UPDATE_TOKEN: PushDeviceRegistrationsDeviceIdResetUpdateToken,
        PathValues.PUSH_PUBLISH: PushPublish,
        PathValues.STATS: Stats,
        PathValues.TIME: Time,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CHANNELS: Channels,
        PathValues.CHANNELS_CHANNEL_ID: ChannelsChannelId,
        PathValues.CHANNELS_CHANNEL_ID_MESSAGES: ChannelsChannelIdMessages,
        PathValues.CHANNELS_CHANNEL_ID_PRESENCE: ChannelsChannelIdPresence,
        PathValues.CHANNELS_CHANNEL_ID_PRESENCE_HISTORY: ChannelsChannelIdPresenceHistory,
        PathValues.KEYS_KEY_NAME_REQUEST_TOKEN: KeysKeyNameRequestToken,
        PathValues.PUSH_CHANNEL_SUBSCRIPTIONS: PushChannelSubscriptions,
        PathValues.PUSH_CHANNELS: PushChannels,
        PathValues.PUSH_DEVICE_REGISTRATIONS: PushDeviceRegistrations,
        PathValues.PUSH_DEVICE_REGISTRATIONS_DEVICE_ID: PushDeviceRegistrationsDeviceId,
        PathValues.PUSH_DEVICE_REGISTRATIONS_DEVICE_ID_RESET_UPDATE_TOKEN: PushDeviceRegistrationsDeviceIdResetUpdateToken,
        PathValues.PUSH_PUBLISH: PushPublish,
        PathValues.STATS: Stats,
        PathValues.TIME: Time,
    }
)
