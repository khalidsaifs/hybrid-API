# update the booking(Put) -booking_id, token
# delete booking

import allure
import pytest

from SRC.Constants.api_constants import API_constats
from SRC.utils.utils import Utils
from SRC.Helpers.api_request_wrappers import *
from SRC.Helpers.common_verification import *
from SRC.Helpers.payload_manager import *


class TestCRUDbooking(object):
    @pytest.mark.put
    @pytest.mark.positive
    @allure.title("API integration testing")
    @allure.description("updating the booking id")
    def test_updating_booking_id(self, create_token, get_booking_id):
        api_constants = API_constats()
        put_url = api_constants.url_put_patch_delete(booking_id=get_booking_id)
        print(put_url)
        response = put_request(
            url=put_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(token=create_token),
            payload=payload_update_booking(),
            in_json=False)

        verify_response_key(response.json()["firstname"], expected_data="Md")
        verify_response_key(response.json()["lastname"], expected_data="Kd")
        verify_http_status_code(response_data=response, expected_data=200)

    @pytest.mark.put
    @pytest.mark.negative
    @allure.title("API integration testing")
    @allure.description("updating the booking id with wrong firstnaem and lastname")
    def test_updating_booking_id_tc(self, create_token, get_booking_id):
        api_constants = API_constats()
        put_url = api_constants.url_put_patch_delete(booking_id=get_booking_id)
        print(put_url)
        response = put_request(
            url=put_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(token=create_token),
            payload=payload_update_booking(),
            in_json=False)

        verify_response_key(response.json()["firstname"], expected_data="M0d")
        verify_response_key(response.json()["lastname"], expected_data="K0d")
        verify_http_status_code(response_data=response, expected_data=200)

    @pytest.mark.delete
    @pytest.mark.positive
    @allure.title("API integration testing")
    @allure.description("deleting the booking id")
    def test_delete_booking_id(self, create_token, get_booking_id):
        api_constants = API_constats()  # instantiate the class
        delete_url = api_constants.url_put_patch_delete(booking_id=get_booking_id)  # call the method on the instance

        print(delete_url)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(token=create_token),
            in_json=False)

        #
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expected_data=201)

    @pytest.mark.delete
    @pytest.mark.negative
    @allure.title("API integration testing")
    @allure.description("deleting the booking id without creat_token")
    def test_delete_booking_id_tc(self, create_token, get_booking_id):
        api_constants = API_constats()  # instantiate the class
        delete_url = api_constants.url_put_patch_delete(booking_id=get_booking_id)  # call the method on the instance

        print(delete_url)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(),
            in_json=False)

        #
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expected_data=201)

    @pytest.mark.delete
    @pytest.mark.negative
    @allure.title("API integration testing")
    @allure.description("deleting the booking id without booking_id")
    def test_delete_booking_id_tc1(self, create_token, get_booking_id):
        api_constants = API_constats()  # instantiate the class
        delete_url = api_constants.url_put_patch_delete()  # call the method on the instance

        print(delete_url)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().common_headers_put_patch_delete_cookie(token=create_token),
            in_json=False)

        #
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expected_data=201)

