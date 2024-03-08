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

from ably_platform_python_sdk.type.notification import Notification
from ably_platform_python_sdk.type.push_apns import PushApns
from ably_platform_python_sdk.type.push_fcm import PushFcm
from ably_platform_python_sdk.type.push_web import PushWeb

class RequiredPush(TypedDict):
    pass

class OptionalPush(TypedDict, total=False):
    apns: PushApns

    # Arbitrary [key-value string-to-string payload](https://www.ably.io/documentation/general/push/publish#channel-broadcast-example).
    data: str

    fcm: PushFcm

    notification: Notification

    web: PushWeb

class Push(RequiredPush, OptionalPush):
    pass
