import requests
import time
import csv
import sys
from bs4 import BeautifulSoup

houses = []

url = "https://www.propertypal.com/property-to-rent/newtownabbey/"
page=requests.get(url)
soup=BeautifulSoup(page.text,"lxml")
g_data = soup.findAll("div", {"class": "propbox-details"})
for item in g_data:
    try:
        title = item.find_all("span", {"class": "propbox-addr"})[0].text
    except:
        pass
    try:
        town = item.find_all("span", {"class": "propbox-town"})[0].text
    except:
        pass
    try:
        price = item.find_all("span", {"class": "price-value"})[0].text
    except:
        pass
    try:
        period = item.find_all("span", {"class": "price-period"})[0].text
    except:
        pass
    course=[title,town,price,period]
    houses.append(course)
        

for i in range(1,10):
    time.sleep(5)#delay time requests are sent so we don't get kicked by server
    url2 = "https://www.propertypal.com/property-to-rent/newtownabbey/page-{0}".format(i)
    page2=requests.get(url2)
    soup=BeautifulSoup(page2.text,"lxml")
    g_data = soup.findAll("div", {"class": "propbox-details"})
    for item in g_data:
        try:
            title = item.find_all("span", {"class": "propbox-addr"})[0].text
        except:
            pass
        try:
            town = item.find_all("span", {"class": "propbox-town"})[0].text
        except:
            pass
        try:
            price = item.find_all("span", {"class": "price-value"})[0].text
        except:
            pass
        try:
            period = item.find_all("span", {"class": "price-period"})[0].text
        except:
            pass
        
        course=[title,town,price,period]
        houses.append(course)

        
with open ('newtownabbeyrentalproperties.csv','w') as file:
   writer=csv.writer(file)
   writer.writerow(['Address','Town', 'Price', 'Period'])
   for row in houses:
      writer.writerow(row)

        
        
        