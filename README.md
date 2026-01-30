# Testing ParlaCAPI

Issues found:
* Column names: `parlmint_text_id` (sic) and `parlmint_id` (even siccer). Should be `parlamint_text_id` and `parlamint_id`.
* The following columns seem to always be empty (tested on a 30k sample):
  * `parlmint_text_id`
  * `parlmint_id`
  * `cap_category`
  * `cap_prob`

Open questions:
* ~~Is there pagination? It would be nice to split the request in N batches.~~
* ~~Is it possible to specify return columns?~~
* How can we filter null values?
* On the website: search field in /filter would benefit from an example.
* On the website: it is not clear what the "Supported Operators" are and how to use them, except maybe

Lessons learned:
* headers are not needed when calling the API via requests.
* When filtering, the result is repeatable, even with shuffled filter conditions. This is good.
* Pagination can be done using the /filter by specifying limit and offset as:
  * `"limit":100, "offset":0`
  * `"limit":100, "offset":100`
  * and so on
* By default, 100 instances will be returned when filtering. This can be tweaked with `limit` parameter, but it can only vary between 1 and 1000.
* With filters, one can specify return columns.
*