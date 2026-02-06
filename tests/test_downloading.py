formats = ["xlsx", "tsv", "csv", "jsonl", "parquet", "rds"]

from pathlib import Path
import requests
import pytest
import polars as pl

url = "https://parlacap.ipipan.waw.pl/"


@pytest.mark.parametrize("format", formats)
def test_downloading_file(format):
    filter = {
        "filter": {"column": "parliament", "value": "SI", "operator": "="},
        "limit": 10,
        "offset": 10,
        "order_by": ["id"],
    }

    response = requests.post(
        url + f"download?format={format}",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, response text: {response.text}"
        )
    p = Path(f"downloaded_data.{format}")
    p.write_bytes(response.content)
    assert p.exists()

    handler = {
        "csv": lambda s: pl.read_csv(
            s,
            #  skip_rows=7
        ),
        "tsv": lambda s: pl.read_csv(
            s,
            separator="\t",
            #  skip_rows=7
        ),
        "parquet": pl.read_parquet,
    }
    if handler.get(format, False):
        df = handler[format](p)
        assert df.height == 10

    # p.unlink()
