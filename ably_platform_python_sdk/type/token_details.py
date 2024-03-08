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


class RequiredTokenDetails(TypedDict):
    pass

class OptionalTokenDetails(TypedDict, total=False):
    # Regular expression representation of the capabilities of the token.
    capability: str

    # Timestamp of token expiration.
    expires: int

    # Timestamp of token creation.
    issued: int

    # Name of the key used to create the token
    keyName: str

    # The Ably Token.
    token: str

class TokenDetails(RequiredTokenDetails, OptionalTokenDetails):
    pass
