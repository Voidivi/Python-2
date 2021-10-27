# !/usr/bin/env python3
# Assignment Week 1 - RSS Feeds
# Author: Lyssette Williams

#importing feedparser was a bit of a pain
#only because I couldn't figure out where I installed python
#plus I am not very confident typing in command

import feedparser

#url is global since I need to declare it before display runs
rss_url = 'https://www.espn.com/espn/rss/news'

#formatting 
def display():
	print('RSS Reader for', rss_url)
	print('='*50)

#the actual feed reeder and formatting
def reader():
	newsfeed = feedparser.parse(rss_url)
	entries = newsfeed.entries[0:5]
	for entry in entries:
		print('Title:', entry.title)
		print('Summary:', entry.summary)
		print('Updated:', entry.published, '\n')
	

def main():
	display()
	reader()


if __name__ == "__main__":
  main() 
