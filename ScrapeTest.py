import urllib
import csv
import requests

wordsfile = csv.DictReader(open("words.csv"))


#links = ['http://econpy.pythonanywhere.com/ex/001.html','http://www.itrade4profit.in/showscripfca0.htm?sym=APCOTEXIND']

#Search for every word in the words list in every URL in the links list. Print both word and the URL if found

for word in wordsfile:
        curr_word = word['search_word']

        linksfile = csv.DictReader(open("links.csv"))

        for link in  linksfile:
                curr_link = link['url']
                site = urllib.urlopen(curr_link).read()

                if curr_word in site:
                        print(curr_word, " Present in", curr_link)
