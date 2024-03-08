# coding: utf-8

# flake8: noqa

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

__version__ = "1.1.0"

# import ApiClient
from ably_platform_python_sdk.api_client import ApiClient

# import Configuration
from ably_platform_python_sdk.configuration import Configuration

# import exceptions
from ably_platform_python_sdk.exceptions import OpenApiException
from ably_platform_python_sdk.exceptions import ApiAttributeError
from ably_platform_python_sdk.exceptions import ApiTypeError
from ably_platform_python_sdk.exceptions import ApiValueError
from ably_platform_python_sdk.exceptions import ApiKeyError
from ably_platform_python_sdk.exceptions import ApiException

from ably_platform_python_sdk.client import Ably
