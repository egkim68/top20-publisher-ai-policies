"""Reproduce the top 20 publisher groups from the archived SJR 2025 CSV."""
import argparse
import collections
import csv
import hashlib
from pathlib import Path
import re

CHECKSUM = 'ead12360e11e9ebc2f4eb7280315540d0bfac69897f9f3b722ebe5039c43d523'
ROOT = Path(__file__).resolve().parent


def covers_2025(value):
    return any(int(a) <= 2025 <= int(b or a)
               for a, b in re.findall(r'(\d{4})(?:-(\d{4}))?', value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='SJR 2025 CSV (semicolon-delimited)')
    args = parser.parse_args()
    if hashlib.sha256(args.source.read_bytes()).hexdigest() != CHECKSUM:
        parser.error('Input checksum differs from the analyzed dataset.')

    with (ROOT / 'publisher_alias_mapping.csv').open(encoding='utf-8', newline='') as f:
        mapping = {r['Raw publisher label']: r['Publisher group'] for r in csv.DictReader(f)}
    with args.source.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader)
        rows = [dict(zip(header, r)) for r in reader]

    journals = [r for r in rows if r['Type'] == 'journal']
    eligible = [r for r in journals if covers_2025(r['Coverage']) and r['Publisher'].strip()]
    counts = collections.Counter(mapping[r['Publisher']] for r in eligible)
    top = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:20]
    top_groups = {group for group, _ in top}

    with open('reproduced_top_20.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Rank', 'Publisher group', 'Journal count'])
        writer.writerows((i, group, n) for i, (group, n) in enumerate(top, 1))
    with open('selected_journals.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Publisher group', 'SJR publisher label', 'Sourceid', 'Title', 'Issn'])
        writer.writerows((mapping[r['Publisher']], r['Publisher'], r['Sourceid'], r['Title'], r['Issn'])
                         for r in eligible if mapping[r['Publisher']] in top_groups)

    with (ROOT / 'top_20_publishers.csv').open(encoding='utf-8', newline='') as f:
        expected = [(r['Publisher group'], int(r['Journal count'])) for r in csv.DictReader(f)]
    print(f'{len(eligible):,} eligible journals; {len(counts):,} publisher groups.')
    print('Matches top_20_publishers.csv.' if top == expected else 'Differs from top_20_publishers.csv.')


if __name__ == '__main__':
    main()
