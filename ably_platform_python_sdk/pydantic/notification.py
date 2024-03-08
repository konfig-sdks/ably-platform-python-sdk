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


class Notification(BaseModel):
    # Text below title on the expanded notification.
    body: typing.Optional[str] = Field(None, alias='body')

    # Platform-specific, used to group notifications together.
    collapse_key: typing.Optional[str] = Field(None, alias='collapseKey')

    # Platform-specific icon for the notification.
    icon: typing.Optional[str] = Field(None, alias='icon')

    # Platform-specific sound for the notification.
    sound: typing.Optional[str] = Field(None, alias='sound')

    # Title to display at the notification.
    title: typing.Optional[str] = Field(None, alias='title')
    class Config:
        arbitrary_types_allowed = True
