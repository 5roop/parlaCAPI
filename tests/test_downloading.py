formats = ["xlsx", "tsv", "csv", "jsonl", "parquet", "rds"]

from pathlib import Path
import requests
import pytest
import polars as pl

url = "https://parlacap.ipipan.waw.pl/"


@pytest.mark.parametrize("metadata", [True, False])
@pytest.mark.parametrize("format", formats)
def test_downloading_file(format: str, metadata: bool):
    filter = {
        "filter": {"column": "parliament", "value": "SI", "operator": "="},
        "limit": 10,
        "offset": 10,
        "order_by": ["id"],
    }

    response = requests.post(
        url + f"download?format={format}&include_metadata={str(metadata).lower()}",
        json=filter,
    )
    if not response.status_code == 200:
        raise Exception(
            f"Got weird response code: {response.status_code}, response text: {response.text}"
        )
    p = Path(f"downloaded_data{'_metadata' if metadata else '_no_metadata'}.{format}")
    p.write_bytes(response.content)
    assert p.exists()

    handler = {
        ("csv", False): lambda s: pl.read_csv(
            s,
        ),
        ("csv", True): lambda s: pl.read_csv(s, skip_rows=7),
        ("tsv", False): lambda s: pl.read_csv(
            s,
            separator="\t",
        ),
        ("tsv", True): lambda s: pl.read_csv(s, separator="\t", skip_rows=7),
        ("parquet", False): pl.read_parquet,
        ("parquet", True): pl.read_parquet,
        ("xlsx", True): pl.read_excel,
        ("xlsx", False): pl.read_excel,
    }
    if handler.get((format, metadata), False):
        df = handler[(format, metadata)](p)
        assert df.height == 10

    # p.unlink()
