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


class RequiredTokenRequest(TypedDict):
    # The [capabilities](https://www.ably.io/documentation/core-features/authentication#capabilities-explained) (i.e. a set of channel names/namespaces and, for each, a set of operations) which should be a subset of the set of capabilities associated with the key specified in keyName.
    capability: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Name of the key used for the TokenRequest. The keyName comprises of the app ID and key ID on an API Key.
    keyName: str

    # An unquoted, un-escaped random string of at least 16 characters. Used to ensure the Ably TokenRequest cannot be reused.
    nonce: str

    # Time of creation of the Ably TokenRequest.
    timestamp: int

class OptionalTokenRequest(TypedDict, total=False):
    # The [client ID](https://www.ably.io/documentation/core-features/authentication#identified-clients) to be assosciated with the token. Can be set to * to allow for any client ID to be used.
    clientId: str

class TokenRequest(RequiredTokenRequest, OptionalTokenRequest):
    pass
