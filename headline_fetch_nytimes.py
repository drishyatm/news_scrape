from feedsearch import search
import feedparser
import time
import csv

feeds = search('nytimes.com')
urls = [f.url for f in feeds]
titles_list = []
if len(urls) > 0:
  news_feed = feedparser.parse(urls[0])
  entries = news_feed["entries"]
  count=0
  for entry in entries:
    a={}
    count = count + 1
    print(
     str(count) + ". " + entry["title"] \
     + "\n\t\t" + entry["published"] \
     + "\n\t\t" + entry["link"]\
     + "\n\n"
     )
    a['Title Number'] = f'Title {count}'
    a['Title Name'] = entry["title"]
    a['Date Published'] = entry["published"]
    titles_list.append(a)
    if count ==2:
        break;
filename = 'headline_nytimes.csv'
with open(filename, 'a', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name','Date Published'])
    #w.writeheader()
     
    w.writerows(titles_list)
    time.sleep(0.33)