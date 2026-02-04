import pytest

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
url = "https://parlacap.ipipan.waw.pl/"

import requests


@pytest.mark.parametrize("p", ps)
def test_filter_endpoint_on_a_parlament(p):
    filter_data = {
        "filter": {"column": "parliament", "value": p, "operator": "="},
        "limit": 10,
        "offset": 0,
    }

    response = requests.post(url + "filter", json=filter_data)
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.content}")

    payload = response.json()
    assert all([i["parliament"] == p for i in payload])


def test_filter_endpoint_with_a_complex_query():
    filter = {
        "filter": {
            "operator": "OR",
            "filters": [
                {
                    "operator": "AND",
                    "filters": [
                        {"column": "date", "operator": ">=", "value": "2015-11-01"},
                        {"column": "speaker_name", "operator": "LIKE", "value": "Duda"},
                    ],
                },
                {"column": "parliament", "operator": "=", "value": "ES"},
                {"column": "parliament", "operator": "=", "value": "PL"},
            ],
        },
        "search": {"query": "panie i panowie", "field": "text"},
        "columns": ["speaker_name", "date", "word_count", "text", "cap_category"],
        "order_by": ["id", "date"],
        "limit": 2,
        "offset": 0,
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, response text: {response.text}"
        )

    payload = response.json()
    assert payload[0]["text"].startswith(
        "Drodzy Rodacy! Panie Marszałku! Szanowni Państwo Marszałkowie poprzedniej i wcześniejszych kadencji Sejmu! Pani Premier! "
    )
    assert payload[1]["text"].startswith(
        "Szanowny Panie Prezydencie! Panie Marszałku! Wysoka Izbo! Zgodnie z art. 162 ust. 1 Konstytucji "
    )


def test_filtering_modes():
    # Test filtering + searching:
    filter = {
        "filter": {
            "operator": "OR",
            "filters": [
                {"column": "parliament", "operator": "=", "value": "SI"},
            ],
        },
        "search": {"query": "zakon", "field": "text"},
        "columns": ["id", "speaker_name", "date", "word_count", "text", "cap_category"],
        "order_by": ["word_count", "id"],
        "limit": 1,
        "offset": 0,
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, response text: {response.text}"
        )

    payload = response.json()[0]
    assert payload["text"] == "Azbestni zakon."
    assert payload["id"] == 6515206

    # Test filtering only on exact match of a text:
    filter = {
        "filter": {
            "operator": "AND",
            "filters": [
                {"column": "text", "operator": "=", "value": "Azbestni zakon."},
                {"column": "parliament", "operator": "=", "value": "SI"},
            ],
        },
        "columns": ["id", "speaker_name", "date", "word_count", "text", "cap_category"],
        "order_by": ["word_count", "id"],
        "limit": 1,
    }
    response = requests.post(
        url + "filter",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, response text: {response.text}"
        )

    payload = response.json()[0]
    assert payload["text"] == "Azbestni zakon."
    assert payload["id"] == 6515206


def test_filter_for_null_values():
    filter = {
        "filter": {"column": "cap_category", "value": None, "operator": "="},
        "limit": 1,
        "offset": 10,
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, response text: {response.text}"
        )

    payload = response.json()
    assert len(payload) == 1


def test_filter_text_starts_with():
    filter = {
        "filter": {
            "operator": "AND",
            "filters": [
                {"column": "parliament", "operator": "=", "value": "SI"},
                {"column": "text", "operator": "STARTS_WITH", "value": "Azbest"},
            ],
        },
        "search": {"query": "zakon", "field": "text"},
        "columns": ["id", "speaker_name", "date", "word_count", "text", "cap_category"],
        "order_by": ["word_count", "id"],
        "limit": 1,
        "offset": 0,
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, response text: {response.text}"
        )

    payload = response.json()[0]
    assert payload["text"] == "Azbestni zakon."
    assert payload["id"] == 6515206


def test_filter_text_contains():
    filter = {
        "filter": {
            "operator": "AND",
            "filters": [
                {"column": "parliament", "operator": "=", "value": "SI"},
                {"column": "text", "operator": "CONTAINS", "value": "Azbestni"},
            ],
        },
        "search": {"query": "zakon", "field": "text"},
        "columns": ["id", "speaker_name", "date", "word_count", "text", "cap_category"],
        "order_by": ["word_count", "id"],
        "limit": 1,
        "offset": 0,
    }

    response = requests.post(
        url + "filter",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, response text: {response.text}"
        )

    payload = response.json()[0]
    assert payload["text"] == "Azbestni zakon."
    assert payload["id"] == 6515206