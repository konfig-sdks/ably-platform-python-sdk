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

from ably_platform_python_sdk.type.recipient import Recipient

RequiredDeviceDetails = TypedDict("RequiredDeviceDetails", {
    })

OptionalDeviceDetails = TypedDict("OptionalDeviceDetails", {
    # Optional trusted client identifier for the device.
    "clientId": str,

    # Secret value for the device.
    "deviceSecret": str,

    # Form factor of the push device.
    "formFactor": str,

    # Unique identifier for the device generated by the device itself.
    "id": str,

    # Optional metadata object for this device. The metadata for a device may only be set by clients with push-admin privileges and will be used more extensively in the future with smart notifications.
    "metadata": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    # Platform of the push device.
    "platform": str,

    "push.recipient": Recipient,

    # the current state of the push device.
    "push.state": str,
    }, total=False)

class DeviceDetails(RequiredDeviceDetails, OptionalDeviceDetails):
    pass
