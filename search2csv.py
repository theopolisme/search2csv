import os
import sys
import glob
import json
import argparse
from datetime import datetime
from operator import itemgetter

try:
    import unicodecsv as csv
except:
    import csv


def make_iso_from_usec(usec):
    return datetime.fromtimestamp(float(usec)/1000000).isoformat()


def get_searches_from_json(raw):
    events = json.loads(raw)['event']
    return map(lambda e: {
        'timestamp': make_iso_from_usec(e['query']['id'][0]['timestamp_usec']),
        'query': e['query']['query_text']
    }, events)


def get_searches_from_files(paths):
    searches = []
    for path in paths:
        with open(path) as f:
            searches += get_searches_from_json(f.read())

    searches.sort(key=itemgetter('timestamp'))
    return searches


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source',
                        help='Directory of Search JSON files to convert')
    parser.add_argument('output',
                        nargs='?',
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Where to write CSV output (default: stdout)')
    args = parser.parse_args()

    files = glob.glob(os.path.join(args.source, '*.json'))

    searches = get_searches_from_files(files)

    with args.output as f:
        writer = csv.DictWriter(f, searches[0].keys())
        writer.writeheader()
        writer.writerows(searches)

if __name__ == '__main__':
    main()
