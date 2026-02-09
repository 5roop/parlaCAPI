# Testing ParlaCAPI

## Status as of 2026-02-06T13:17:28

All of the issues identified have been resolved.

Further questions:
1. Do we want to bother with /preview endpoint?

Bugs found:
1. `partyfacts_id` shows up as `"1011.0"`. This can be an int.
2. If filtering with an illogical query, the error message could be improved.



## Issues found:
* Column names: `parlmint_text_id` and `parlmint_id`. Should be `parlamint_text_id` and `parlamint_id`.
* The following columns seem to always be empty (tested on a 30k sample):
  * `parlmint_text_id`
  * `parlmint_id`
  * `cap_category`
  * `cap_prob`
* The null issues persist on all urls, so /filter, /download, and /sample

## Open questions:
* ~~Is there pagination? It would be nice to split the request in N batches.~~
* ~~Is it possible to specify return columns?~~
* How can we filter out null values?
* On the website: search field in /filter would benefit from an example.
* On the website: Supported Operators would benefit from a few examples

## Lessons learned:
* headers (`-H 'accept: application/json'`) are not needed when calling the API via requests.
* When filtering, the result is repeatable, even with shuffled filter conditions. This is good.
* Pagination can be done using the /filter by specifying limit and offset as:
  * `"limit":100, "offset":0`
  * `"limit":100, "offset":100`
  * and so on
* By default, 100 instances will be returned when filtering. This can be tweaked with `limit` parameter, but it can only vary between 1 and 1000.
* With filters, one can specify return columns and save bandwidth and compute resources.

## Downloading:

The files obtained via the /download url in TSV or CSV have a preamble:
```
# Metadata used to filter data
# exported_at: "2026-01-30 14:55:49"
# format: "csv"
# filters: {"column": "parliament", "operator": "=", "value": "SI"}
# search: null
# columns: null

```
while for JSONL the preamble is
```
{"_meta": {"description": "Metadata used to filter data", "exported_at": "2026-01-30 15:17:04", "format": "jsonl", "filters": {"column": "parliament", "operator": "=", "value": "SI"}, "search": null, "columns": null}}
```

I don't like this, it's packaging metadata with data, and if at all possible, this should be removed.

Interestingly enough, parquet files can be read with pandas without dealing with the preamble.


# Migrating to pytest

Requirements: pytest and polars

Invoking: `parlaCAPI$ pytest tests -vv`

The set of tests is not yet complete and will be expanded on.