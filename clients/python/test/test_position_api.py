# coding: utf-8

"""
    BitMEX API

    REST API for the BitMEX.com trading platform.<br><br><a href=\"/app/restAPI\">REST Documentation</a><br><a href=\"/app/wsAPI\">Websocket Documentation</a>

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.position_api import PositionApi


class TestPositionApi(unittest.TestCase):
    """ PositionApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.position_api.PositionApi()

    def tearDown(self):
        pass

    def test_position_get(self):
        """
        Test case for position_get

        Get your positions.
        """
        pass

    def test_position_isolate_margin(self):
        """
        Test case for position_isolate_margin

        Enable isolated margin or cross margin per-position.
        """
        pass

    def test_position_transfer_isolated_margin(self):
        """
        Test case for position_transfer_isolated_margin

        Transfer equity in or out of a position.
        """
        pass

    def test_position_update_leverage(self):
        """
        Test case for position_update_leverage

        Choose leverage for a position.
        """
        pass


if __name__ == '__main__':
    unittest.main()