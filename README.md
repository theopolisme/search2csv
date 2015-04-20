search2csv
=============

*Export your Google search history as a CSV*

Google just added the ability to export your complete search history as JSON. *This is super cool!* Unfortunately, the exported form is a series of JSON files that aren't very easy to work with. *search2csv* concatenates them all into a single CSV containing just timestamps and searches, so you can get to the fun part... analyzing it.

## Usage

*Having trouble with UnicodeEncodeErrors? This is probably because Python's CSV module doesn't support Unicode. Try `pip install unicodecsv` and then run the script again.*

First, download your Google Search History by following [these instructions](https://support.google.com/websearch/answer/6068625?p=ws_history_download&rd=1). Unzip the file, and you should be left with a "Searches" directory, inside of which there should be *another* "Searches" directory. Run `search2csv.py`, passing in the path to the second Searches directory, and you're all done:

```
$ python search2csv.py /path/to/Searches/Searches /path/to/output.csv
```

Slightly more detailed:

```
$ python search2csv.py -h
usage: search2csv.py [-h] source [output]

positional arguments:
  source      Directory of Search JSON files to convert
  output      Where to write CSV output (default: stdout)

optional arguments:
  -h, --help  show this help message and exit
```

## Output

`search2csv` produces a CSV file in the following format, ordered chronologically:

```csv
timestamp,query
2015-04-20T14:09:56.712142,example query
2015-04-20T14:40:37.117257,example query 2
...
```

Happy analyzing!
