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

class RequiredPushWeb(TypedDict):
    pass

class OptionalPushWeb(TypedDict, total=False):
    notification: Notification

class PushWeb(RequiredPushWeb, OptionalPushWeb):
    pass
