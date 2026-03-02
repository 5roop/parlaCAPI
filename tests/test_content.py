import requests
import pytest
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="my_secrets.env")
headers={"X-API-Key": os.getenv("parlacapi_key")}
url = "https://parlacap.ipipan.waw.pl/api/v1/"

def get_variables():
    response = requests.get(url + "variables", headers = headers)
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, content: {response.content}"
        )

    payload = response.json()
    return [i["name"] for i in payload]


@pytest.fixture(scope="package")
def get_sample():
    response = requests.get(url + "sample?size=500", headers = headers)
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")

    payload = response.json()
    return payload


@pytest.mark.parametrize(
    "attr",
    get_variables(),
)
def test_if_all_nulls_in_attr_cap_category(get_sample, attr: str):

    non_nulls = [i for i in get_sample if i[attr] is not None]
    assert len(non_nulls) > 0
