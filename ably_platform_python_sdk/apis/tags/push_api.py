# coding: utf-8

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

from ably_platform_python_sdk.paths.push_channel_subscriptions.delete import DeletePushDeviceDetails
from ably_platform_python_sdk.paths.push_channels.get import GetChannelsWithPushSubscribers
from ably_platform_python_sdk.paths.push_device_registrations_device_id.get import GetPushDeviceDetails
from ably_platform_python_sdk.paths.push_channel_subscriptions.get import GetPushSubscriptionsOnChannels
from ably_platform_python_sdk.paths.push_device_registrations.get import GetRegisteredPushDevices
from ably_platform_python_sdk.paths.push_device_registrations_device_id.patch import PatchPushDeviceDetails
from ably_platform_python_sdk.paths.push_publish.post import PublishPushNotificationToDevices
from ably_platform_python_sdk.paths.push_device_registrations_device_id.put import PutPushDeviceDetails
from ably_platform_python_sdk.paths.push_device_registrations.post import RegisterPushDevice
from ably_platform_python_sdk.paths.push_channel_subscriptions.post import SubscribePushDeviceToChannel
from ably_platform_python_sdk.paths.push_device_registrations.delete import UnregisterAllPushDevices
from ably_platform_python_sdk.paths.push_device_registrations_device_id.delete import UnregisterPushDevice
from ably_platform_python_sdk.paths.push_device_registrations_device_id_reset_update_token.get import UpdatePushDeviceDetails
from ably_platform_python_sdk.apis.tags.push_api_raw import PushApiRaw


class PushApi(
    DeletePushDeviceDetails,
    GetChannelsWithPushSubscribers,
    GetPushDeviceDetails,
    GetPushSubscriptionsOnChannels,
    GetRegisteredPushDevices,
    PatchPushDeviceDetails,
    PublishPushNotificationToDevices,
    PutPushDeviceDetails,
    RegisterPushDevice,
    SubscribePushDeviceToChannel,
    UnregisterAllPushDevices,
    UnregisterPushDevice,
    UpdatePushDeviceDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PushApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PushApiRaw(api_client)