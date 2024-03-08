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
from ably_platform_python_sdk.paths.push_channel_subscriptions import delete
from ably_platform_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPushChannelSubscriptions(ApiTestMixin, unittest.TestCase):
    """
    PushChannelSubscriptions unit test stubs
        Delete a registered device's update token
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 2XX
    response_body = ''


if __name__ == '__main__':
    unittest.main()
