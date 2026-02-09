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


@pytest.mark.parametrize(
    "attr",
    get_variables(),
)
def test_if_all_nulls_in_attr_cap_category(get_sample, attr: str):

    non_nulls = [i for i in get_sample if i[attr] is not None]
    assert len(non_nulls) > 0
