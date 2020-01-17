#! /usr/bin/python3

from wordcloud import WordCloud, STOPWORDS
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
stop_words = ["https", "co", "RT"] + list(STOPWORDS)

wordcloud = WordCloud(stopwords = stop_words, width = 480, height = 480, margin = 0).generate(txt)

pngname = "CT_tweets.png"
print("Am make file " + pngname)
wordcloud.to_file(pngname)
