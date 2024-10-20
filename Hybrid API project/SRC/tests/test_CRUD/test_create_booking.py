import allure
import pytest
import logging

from SRC.Constants.api_constants import API_constats
from SRC.utils.utils import Utils
from SRC.Helpers.api_request_wrappers import post_request
from SRC.Helpers.common_verification import *
from SRC.Helpers.payload_manager import payload_create_booking


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Creates a new booking in the API(P)")
    @allure.description("create a booking and verify the status code and booking is not null")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("starting the postive tc 1")
        response = post_request(
            url=API_constats().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_key_is_not_null(response.json()["bookingid"])
        LOGGER.info(response.json()["bookingid"])
        LOGGER.info("ending the positive tc 1")

    @pytest.mark.negative
    @allure.title("Creates a new booking in the API (N)")
    @allure.description("create a booking without payload and verify the status code ")
    def test_create_booking_Negative(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("starting the negative testcase 1")
        response = post_request(
            url=API_constats().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=500)
        LOGGER.info("ending the negative testcase 1")
