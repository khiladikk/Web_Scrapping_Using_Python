#import the library used to query a wesite
import urllib2


#Impoort the Beautiful soup functions to parse the data returned from the website 
from bs4 import BeautifulSoup


#Specify the url
url= "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"


#Query the website and return the html to variable 'page'
page= urllib2.urlopen(url)


#Parse the html in 'page' variable, and store it in Beautiful Soup Format 
html = BeautifulSoup(page, "lxml")

table = html.find('table',{'class':'table'})

print table


#Generate Lists
A,B,C,D= [],[],[],[]

for row in table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
       
#Import pandas to convert list to data frame       
import pandas as pd
from collections import OrderedDict

team_ranking = ["Team","Matches","Points","Rating"]

ranking_data = OrderedDict(zip(team_ranking,[A,B,C,D]))

data = pd.DataFrame(ranking_data) 

print data
