url = "https://parlacap.ipipan.waw.pl/api/v1/"

import requests
import pytest
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="my_secrets.env")
headers = {"X-API-Key": os.getenv("parlacapi_key")}


@pytest.fixture(scope="package")
def sample():
    response = requests.get(url + "sample?size=100", headers=headers)
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")

    payload = response.json()
    return payload


@pytest.fixture(scope="package")
def variables():
    response = requests.get(url + "variables", headers=headers)
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")
    payload = response.json()
    return payload


def test_that_API_returns_anything(sample):
    assert bool(sample)


def test_variables_dtypes(sample, variables):

    declared_dtypes = {i["name"]: i["type"] for i in variables}

    for name, dtype in declared_dtypes.items():
        pythontype = {"INTEGER": int, "REAL": float, "TEXT": str}.get(dtype)
        for i in sample:
            if i[name] is None:
                continue
            assert isinstance(i[name], pythontype)


def test_variables():
    response = requests.get(url + "variables", headers=headers)
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")
    payload = response.json()
    assert payload == [
        {
            "description": "Predicted CAP category.",
            "name": "cap_category",
            "stats": {
                "count": 7982341,
                "freq": 3921514,
                "null_count": 411,
                "top": "Other",
                "top10": [
                    {
                        "freq": 3921514,
                        "value": "Other",
                    },
                    {
                        "freq": 417071,
                        "value": "Mix",
                    },
                    {
                        "freq": 397359,
                        "value": "Macroeconomics",
                    },
                    {
                        "freq": 340523,
                        "value": "Government Operations",
                    },
                    {
                        "freq": 326293,
                        "value": "Law and Crime",
                    },
                    {
                        "freq": 316597,
                        "value": "Health",
                    },
                    {
                        "freq": 259153,
                        "value": "International Affairs",
                    },
                    {
                        "freq": 228896,
                        "value": "Civil Rights",
                    },
                    {
                        "freq": 201170,
                        "value": "Education",
                    },
                    {
                        "freq": 172098,
                        "value": "Labor",
                    },
                ],
                "unique_count": 23,
            },
            "type": "TEXT",
        },
        {
            "description": "CAP category prediction probability.",
            "name": "cap_prob",
            "stats": {
                "count": 7982341,
                "max": 0.998,
                "mean": 0.936103,
                "median": 0.993,
                "min": 0.069,
                "null_count": 411,
                "stddev": 0.131348,
                "unique_count": 880,
            },
            "type": "REAL",
        },
        {
            "description": "Date of the session.",
            "name": "date",
            "stats": {
                "count": 7982752,
                "freq": 11668,
                "null_count": 0,
                "top": "2016-11-23",
                "top10": [
                    {
                        "freq": 11668,
                        "value": "2016-11-23",
                    },
                    {
                        "freq": 10302,
                        "value": "2017-12-13",
                    },
                    {
                        "freq": 9766,
                        "value": "2016-12-14",
                    },
                    {
                        "freq": 9511,
                        "value": "2020-12-10",
                    },
                    {
                        "freq": 9188,
                        "value": "2018-12-20",
                    },
                    {
                        "freq": 9172,
                        "value": "2015-12-17",
                    },
                    {
                        "freq": 9027,
                        "value": "2017-11-23",
                    },
                    {
                        "freq": 9019,
                        "value": "2017-11-22",
                    },
                    {
                        "freq": 8962,
                        "value": "2017-12-20",
                    },
                    {
                        "freq": 8779,
                        "value": "2020-12-15",
                    },
                ],
                "unique_count": 5723,
            },
            "type": "TEXT",
        },
        {
            "description": "Primary key",
            "name": "id",
            "stats": None,
            "type": "INTEGER",
        },
        {
            "description": "Language of the transcript",
            "name": "lang",
            "stats": {
                "count": 7982752,
                "freq": 795637,
                "null_count": 0,
                "top": "French",
                "top10": [
                    {
                        "freq": 795637,
                        "value": "French",
                    },
                    {
                        "freq": 739744,
                        "value": "Turkish",
                    },
                    {
                        "freq": 699925,
                        "value": "Dutch",
                    },
                    {
                        "freq": 671038,
                        "value": "English",
                    },
                    {
                        "freq": 504334,
                        "value": "Croatian",
                    },
                    {
                        "freq": 402731,
                        "value": "Ukrainian",
                    },
                    {
                        "freq": 398610,
                        "value": "Danish",
                    },
                    {
                        "freq": 342274,
                        "value": "Greek",
                    },
                    {
                        "freq": 334636,
                        "value": "Norwegian bokmål",
                    },
                    {
                        "freq": 316069,
                        "value": "Serbian",
                    },
                ],
                "unique_count": 30,
            },
            "type": "TEXT",
        },
        {
            "description": "Original document ID from ParlaCap",
            "name": "parlacap_id",
            "stats": None,
            "type": "TEXT",
        },
        {
            "description": "Original speech ID from ParlaMint.",
            "name": "parlamint_id",
            "stats": None,
            "type": "TEXT",
        },
        {
            "description": "Original document ID from ParlaMint.",
            "name": "parlamint_text_id",
            "stats": None,
            "type": "TEXT",
        },
        {
            "description": "Parliament code (e.g. BA, ES-GA, ...)",
            "name": "parliament",
            "stats": {
                "count": 7982752,
                "freq": 739744,
                "null_count": 0,
                "top": "TR",
                "top10": [
                    {
                        "freq": 739744,
                        "value": "TR",
                    },
                    {
                        "freq": 714439,
                        "value": "FR",
                    },
                    {
                        "freq": 670912,
                        "value": "GB",
                    },
                    {
                        "freq": 609209,
                        "value": "NL",
                    },
                    {
                        "freq": 504334,
                        "value": "HR",
                    },
                    {
                        "freq": 429156,
                        "value": "UA",
                    },
                    {
                        "freq": 398809,
                        "value": "NO",
                    },
                    {
                        "freq": 398610,
                        "value": "DK",
                    },
                    {
                        "freq": 342274,
                        "value": "GR",
                    },
                    {
                        "freq": 316069,
                        "value": "RS",
                    },
                ],
                "unique_count": 28,
            },
            "type": "TEXT",
        },
        {
            "description": "Political orientation (e.g., left, right).",
            "name": "party_orientation",
            "stats": {
                "count": 6582010,
                "freq": 1750355,
                "null_count": 1400742,
                "top": "Centre-right",
                "top10": [
                    {
                        "freq": 1750355,
                        "value": "Centre-right",
                    },
                    {
                        "freq": 1375925,
                        "value": "Centre-left",
                    },
                    {
                        "freq": 609294,
                        "value": "Centre",
                    },
                    {
                        "freq": 470346,
                        "value": "Right",
                    },
                    {
                        "freq": 407410,
                        "value": "Centre-right to right",
                    },
                    {
                        "freq": 331286,
                        "value": "Centre to centre-right",
                    },
                    {
                        "freq": 311292,
                        "value": "Centre-left to left",
                    },
                    {
                        "freq": 290246,
                        "value": "Right to far-right",
                    },
                    {
                        "freq": 271278,
                        "value": "Centre to centre-left",
                    },
                    {
                        "freq": 207241,
                        "value": "Left",
                    },
                ],
                "unique_count": 44,
            },
            "type": "TEXT",
        },
        {
            "description": "Government or opposition or coalition.",
            "name": "party_status",
            "stats": {
                "count": 5666374,
                "freq": 3095316,
                "null_count": 2316378,
                "top": "Coalition",
                "top10": [
                    {
                        "freq": 3095316,
                        "value": "Coalition",
                    },
                    {
                        "freq": 2571058,
                        "value": "Opposition",
                    },
                ],
                "unique_count": 2,
            },
            "type": "TEXT",
        },
        {
            "description": "Party ID in the Party Facts database",
            "name": "partyfacts_id",
            "stats": None,
            "type": "INTEGER",
        },
        {
            "description": "Sentiment estimation as a 3-category label (Negative, Neutral, "
            "Positive).",
            "name": "sent3_category",
            "stats": {
                "count": 7982752,
                "freq": 4670289,
                "null_count": 0,
                "top": "Neutral",
                "top10": [
                    {
                        "freq": 4670289,
                        "value": "Neutral",
                    },
                    {
                        "freq": 1724121,
                        "value": "Negative",
                    },
                    {
                        "freq": 1588342,
                        "value": "Positive",
                    },
                ],
                "unique_count": 3,
            },
            "type": "TEXT",
        },
        {
            "description": "Sentiment estimation as a 6-category label (Negative, Mixed Negative, "
            "Neutral Negative, Neutral Positive, Mixed Positive, Positive).",
            "name": "sent6_category",
            "stats": {
                "count": 7982752,
                "freq": 2889729,
                "null_count": 0,
                "top": "Neutral Positive",
                "top10": [
                    {
                        "freq": 2889729,
                        "value": "Neutral Positive",
                    },
                    {
                        "freq": 1780560,
                        "value": "Neutral Negative",
                    },
                    {
                        "freq": 1377031,
                        "value": "Mixed Positive",
                    },
                    {
                        "freq": 1250959,
                        "value": "Mixed Negative",
                    },
                    {
                        "freq": 473162,
                        "value": "Negative",
                    },
                    {
                        "freq": 211311,
                        "value": "Positive",
                    },
                ],
                "unique_count": 6,
            },
            "type": "TEXT",
        },
        {
            "description": "Sentiment estimation as a floating point value, on a scale of 0 to 6, "
            "with 0 being negative. Sentiment is calculated as a length-weighed "
            "average of sentiments of sentences in the speech.",
            "name": "sent_logit",
            "stats": {
                "count": 7982752,
                "max": 5.797,
                "mean": 2.515722,
                "median": 2.705,
                "min": -9.522,
                "null_count": 0,
                "stddev": 1.138799,
                "unique_count": 5876,
            },
            "type": "REAL",
        },
        {
            "description": "Birth year of the speaker.",
            "name": "speaker_birth",
            "stats": {
                "count": 6578947,
                "max": 2002,
                "mean": 1963.525527,
                "median": 1963,
                "min": 1905,
                "null_count": 1403805,
                "stddev": 11.624132,
                "unique_count": 85,
            },
            "type": "INTEGER",
        },
        {
            "description": "Gender of the speaker (M or F).",
            "name": "speaker_gender",
            "stats": {
                "count": 7905874,
                "freq": 5691694,
                "null_count": 76878,
                "top": "M",
                "top10": [
                    {
                        "freq": 5691694,
                        "value": "M",
                    },
                    {
                        "freq": 2214180,
                        "value": "F",
                    },
                ],
                "unique_count": 2,
            },
            "type": "TEXT",
        },
        {
            "description": 'Unique speaker identifier, usually in format "LastnameFirstName".',
            "name": "speaker_id",
            "stats": {
                "count": 7916628,
                "freq": 105909,
                "null_count": 66124,
                "top": "KhadijaArib",
                "top10": [
                    {
                        "freq": 105909,
                        "value": "KhadijaArib",
                    },
                    {
                        "freq": 64370,
                        "value": "MūrnieceInāra",
                    },
                    {
                        "freq": 50380,
                        "value": "ВолодимирМихайловичЛитвин.1956",
                    },
                    {
                        "freq": 42021,
                        "value": "ReinerŽeljko",
                    },
                    {
                        "freq": 41162,
                        "value": "PA721824",
                    },
                    {
                        "freq": 40837,
                        "value": "PA1874",
                    },
                    {
                        "freq": 38904,
                        "value": "KristensenHenrikDam",
                    },
                    {
                        "freq": 38342,
                        "value": "KjærsgaardPia",
                    },
                    {
                        "freq": 37467,
                        "value": "ŠeksVladimir",
                    },
                    {
                        "freq": 35279,
                        "value": "PA720746",
                    },
                ],
                "unique_count": 22510,
            },
            "type": "TEXT",
        },
        {
            "description": "Whether speaker is a minister.",
            "name": "speaker_minister",
            "stats": {
                "count": 7916628,
                "freq": 7494195,
                "null_count": 66124,
                "top": "notMinister",
                "top10": [
                    {
                        "freq": 7494195,
                        "value": "notMinister",
                    },
                    {
                        "freq": 422433,
                        "value": "Minister",
                    },
                ],
                "unique_count": 2,
            },
            "type": "TEXT",
        },
        {
            "description": "Whether speaker is a Member of Parliament.",
            "name": "speaker_mp",
            "stats": {
                "count": 7916628,
                "freq": 6956913,
                "null_count": 66124,
                "top": "MP",
                "top10": [
                    {
                        "freq": 6956913,
                        "value": "MP",
                    },
                    {
                        "freq": 959715,
                        "value": "notMP",
                    },
                ],
                "unique_count": 2,
            },
            "type": "TEXT",
        },
        {
            "description": 'Full name of the speaker in format "Lastname, Firstname".',
            "name": "speaker_name",
            "stats": {
                "count": 7916628,
                "freq": 105909,
                "null_count": 66124,
                "top": "Arib, Khadija",
                "top10": [
                    {
                        "freq": 105909,
                        "value": "Arib, Khadija",
                    },
                    {
                        "freq": 64370,
                        "value": "Mūrniece, Ināra",
                    },
                    {
                        "freq": 50380,
                        "value": "Lytvyn, Volodymyr Mychajlovyč",
                    },
                    {
                        "freq": 42021,
                        "value": "Reiner, Željko",
                    },
                    {
                        "freq": 41162,
                        "value": "Renson, Hugues",
                    },
                    {
                        "freq": 40837,
                        "value": "Le Fur, Marc",
                    },
                    {
                        "freq": 38904,
                        "value": "Kristensen, Henrik Dam",
                    },
                    {
                        "freq": 38343,
                        "value": "Kjærsgaard, Pia",
                    },
                    {
                        "freq": 37467,
                        "value": "Šeks, Vladimir",
                    },
                    {
                        "freq": 35279,
                        "value": "Waserman, Sylvain",
                    },
                ],
                "unique_count": 22447,
            },
            "type": "TEXT",
        },
        {
            "description": "Party abbreviation.",
            "name": "speaker_party",
            "stats": {
                "count": 7511827,
                "freq": 388715,
                "null_count": 470925,
                "top": "CON",
                "top10": [
                    {
                        "freq": 388715,
                        "value": "CON",
                    },
                    {
                        "freq": 309143,
                        "value": "AKP",
                    },
                    {
                        "freq": 232921,
                        "value": "HDZ",
                    },
                    {
                        "freq": 218728,
                        "value": "CHP",
                    },
                    {
                        "freq": 207972,
                        "value": "LAREM",
                    },
                    {
                        "freq": 166497,
                        "value": "LR",
                    },
                    {
                        "freq": 161215,
                        "value": "LAB",
                    },
                    {
                        "freq": 151504,
                        "value": "PvdA",
                    },
                    {
                        "freq": 142661,
                        "value": "S",
                    },
                    {
                        "freq": 121589,
                        "value": "A",
                    },
                ],
                "unique_count": 765,
            },
            "type": "TEXT",
        },
        {
            "description": "Full name of the party.",
            "name": "speaker_party_name",
            "stats": {
                "count": 7511827,
                "freq": 388715,
                "null_count": 470925,
                "top": "Conservative",
                "top10": [
                    {
                        "freq": 388715,
                        "value": "Conservative",
                    },
                    {
                        "freq": 309143,
                        "value": "Justice and Development Party",
                    },
                    {
                        "freq": 232921,
                        "value": "Hrvatska demokratska zajednica",
                    },
                    {
                        "freq": 218728,
                        "value": "Republican People's Party",
                    },
                    {
                        "freq": 207972,
                        "value": "La République en Marche",
                    },
                    {
                        "freq": 166497,
                        "value": "Les Républicains",
                    },
                    {
                        "freq": 161215,
                        "value": "Labour",
                    },
                    {
                        "freq": 151504,
                        "value": "Partij van de Arbeid",
                    },
                    {
                        "freq": 120799,
                        "value": "Arbeiderpartiet",
                    },
                    {
                        "freq": 117833,
                        "value": "Volkspartij voor Vrijheid en Democratie",
                    },
                ],
                "unique_count": 826,
            },
            "type": "TEXT",
        },
        {
            "description": "Role of the speaker (e.g., Regular, Minister).",
            "name": "speaker_role",
            "stats": {
                "count": 7982752,
                "freq": 5073521,
                "null_count": 0,
                "top": "Regular",
                "top10": [
                    {
                        "freq": 5073521,
                        "value": "Regular",
                    },
                    {
                        "freq": 2792290,
                        "value": "Chairperson",
                    },
                    {
                        "freq": 116941,
                        "value": "Guest",
                    },
                ],
                "unique_count": 3,
            },
            "type": "TEXT",
        },
        {
            "description": "Speech text in the original language.",
            "name": "text",
            "stats": None,
            "type": "TEXT",
        },
        {
            "description": "English machine translation.",
            "name": "text_en",
            "stats": None,
            "type": "TEXT",
        },
        {
            "description": "Country ID as per V-Dem Country Coding Units.",
            "name": "vdem_country_id",
            "stats": None,
            "type": "INTEGER",
        },
        {
            "description": "Number of words in the speech.",
            "name": "word_count",
            "stats": {
                "count": 7982752,
                "max": 35522,
                "mean": 151.703066,
                "median": 39,
                "min": 1,
                "null_count": 0,
                "stddev": 310.70402,
                "unique_count": 5841,
            },
            "type": "INTEGER",
        },
    ]
