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


class RequiredError(TypedDict):
    pass

class OptionalError(TypedDict, total=False):
    # Error code.
    code: int

    # Link to help with error.
    href: str

    # Message explaining the error's cause.
    message: str

    # Server ID with which error was encountered.
    serverId: str

    # Status error code.
    statusCode: int

class Error(RequiredError, OptionalError):
    pass
