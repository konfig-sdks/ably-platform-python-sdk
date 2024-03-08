# coding: utf-8

"""
    Platform API

    The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.

    The version of the OpenAPI document: 1.1.0
    Contact: support@ably.io
    Created by: https://www.ably.io/contact
"""

import unittest

import os
from pprint import pprint
from ably_platform_python_sdk import Ably

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        ably = Ably(
        
            username = 'YOUR_USERNAME',
            password = 'YOUR_PASSWORD',
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(ably)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
