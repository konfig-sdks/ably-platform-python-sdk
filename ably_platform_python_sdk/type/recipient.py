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


class RequiredRecipient(TypedDict):
    pass

class OptionalRecipient(TypedDict, total=False):
    # Client ID of recipient
    clientId: str

    # Client ID of recipient
    deviceId: str

    # when using APNs, specifies the required device token.
    deviceToken: str

    # when using GCM or FCM, specifies the required registration token.
    registrationToken: str

    # Defines which push platform is being used.
    transportType: str

class Recipient(RequiredRecipient, OptionalRecipient):
    pass
