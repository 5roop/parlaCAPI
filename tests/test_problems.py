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
