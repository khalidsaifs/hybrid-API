# all common verifications
# all function which we use in every test
# to verify responses.
# http code
# assert key values
# data verification
# json schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed status code match"


def verify_response_key(key, expected_data):
    assert key == expected_data


def verify_response_key_is_not_null(key):
    assert key != 0, "Failed - key is not empty" + key
    assert key >= 0, "failed- key is greater than zero" + key


def verify_response_key_is_not_null_token(key):
    assert key != 0, "Failed - key is not empty" + key


def verify_response_delete(response):
    assert "Created" in response


# def verify_response_delete(response):
#     # Check if the response is empty or look for another indicator
#     assert response == "" or response is not None, "Delete operation did not return the expected response"
