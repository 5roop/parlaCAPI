import pytest
import polars as pl


@pytest.fixture
def get_sample():
    url = "https://parlacap.ipipan.waw.pl/"

    import requests

    response = requests.get(url + "sample?size=500")
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")

    payload = response.json()
    return pl.DataFrame(payload)


ps = [
    "AT",
    "BA",
    "BE",
    "BG",
    "CZ",
    "DK",
    "EE",
    "ES",
    "ES-CT",
    "ES-GA",
    "ES-PV",
    "FR",
    "GB",
    "GR",
    "HR",
    "HU",
    "IS",
    "IT",
    "LV",
    "NL",
    "NO",
    "PL",
    "PT",
    "RS",
    "SE",
    "SI",
    "TR",
    "UA",
]


def test_valid_parliaments(get_sample):
    df = get_sample
    unique_parliaments = df["parliament"].unique().sort().to_list()
    # Is there a parliament that is not in ps?
    for u in unique_parliaments:
        assert u in ps


def test_if_all_nulls_in_cap_category(get_sample):
    df = get_sample
    non_nulls = df["cap_category"].drop_nulls().shape[0]
    assert non_nulls > 0


def test_if_all_nulls_in_cap_prob(get_sample):
    df = get_sample
    non_nulls = df["cap_prob"].drop_nulls().shape[0]
    assert non_nulls > 0


def test_if_all_nulls_in_parlamint_text_id(get_sample):
    df = get_sample
    non_nulls = df["parlamint_text_id"].drop_nulls().shape[0]
    assert non_nulls > 0


def test_if_all_nulls_in_parlamint_id(get_sample):
    df = get_sample
    non_nulls = df["parlamint_id"].drop_nulls().shape[0]
    assert non_nulls > 0


def test_if_all_nulls_in_speaker_id(get_sample):
    df = get_sample
    non_nulls = df["speaker_id"].drop_nulls().shape[0]
    assert non_nulls > 0


def test_if_all_nulls_in_speaker_name(get_sample):
    df = get_sample
    non_nulls = df["speaker_name"].drop_nulls().shape[0]
    assert non_nulls > 0


def test_if_all_nulls_in_text(get_sample):
    df = get_sample
    non_nulls = df["text"].drop_nulls().shape[0]
    assert non_nulls > 0


def test_if_all_nulls_in_text_en(get_sample):
    df = get_sample
    non_nulls = df["text_en"].drop_nulls().shape[0]
    assert non_nulls > 0
