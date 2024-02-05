import pytest
import requests


def test_positive(url, status_code):
    assert requests.get(url).status_code == status_code


@pytest.mark.parametrize("id", ["sfhfh"])
def test_negative(url, status_code_error, id):
    response = requests.get(f"{url}/{id}")
    assert response.status_code == status_code_error
