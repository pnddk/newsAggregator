# This program is used to download various newspaper articles using a python script and a json file.
import feedparser
import nltk
import json
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime

#set the limit for number of articles to download
LIMIT = 10

#creating a dict object called data, which stores newspaper articles in a json file and load into news_agg.py
dataEntry = {}
dataEntry['newspapers'] = []

#stub
print ("hello world!")

# load a json file with the list of newspaper websites using a switch case statement instead of for loops. As a reminder,
# when the word "open" appears, it means you are loading a file with the name enclosed in appostrophes and this file will
# remain open for as long as it is needed, which is done when using "with" since it acts as an encapsulated context manager.
with open ('newsite.json') as json_file:
    jsonData = json.load(json_file)
#start with a count at 1, going up to 10 articles
count = 1

#the following line iterates through the newspaper companies and prints out tuple pairs of information using a Python Dict Method items() 
#the following code checks for any value in the items() method in the json file, specifically the rss, publishing date and regular news article using if statements
for newspaper, value in jsonData.items():
    if 'rss' in value:
        data = feedparser.parse(value['rss'])
        print ("Downloading from: ", newspaper)
        newsArticle = {
                "rss": value['rss'],
                "link": value['link'],
                "articles": []
        }

       
    

#run a for loop that looks for the title of the particular news article, print it
#run a for loop that looks for the date of the article, print it
#print the url of the article(s)



#run a machine learning algorithm here...

#add a training set of data for newspaper websites???? Maybe this can be other newspaper topics in the same vein...

#add an optimization method to fine tune learning algorithm such as alpha-beta or markov tree decision. This specifically can contain weight functions as a for loop for accounting for different weight factors.



