# This program is used to download various newspaper articles using a python script and a json file.
import feedparser as fp
import json
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime

#set the limit for number of articles to download
LIMIT = 10

#creating a dict object called data, which stores newspaper articles in a json file and load into news_agg.py
data = {}
data['newspapers'] = []

#stub
print ("hello world!")

# load a json file with the list of newspaper websites using a switch case statement instead of for loops. As a reminder,
# when the word "open" appears, it means you are loading a file with the name enclosed in appostrophes and this file will
# remain open for as long as it is needed, which is done when using "with" since it acts as an encapsulated context manager.
with open ('newspaper.txt') as json_file:
    newspaper_corps = json.load(json_file)
#run a for loop that looks for the name of the news organization, print it
#run a for loop that looks for the title of the particular news article, print it
#run a for loop that looks for the date of the article, print it
#print the url of the article(s)



#run a machine learning algorithm here...

#add a training set of data for newspaper websites???? Maybe this can be other newspaper topics in the same vein...

#add an optimization method to fine tune learning algorithm such as alpha-beta or markov tree decision. This specifically can contain weight functions as a for loop for accounting for different weight factors.



