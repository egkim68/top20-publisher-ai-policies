# Top 20 publishers and reviewer AI upload policies

Supporting data for Table 1 of “Should authors be able to consent to AI assistance in peer review?”

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

### Grouping decisions

SJR lists journals under imprint and legal-entity names. Each label was assigned to the publisher that owned it at the time of analysis, including recent acquisitions. Examples:

* Elsevier: Cell Press, Academic Press, W.B. Saunders, Elsevier Masson.
* Springer Nature: BioMed Central, Nature Research, Palgrave Macmillan, Adis.
* Taylor & Francis: Routledge, Dove Medical Press, F1000, PeerJ, Maney.
* Sage: Mary Ann Liebert, IOS Press.
* De Gruyter Brill: Brill, Sciendo, Ubiquity Press, Vandenhoeck & Ruprecht.
* Wolters Kluwer: Lippincott, Medknow.
* Science Press: EDP Sciences.

Labels with similar names but different owners were kept separate, such as Springer Publishing Company, Russell Sage Foundation, Cambridge Scientific Publishers and World Scientific and Engineering Academy and Society.

Two publishers were counted separately from a larger partner:

* KeAi (162 journals), a joint venture of China Science Publishing & Media and Elsevier.
* Pleiades Publishing (141 journals), whose journals Springer Nature distributes under a partnership.

Both publish under their own names. Merging either into its partner would remove it from the top 20 and add S. Karger AG (89 journals, rank 21). Thieme ranks 20th with 101 journals. Bentham Science and World Scientific tie at 120 journals.

### Limitations

* Journals with 2025 coverage but no publisher listed in SJR (696) were excluded.
* Ranking by journal count favors publishers with many small journals over those with high article output. For example, Public Library of Science has 13 journals in the dataset.
* Ownership reflects the analysis date. Later acquisitions may change the grouping.

## Policy classification

Public reviewer guidance was collected on October 27, 2026 and last verified on November 26, 2026. These pages may change; thus, excerpts are provided for each source.

* **No**: manuscript upload to AI tools prohibited.
* **Conditional**: upload permitted under stated conditions.
* **No policy**: no publisher-level rule identified; individual journals may differ. This does not mean permission.
* **Not verified**: policy could not be accessed.

Markers a) and b) flag limited scope, as in Table 1: a) prohibition stated for one imprint only; b) prohibition stated for public AI platforms, without explicit permission for secure tools. Conditional is assigned only when the guidance explicitly permits upload under stated conditions.
