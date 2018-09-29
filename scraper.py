import argparse
import json
import urllib2

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--username',
                    metavar='-u',
                    required=True,
                    type=str,
                    help='Username to get keys for')
args = parser.parse_args()

data = json.load(urllib2.urlopen('https://api.github.com/users/' + args.username + '/keys'))

for item in data:
    print item['key']
