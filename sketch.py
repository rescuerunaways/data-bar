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
import operator

#this value to change to ds one
hardcode_best = 4.0

def el(x): return [x['name'], isRanked(x)]

def fl(x): return float(x[1])> hardcode_best

def isRanked(x):
    if 'rating' in x : return x['rating']
    else: return 0.0

def find(args):
    res = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?location=-37.8251586,144.9605128&radius=400&type=bar&key=AIzaSyA6_gacsifsaFHXJeCWUlY6vAC2VH8pm7c')

    l = json.loads(res.text)['results']
    print(filter(fl, dict(map(el, l)).items()))

if __name__ == '__main__':
    args = docopt(__doc__)


if args['find']:
    find(args)
