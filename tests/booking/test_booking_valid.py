from http import HTTPStatus

import requests
from pytest_check import check


def test_bookingids(booking_config, token):
    token = token
    if token is None:
        raise "Błędny token"
    # params firstname lastname checkin checkout
    params = {"checkin": "2024-01-01"}
    response: requests.Response = requests.get(url=booking_config, params=params)
    with check:
        assert response.status_code == HTTPStatus.OK  # enumerator zamiast wpisania 201
    with check:
        assert len(response.json()) > 0
    with check:
        for booking in response.json():
            assert "bookingid" in booking
    with check:
        for booking in response.json():
            #            assert type(booking["bookingid"]) == int
            assert isinstance(booking["bookingid"], int)
    print(response.json()[0])
    print(len(response.json()))
    print(response.json())
