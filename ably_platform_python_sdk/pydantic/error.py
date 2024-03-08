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


class Error(BaseModel):
    # Error code.
    code: typing.Optional[int] = Field(None, alias='code')

    # Link to help with error.
    href: typing.Optional[str] = Field(None, alias='href')

    # Message explaining the error's cause.
    message: typing.Optional[str] = Field(None, alias='message')

    # Server ID with which error was encountered.
    server_id: typing.Optional[str] = Field(None, alias='serverId')

    # Status error code.
    status_code: typing.Optional[int] = Field(None, alias='statusCode')
    class Config:
        arbitrary_types_allowed = True
