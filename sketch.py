#! /usr/bin/python

"""Rests.

Usage:
  sketch.py find

Options:
  -h --help     Show this screen.

"""
from docopt import docopt
import requests
import json
from fn import _

def el(x): return [x['name'], isRanked(x)]

def isRanked(x):
    if ('rating' in x): return x['rating']
    else: return 'not rated'

def find(args):
    res = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?location=-37.8251586,144.9605128&radius=400&type=bar&key=AIzaSyA6_gacsifsaFHXJeCWUlY6vAC2VH8pm7c')

    parsed_json = json.loads(res.text)
    list_json = parsed_json['results']

    print(dict(map(el, list_json)))

if __name__ == '__main__':
    args = docopt(__doc__)


if args['find']:
    find(args)
