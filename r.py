""""
GitHub: https://github.com/4144414D/r
Email: adam@nucode.co.uk

Usage:
  r <text_file> <regex_file>
  r --version
  r --help
"""
VERSION="0.1"

from docopt import docopt
import sys
import re

def r(text_file, regex_file):
    try:
        text_data = open(text_file).read()
    except:
        print "ERROR: unable to read text file"
        sys.exit(1)

    try:
        raw_regex = []
        for line in open(regex_file):
            raw_regex.append(line[:-1])
    except:
        print "ERROR: unable to read text file"
        sys.exit(1)

    parsed_regex = []
    for regex in raw_regex:
        try:
            parsed_regex.append([regex,re.compile(regex)])
        except:
            print "ERROR: incorrect regex syntax",
            print regex

    if parsed_regex:
        for regex in parsed_regex:
            results = re.findall(regex[1], text_data)
            print '{} matches {}!'.format(regex[0], len(results))
            for match in results:
                print match
            print

if __name__ == '__main__':
        arguments = docopt(__doc__, version=VERSION)
        r(arguments['<text_file>'], arguments['<regex_file>'])
