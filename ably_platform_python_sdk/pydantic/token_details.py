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


class TokenDetails(BaseModel):
    # Regular expression representation of the capabilities of the token.
    capability: typing.Optional[str] = Field(None, alias='capability')

    # Timestamp of token expiration.
    expires: typing.Optional[int] = Field(None, alias='expires')

    # Timestamp of token creation.
    issued: typing.Optional[int] = Field(None, alias='issued')

    # Name of the key used to create the token
    key_name: typing.Optional[str] = Field(None, alias='keyName')

    # The Ably Token.
    token: typing.Optional[str] = Field(None, alias='token')
    class Config:
        arbitrary_types_allowed = True
