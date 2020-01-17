#! /usr/bin/python3

import sys
import requests
from bs4 import  BeautifulSoup

print ("You run %s" % (sys.argv[0]))

if len(sys.argv) < 2:
    print("give name html file")
    sys.exit()
else:
    text = open(sys.argv[1], "r")

print("Me read %s" % str(sys.argv[1]))

soup = BeautifulSoup(text, 'html.parser')

tweets = [p.text for p in soup.findAll('p')]
txt = ' '.join(tweets)

for t in tweets:
    print(t)

with open('bestfilename.txt', 'w') as f:
    for t in tweets:
        f.write(t + "\n")
