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
from pydantic import BaseModel, Field, RootModel


class Recipient(BaseModel):
    # Client ID of recipient
    client_id: typing.Optional[str] = Field(None, alias='clientId')

    # Client ID of recipient
    device_id: typing.Optional[str] = Field(None, alias='deviceId')

    # when using APNs, specifies the required device token.
    device_token: typing.Optional[str] = Field(None, alias='deviceToken')

    # when using GCM or FCM, specifies the required registration token.
    registration_token: typing.Optional[str] = Field(None, alias='registrationToken')

    # Defines which push platform is being used.
    transport_type: typing.Optional[Literal["apns", "fcm", "gcm"]] = Field(None, alias='transportType')
    class Config:
        arbitrary_types_allowed = True
