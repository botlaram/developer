##extracting the data from https://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
response=requests.get(url)

soup = BeautifulSoup(response.text,"html")   ##response.txt prints urls inspect
print(soup)

quotes=soup.find_all("span",class_="text") ##(<span> is tag and class_ is class name present in url inspect)
print(quotes)

##to print quotes 
for lines in quotes:
    print(lines.text)
    
##find all author name
authors=soup.find_all("small",class_="author") ##(<small> is tag and class_ is class name present in url inspest)

##find all author tags mentioned in url
tags=soup.find_all("div",class_="tags")

##print all details
for i in range(0,len(quotes)):
    print("\n",quotes[i].text)
    print(authors[i].text)
    author_tag=tags[i].find_all("a",class_="tag")  ##(<a> tag present inside <div> tag line 23)
    for i in range(0,len(author_tag)):
        print(author_tag[i].text)