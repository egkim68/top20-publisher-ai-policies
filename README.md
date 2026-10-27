# Top 20 publishers and reviewer AI upload policies

Supporting data for Table 1 of "Beyond manuscript upload prohibitions: Author consent and responsible AI assistance in peer review."

## Files

* `rank_publishers.py`: selects the 20 largest publisher groups (Python 3, standard library).
* `publisher_alias_mapping.csv`: assigns each SJR publisher label to a publisher group.
* `top_20_publishers.csv`: ranking and journal counts.
* `policy_evidence.csv`: classification, supporting excerpt and source for each publisher.

## Publisher selection

Source: SCImago Journal & Country Rank 2025 (https://www.scimagojr.com/journalrank.php?year=2025&type=j), analyzed October 26, 2026. The file is not redistributed. SHA-256: `ead12360e11e9ebc2f4eb7280315540d0bfac69897f9f3b722ebe5039c43d523`.

Journals with 2025 coverage and a named publisher (28,039) were grouped by owner and counted. Ties are broken alphabetically.

```bash
python rank_publishers.py sjr2025.csv
```

The script writes `reproduced_top_20.csv` and `selected_journals.csv` (the journals counted) and reports whether the ranking matches `top_20_publishers.csv`.

## Policy classification

Public reviewer guidance was collected on October 20, 2026; excerpts were rechecked on October 27, 2026. Pages may change, so excerpts are recorded with each source.

* **No**: manuscript upload to AI tools prohibited.
* **Conditional**: upload permitted under stated conditions.
* **No policy**: no publisher-level rule identified; individual journals may differ. This does not mean permission.
* **Not verified**: policy could not be accessed.

An asterisk (*) marks limited scope, explained in the Note column.
