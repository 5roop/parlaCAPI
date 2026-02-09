import pytest


def get_variables():
    import requests

    url = "https://parlacap.ipipan.waw.pl/"
    response = requests.get(url + "variables")
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, content: {response.content}"
        )

    payload = response.json()
    return [i["name"] for i in payload]


@pytest.fixture
def get_sample():
    url = "https://parlacap.ipipan.waw.pl/"

    import requests

    response = requests.get(url + "sample?size=500")
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")

    payload = response.json()
    return payload


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
    unique_parliaments = set([i["parliament"] for i in get_sample])
    # Is there a parliament that is not in ps?
    for u in unique_parliaments:
        assert u in ps


@pytest.mark.parametrize(
    "attr",
    get_variables(),
)
def test_if_all_nulls_in_attr_cap_category(get_sample, attr: str):

    non_nulls = [i for i in get_sample if i[attr] is not None]
    assert len(non_nulls) > 0
