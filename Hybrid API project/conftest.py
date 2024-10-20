# we will be adding fixtures of create token and booking id.
import allure
import pytest
import logging

from SRC.Constants.api_constants import *
from SRC.utils.utils import *
from SRC.Helpers.api_request_wrappers import *
from SRC.Helpers.common_verification import *
from SRC.Helpers.payload_manager import *


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=API_constats().url_create_booking(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_response_key_is_not_null(booking_id)
    return booking_id


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=API_constats().url_create_token(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_token(),
        in_json=False
    )
    ticket = response.json()["token"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_response_key_is_not_null_token(ticket)
    return ticket
