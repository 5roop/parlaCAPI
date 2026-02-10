import pytest
import requests

url = "https://parlacap.ipipan.waw.pl/"


def test_no_result_query():
    filter = {
        "filter": {"column": "speaker_name", "operator": "=", "value": "Miška, Miki"},
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    assert response.status_code == 404
    assert (
        response.content
        == b'{"detail":{"code":"NO_RESULTS","message":"No results found","details":null}}'
    )


def test_malformed_filter_query():
    filter = {
        "filter": {"column": "speaker_name", "moperator": "=", "value": "Miška, Miki"},
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    assert response.status_code == 400
    assert (
        response.content
        == b'{"detail":{"code":"INVALID_FILTER","message":"Unknown filter type","details":{"type":"dict"}}}'
    )


def test_illogical_filter_query():
    filter = {
        "operator": "AND",
        "filters": [
            {"column": "parliament", "operator": "=", "value": "SI"},
            {"column": "parliament", "operator": "!=", "value": "SI"},
        ],
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    assert response.status_code == 422
    assert (
        response.content
        == b'{"detail":[{"type":"extra_forbidden","loc":["body","operator"],"msg":"Extra inputs are not permitted","input":"AND"},{"type":"extra_forbidden","loc":["body","filters"],"msg":"Extra inputs are not permitted","input":[{"column":"parliament","operator":"=","value":"SI"},{"column":"parliament","operator":"!=","value":"SI"}]}]}'
    )


def test_filter_with_empty_IN_in_complex_filter_query():
    filter = {
        "filter": {
            "operator": "AND",
            "filters": [
                {"column": "parliament", "value": "SI", "operator": "="},
                {"column": "speaker_party", "value": [], "operator": "IN"},
            ],
        },
        "limit": 1,
        "offset": 10,
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    assert '{"detail":{"code":"INVALID_FILTER"' in response.content.decode("utf8")
    assert '"IN operator requires at least one value"' in response.content.decode(
        "utf8"
    )


def test_filter_with_empty_IN_in_simple_filter_query():
    filter = {
        "filter": {"column": "speaker_party", "value": [], "operator": "IN"},
        "limit": 1,
        "offset": 10,
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    assert '{"detail":{"code":"INVALID_FILTER"' in response.content.decode("utf8")
    assert '"IN operator requires at least one value"' in response.content.decode(
        "utf8"
    )


def test_genders_for_non_MF_values():
    filter = {
        "filter": {
            "operator": "NOT",
            "filters": [
                {"column": "speaker_gender", "operator": "IN", "value": ["M", "F"]}
            ],
        },
        "limit": 200,
        "columns": ["speaker_gender"],
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, content: {response.content}"
        )
    payload = response.json()
    genders = set([i["speaker_gender"] for i in payload])
    assert genders == {None}


def test_genders_for_null_values():
    filter = {
        "filter": {"column": "speaker_gender", "value": None, "operator": "="},
        "limit": 10,
        "columns": ["speaker_gender"],
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, content: {response.content}"
        )
    payload = response.json()
    assert len(payload) == 10
