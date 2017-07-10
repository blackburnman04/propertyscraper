import requests
import time
import csv
import sys
from bs4 import BeautifulSoup

houses = []
# first page doesnt use page- string in url or had to do this separately for first page and add results to the same list that will contain the paginated results
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
        

button_next = soup.find("a", {"class": "btn paging-next"}, href=True) # used for looping through pages pagination. Better than previous range solution which was limited to certain page numbers
while button_next: # while loop for pagination
    time.sleep(2)#delay time requests are sent so we don't get kicked by server
    url2 = "https://www.propertypal.com{0}".format(button_next["href"]) # added page number string to link e.g /page-3
    page2=requests.get(url2)
    print(url2)
    soup=BeautifulSoup(page2.text,"lxml")
    g_data = soup.findAll("div", {"class": "propbox-details"})
    for item in g_data:
        try:
            title = item.find_all("span", {"class": "propbox-addr"})[0].text # scrape address
        except:
            pass
        try:
            town = item.find_all("span", {"class": "propbox-town"})[0].text # scrape town
        except:
            pass
        try:
            price = item.find_all("span", {"class": "price-value"})[0].text # scrape price
        except:
            pass
        try:
            period = item.find_all("span", {"class": "price-period"})[0].text # scrape period of payment e.g weekly/monthly
        except:
            pass
        
        course=[title,town,price,period] # puts scraped values in list
        houses.append(course) 

        button_next = soup.find("a", {"class" : "btn paging-next"}, href=True)

        
with open ('newtownabbeyrentalproperties.csv','w') as file: # output scraped data to csv file
   writer=csv.writer(file)
   writer.writerow(['Address','Town', 'Price', 'Period'])
   for row in houses:
      writer.writerow(row)

        
        
        
