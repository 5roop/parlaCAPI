url = "https://parlacap.ipipan.waw.pl/"

import requests
import pytest

expected_keys = [
    "id",
    "parlamint_text_id",
    "parlamint_id",
    "date",
    "parliament",
    "vdem_country_id",
    "lang",
    "speaker_role",
    "speaker_mp",
    "speaker_minister",
    "speaker_party",
    "speaker_party_name",
    "party_status",
    "party_orientation",
    "partyfacts_id",
    "speaker_id",
    "speaker_name",
    "speaker_gender",
    "speaker_birth",
    "word_count",
    "cap_category",
    "cap_prob",
    "sent_logit",
    "sent3_category",
    "sent6_category",
    "text",
    "text_en",
]


def test_that_API_returns_anything():
    response = requests.get(url + "sample?size=1")
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")

    payload = response.json()[0]
    assert bool(payload)


@pytest.fixture
def sample():
    response = requests.get(url + "sample?size=1")
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")

    payload = response.json()[0]
    return payload


def test_attribute_names(sample):
    got_keys = list(sample.keys())
    assert got_keys == expected_keys
