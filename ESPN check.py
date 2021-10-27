import feedparser

newsfeed = feedparser.parse("https://www.espn.com/espn/rss/news")
entry = newsfeed.entries[0]

print ('Number of RSS posts :', len(newsfeed.entries))
print ('Available properties :', entry.keys())
