#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Fetch comments and anchor tags from a website')
parser.add_argument('-u', '--urll', type=str, help='URL to scrape.')

arg = parser.parse_args()

print(arg.urll)