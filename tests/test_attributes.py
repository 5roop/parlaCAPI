url = "https://parlacap.ipipan.waw.pl/"

import requests
import pytest


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


def test_variables():
    response = requests.get(url + "variables")
    if not response.status_code == 200:
        raise Exception(f"Got weird response code: {response.status_code}")
    payload = response.json()
    assert payload == [
        {
            "name": "cap_category",
            "type": "TEXT",
            "description": "Predicted CAP category.",
            "stats": {
                "count": 7982341,
                "unique_count": 23,
                "top": "Other",
                "freq": 3921514,
                "top10": [
                    {"value": "Other", "freq": 3921514},
                    {"value": "Mix", "freq": 417071},
                    {"value": "Macroeconomics", "freq": 397359},
                    {"value": "Government Operations", "freq": 340523},
                    {"value": "Law and Crime", "freq": 326293},
                    {"value": "Health", "freq": 316597},
                    {"value": "International Affairs", "freq": 259153},
                    {"value": "Civil Rights", "freq": 228896},
                    {"value": "Education", "freq": 201170},
                    {"value": "Labor", "freq": 172098},
                ],
            },
        },
        {
            "name": "cap_prob",
            "type": "REAL",
            "description": "CAP category prediction probability.",
            "stats": {
                "count": 7982341,
                "unique_count": 880,
                "min": 0.069,
                "max": 0.998,
                "mean": 0.936103,
                "median": 0.993,
                "stddev": 0.131348,
            },
        },
        {
            "name": "date",
            "type": "TEXT",
            "description": "Date of the session.",
            "stats": {
                "count": 7982752,
                "unique_count": 5723,
                "top": "2016-11-23",
                "freq": 11668,
                "top10": [
                    {"value": "2016-11-23", "freq": 11668},
                    {"value": "2017-12-13", "freq": 10302},
                    {"value": "2016-12-14", "freq": 9766},
                    {"value": "2020-12-10", "freq": 9511},
                    {"value": "2018-12-20", "freq": 9188},
                    {"value": "2015-12-17", "freq": 9172},
                    {"value": "2017-11-23", "freq": 9027},
                    {"value": "2017-11-22", "freq": 9019},
                    {"value": "2017-12-20", "freq": 8962},
                    {"value": "2020-12-15", "freq": 8779},
                ],
            },
        },
        {"name": "id", "type": "INTEGER", "description": "Primary key", "stats": None},
        {
            "name": "lang",
            "type": "TEXT",
            "description": "Language of the transcript",
            "stats": {
                "count": 7982752,
                "unique_count": 30,
                "top": "French",
                "freq": 795637,
                "top10": [
                    {"value": "French", "freq": 795637},
                    {"value": "Turkish", "freq": 739744},
                    {"value": "Dutch", "freq": 699925},
                    {"value": "English", "freq": 671038},
                    {"value": "Croatian", "freq": 504334},
                    {"value": "Ukrainian", "freq": 402731},
                    {"value": "Danish", "freq": 398610},
                    {"value": "Greek", "freq": 342274},
                    {"value": "Norwegian bokmål", "freq": 334636},
                    {"value": "Serbian", "freq": 316069},
                ],
            },
        },
        {
            "name": "parlacap_id",
            "type": "TEXT",
            "description": "Original document ID from ParlaCap",
            "stats": None,
        },
        {
            "name": "parlamint_id",
            "type": "TEXT",
            "description": "Original speech ID from ParlaMint.",
            "stats": None,
        },
        {
            "name": "parlamint_text_id",
            "type": "TEXT",
            "description": "Original document ID from ParlaMint.",
            "stats": None,
        },
        {
            "name": "parliament",
            "type": "TEXT",
            "description": "Parliament code (e.g. BA, ES-GA, ...)",
            "stats": {
                "count": 7982752,
                "unique_count": 28,
                "top": "TR",
                "freq": 739744,
                "top10": [
                    {"value": "TR", "freq": 739744},
                    {"value": "FR", "freq": 714439},
                    {"value": "GB", "freq": 670912},
                    {"value": "NL", "freq": 609209},
                    {"value": "HR", "freq": 504334},
                    {"value": "UA", "freq": 429156},
                    {"value": "NO", "freq": 398809},
                    {"value": "DK", "freq": 398610},
                    {"value": "GR", "freq": 342274},
                    {"value": "RS", "freq": 316069},
                ],
            },
        },
        {
            "name": "party_orientation",
            "type": "TEXT",
            "description": "Political orientation (e.g., left, right).",
            "stats": {
                "count": 6582010,
                "unique_count": 44,
                "top": "Centre-right",
                "freq": 1750355,
                "top10": [
                    {"value": "Centre-right", "freq": 1750355},
                    {"value": "Centre-left", "freq": 1375925},
                    {"value": "Centre", "freq": 609294},
                    {"value": "Right", "freq": 470346},
                    {"value": "Centre-right to right", "freq": 407410},
                    {"value": "Centre to centre-right", "freq": 331286},
                    {"value": "Centre-left to left", "freq": 311292},
                    {"value": "Right to far-right", "freq": 290246},
                    {"value": "Centre to centre-left", "freq": 271278},
                    {"value": "Left", "freq": 207241},
                ],
            },
        },
        {
            "name": "party_status",
            "type": "TEXT",
            "description": "Government or opposition or coalition.",
            "stats": {
                "count": 5666374,
                "unique_count": 2,
                "top": "Coalition",
                "freq": 3095316,
                "top10": [
                    {"value": "Coalition", "freq": 3095316},
                    {"value": "Opposition", "freq": 2571058},
                ],
            },
        },
        {
            "name": "partyfacts_id",
            "type": "TEXT",
            "description": "Party ID in the Party Facts database",
            "stats": None,
        },
        {
            "name": "sent3_category",
            "type": "TEXT",
            "description": "Sentiment estimation as a 3-category label (Negative, Neutral, Positive).",
            "stats": {
                "count": 7982752,
                "unique_count": 3,
                "top": "Neutral",
                "freq": 4670289,
                "top10": [
                    {"value": "Neutral", "freq": 4670289},
                    {"value": "Negative", "freq": 1724121},
                    {"value": "Positive", "freq": 1588342},
                ],
            },
        },
        {
            "name": "sent6_category",
            "type": "TEXT",
            "description": "Sentiment estimation as a 6-category label (Negative, Mixed Negative, Neutral Negative, Neutral Positive, Mixed Positive, Positive).",
            "stats": {
                "count": 7982752,
                "unique_count": 6,
                "top": "Neutral Positive",
                "freq": 2889729,
                "top10": [
                    {"value": "Neutral Positive", "freq": 2889729},
                    {"value": "Neutral Negative", "freq": 1780560},
                    {"value": "Mixed Positive", "freq": 1377031},
                    {"value": "Mixed Negative", "freq": 1250959},
                    {"value": "Negative", "freq": 473162},
                    {"value": "Positive", "freq": 211311},
                ],
            },
        },
        {
            "name": "sent_logit",
            "type": "REAL",
            "description": "Sentiment estimation as a floating point value, on a scale of 0 to 6, with 0 being negative. Sentiment is calculated as a length-weighed average of sentiments of sentences in the speech.",
            "stats": {
                "count": 7982752,
                "unique_count": 5876,
                "min": -9.522,
                "max": 5.797,
                "mean": 2.515722,
                "median": 2.705,
                "stddev": 1.138799,
            },
        },
        {
            "name": "speaker_birth",
            "type": "INTEGER",
            "description": "Birth year of the speaker.",
            "stats": {
                "count": 6578947,
                "unique_count": 85,
                "min": 1905,
                "max": 2002,
                "mean": 1963.525527,
                "median": 1963,
                "stddev": 11.624132,
            },
        },
        {
            "name": "speaker_gender",
            "type": "TEXT",
            "description": "Gender of the speaker (M or F).",
            "stats": {
                "count": 7916628,
                "unique_count": 3,
                "top": "M",
                "freq": 5691694,
                "top10": [
                    {"value": "M", "freq": 5691694},
                    {"value": "F", "freq": 2214180},
                    {"value": "U", "freq": 10754},
                ],
            },
        },
        {
            "name": "speaker_id",
            "type": "TEXT",
            "description": 'Unique speaker identifier, usually in format "LastnameFirstName".',
            "stats": {
                "count": 7916628,
                "unique_count": 22510,
                "top": "KhadijaArib",
                "freq": 105909,
                "top10": [
                    {"value": "KhadijaArib", "freq": 105909},
                    {"value": "MūrnieceInāra", "freq": 64370},
                    {"value": "ВолодимирМихайловичЛитвин.1956", "freq": 50380},
                    {"value": "ReinerŽeljko", "freq": 42021},
                    {"value": "PA721824", "freq": 41162},
                    {"value": "PA1874", "freq": 40837},
                    {"value": "KristensenHenrikDam", "freq": 38904},
                    {"value": "KjærsgaardPia", "freq": 38342},
                    {"value": "ŠeksVladimir", "freq": 37467},
                    {"value": "PA720746", "freq": 35279},
                ],
            },
        },
        {
            "name": "speaker_minister",
            "type": "TEXT",
            "description": "Whether speaker is a minister.",
            "stats": {
                "count": 7916628,
                "unique_count": 2,
                "top": "notMinister",
                "freq": 7494195,
                "top10": [
                    {"value": "notMinister", "freq": 7494195},
                    {"value": "Minister", "freq": 422433},
                ],
            },
        },
        {
            "name": "speaker_mp",
            "type": "TEXT",
            "description": "Whether speaker is a Member of Parliament.",
            "stats": {
                "count": 7916628,
                "unique_count": 2,
                "top": "MP",
                "freq": 6956913,
                "top10": [
                    {"value": "MP", "freq": 6956913},
                    {"value": "notMP", "freq": 959715},
                ],
            },
        },
        {
            "name": "speaker_name",
            "type": "TEXT",
            "description": 'Full name of the speaker in format "Lastname, Firstname".',
            "stats": {
                "count": 7916628,
                "unique_count": 22447,
                "top": "Arib, Khadija",
                "freq": 105909,
                "top10": [
                    {"value": "Arib, Khadija", "freq": 105909},
                    {"value": "Mūrniece, Ināra", "freq": 64370},
                    {"value": "Lytvyn, Volodymyr Mychajlovyč", "freq": 50380},
                    {"value": "Reiner, Željko", "freq": 42021},
                    {"value": "Renson, Hugues", "freq": 41162},
                    {"value": "Le Fur, Marc", "freq": 40837},
                    {"value": "Kristensen, Henrik Dam", "freq": 38904},
                    {"value": "Kjærsgaard, Pia", "freq": 38343},
                    {"value": "Šeks, Vladimir", "freq": 37467},
                    {"value": "Waserman, Sylvain", "freq": 35279},
                ],
            },
        },
        {
            "name": "speaker_party",
            "type": "TEXT",
            "description": "Party abbreviation.",
            "stats": {
                "count": 7511827,
                "unique_count": 765,
                "top": "CON",
                "freq": 388715,
                "top10": [
                    {"value": "CON", "freq": 388715},
                    {"value": "AKP", "freq": 309143},
                    {"value": "HDZ", "freq": 232921},
                    {"value": "CHP", "freq": 218728},
                    {"value": "LAREM", "freq": 207972},
                    {"value": "LR", "freq": 166497},
                    {"value": "LAB", "freq": 161215},
                    {"value": "PvdA", "freq": 151504},
                    {"value": "S", "freq": 142661},
                    {"value": "A", "freq": 121589},
                ],
            },
        },
        {
            "name": "speaker_party_name",
            "type": "TEXT",
            "description": "Full name of the party.",
            "stats": {
                "count": 7511827,
                "unique_count": 826,
                "top": "Conservative",
                "freq": 388715,
                "top10": [
                    {"value": "Conservative", "freq": 388715},
                    {"value": "Justice and Development Party", "freq": 309143},
                    {"value": "Hrvatska demokratska zajednica", "freq": 232921},
                    {"value": "Republican People's Party", "freq": 218728},
                    {"value": "La République en Marche", "freq": 207972},
                    {"value": "Les Républicains", "freq": 166497},
                    {"value": "Labour", "freq": 161215},
                    {"value": "Partij van de Arbeid", "freq": 151504},
                    {"value": "Arbeiderpartiet", "freq": 120799},
                    {
                        "value": "Volkspartij voor Vrijheid en Democratie",
                        "freq": 117833,
                    },
                ],
            },
        },
        {
            "name": "speaker_role",
            "type": "TEXT",
            "description": "Role of the speaker (e.g., Regular, Minister).",
            "stats": {
                "count": 7982752,
                "unique_count": 3,
                "top": "Regular",
                "freq": 5073521,
                "top10": [
                    {"value": "Regular", "freq": 5073521},
                    {"value": "Chairperson", "freq": 2792290},
                    {"value": "Guest", "freq": 116941},
                ],
            },
        },
        {
            "name": "text",
            "type": "TEXT",
            "description": "Speech text in the original language.",
            "stats": {
                "count": 7982752,
                "unique_count": 6662755,
                "top": "Ordføreren.",
                "freq": 34988,
                "top10": [
                    {"value": "Ordføreren.", "freq": 34988},
                    {"value": "Ne ha facoltà.", "freq": 29306},
                    {"value": "Deputāti atbalsta.", "freq": 22997},
                    {"value": "Quel est l'avis du Gouvernement ?", "freq": 22545},
                    {"value": "Quel est l'avis de la commission ?", "freq": 21628},
                    {"value": "Ναι.", "freq": 20781},
                    {"value": "Domando di parlare.", "freq": 19179},
                    {"value": "Ministeren.", "freq": 17933},
                    {"value": "Sayın Başkan…", "freq": 11819},
                    {"value": "Όχι.", "freq": 11181},
                ],
            },
        },
        {
            "name": "text_en",
            "type": "TEXT",
            "description": "English machine translation.",
            "stats": {
                "count": 7982752,
                "unique_count": 6573929,
                "top": "The rapporteur.",
                "freq": 35080,
                "top10": [
                    {"value": "The rapporteur.", "freq": 35080},
                    {"value": "You have the right to do so.", "freq": 29308},
                    {"value": "Yeah.", "freq": 26021},
                    {"value": "Here you go.", "freq": 24334},
                    {"value": "Members are in favour.", "freq": 22997},
                    {"value": "What is the Government's opinion?", "freq": 22546},
                    {"value": "What is the opinion of the committee?", "freq": 21630},
                    {"value": "I'm asking to talk.", "freq": 19179},
                    {"value": "All right!", "freq": 18164},
                    {"value": "The minister.", "freq": 17934},
                ],
            },
        },
        {
            "name": "vdem_country_id",
            "type": "INTEGER",
            "description": "Country ID as per V-Dem Country Coding Units.",
            "stats": None,
        },
        {
            "name": "word_count",
            "type": "INTEGER",
            "description": "Number of words in the speech.",
            "stats": {
                "count": 7982752,
                "unique_count": 5841,
                "min": 1,
                "max": 35522,
                "mean": 151.703066,
                "median": 39,
                "stddev": 310.70402,
            },
        },
    ]
