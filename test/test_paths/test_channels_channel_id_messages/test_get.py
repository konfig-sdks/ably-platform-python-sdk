# coding: utf-8

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

import unittest
from unittest.mock import patch

import urllib3

import ably_platform_python_sdk
from ably_platform_python_sdk.paths.channels_channel_id_messages import get
from ably_platform_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestChannelsChannelIdMessages(ApiTestMixin, unittest.TestCase):
    """
    ChannelsChannelIdMessages unit test stubs
        Get message history for a channel
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 2XX








if __name__ == '__main__':
    unittest.main()
