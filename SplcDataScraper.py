#Title: Simple Scraping Script
#Description: Scrapes the news section of the SPLC's website for the most recent article dates and descriptions.
#Written by: Kingsley Bawuah

from urllib.request import urlopen as uRequest #Importing HTML client
from bs4 import BeautifulSoup as parser #Importing Parsing Library.
myUrl = 'https://www.splcenter.org/news'
dateList = []
counter = 0
x = 0

#Open connection to webpage, read, and close.
uClient = uRequest(myUrl)
pageHtml = uClient.read()
uClient.close()

#HTML "page soup" is stored here.
page_soup = parser(pageHtml, "html.parser")

#Display scraped information.
for link in page_soup.findAll("span", {"class": "date-display-single"}):
    #print(link.get('href'))
    dateList.append(link.get_text())
    counter += 1

for text in page_soup.findAll("p"):
    if x != counter:
        print('\n')
        print(dateList[x])
        print(text.get_text())
        x += 1
        print('\n')

#ISSUES : The dates get out of order when there is a special announcement with no description.