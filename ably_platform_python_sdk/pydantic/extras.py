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

from ably_platform_python_sdk.pydantic.push import Push

class Extras(BaseModel):
    push: typing.Optional[Push] = Field(None, alias='push')
    class Config:
        arbitrary_types_allowed = True
