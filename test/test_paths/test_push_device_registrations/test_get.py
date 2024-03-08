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
from ably_platform_python_sdk.paths.push_device_registrations import get
from ably_platform_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPushDeviceRegistrations(ApiTestMixin, unittest.TestCase):
    """
    PushDeviceRegistrations unit test stubs
        List devices registered for receiving push notifications
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 2XX








if __name__ == '__main__':
    unittest.main()
