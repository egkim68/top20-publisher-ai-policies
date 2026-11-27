# Top 20 publishers and reviewer AI upload policies

Supporting data for Table 1 of “Should authors be able to consent to AI assistance in peer review?”

## Files

* `rank_publishers.py`: selects the 20 largest publisher groups (Python 3, standard library).
* `publisher_alias_mapping.csv`: assigns each SJR publisher label to a publisher group.
* `top_20_publishers.csv`: ranking and journal counts.
* `policy_evidence.csv`: classification, verbatim excerpt, source, note and access date for each publisher.

## Publisher selection

Source: SCImago Journal & Country Rank 2025 (https://www.scimagojr.com/journalrank.php?year=2025&type=j), analyzed October 26, 2026. The file is not redistributed. SHA-256: `ead12360e11e9ebc2f4eb7280315540d0bfac69897f9f3b722ebe5039c43d523`.

Journals with 2025 coverage and a named publisher (28,039) were grouped by owner, including acquired imprints, and counted. Ties are broken alphabetically. KeAi (an Elsevier joint venture) and Pleiades Publishing (distributed by Springer Nature) are counted as separate publishers. Merging either would replace it with S. Karger AG (89 journals, rank 21).

```bash
python rank_publishers.py sjr2025.csv
```

The script reports whether the result matches `top_20_publishers.csv`.

## Policy classification

Public reviewer guidance was collected from publisher websites. Excerpts and access dates are recorded with each source because pages may change.

* **No**: manuscript upload to AI tools prohibited.
* **Conditional**: upload explicitly permitted under stated conditions.
* **No policy**: no publisher-level rule identified. This does not mean permission.
* **Not verified**: policy could not be accessed.

Markers a) and b) flag limited scope, as in Table 1: a) one imprint only; b) public AI platforms only.
