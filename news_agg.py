import feedparser as fp
import json
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime

#set the limit for number of articles to download
LIMIT = 5

data = {}
data['newspaper articles'] = {}


print ("hello world!")

