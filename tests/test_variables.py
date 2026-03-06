url = "https://parlacap.ipipan.waw.pl/api/v1/"

import requests
import pytest
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="my_secrets.env")
headers = {"X-API-Key": os.getenv("parlacapi_key")}


@pytest.mark.parametrize(
    "col",
    [
        "lang",
        "parliament",
        "date",
        "sent3_category",
        "sent6_category",
        "sent_logit",
        "speaker_role",
    ],
)
def test_variables_that_should_never_be_null(col):
    response = requests.get(url + f"variables?column_name={col}", headers=headers)
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")

    payload = response.json()
    assert payload["stats"]["count"] == 7982752
    assert payload["stats"]["null_count"] == 0


@pytest.mark.parametrize(
    "col",
    [
        "id",
        "parlacap_id",
        "parlamint_id",
        "parlamint_text_id",
        "partyfacts_id",
        "text",
        "text_en",
        "vdem_country_id",
    ],
)
def test_variables_that_should_not_have_stats(col):
    response = requests.get(url + f"variables?column_name={col}", headers=headers)
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")

    payload = response.json()
    assert payload["stats"] is None


2 + 2
