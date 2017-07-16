import requests
import time
import csv
import sys
from bs4 import BeautifulSoup

houses = []

def deletelist():
    houses.clear()


def savefile():
    filename = input("Please input name of file to be saved")        
    with open (filename + '.csv','w') as file:
       writer=csv.writer(file)
       writer.writerow(['Address','Town', 'Price', 'Period'])
       for row in houses:
          writer.writerow(row)
    print("File Saved Successfully")


def appendhouses(scrape):
    houses.append(scrape)

def makesoup(url):
    page=requests.get(url)
    print(url + "  scraped successfully")
    return BeautifulSoup(page.text,"lxml")

def rentalscrape(g_data):
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
            description = item.find_all("p", {"class": "propbox-brief"})[0].text
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
        appendhouses(scrape=[title,town,description,price,period])

def buyscrape(g_data):
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
            description = item.find_all("p", {"class": "propbox-brief"})[0].text
        except:
            pass
        try:
            price = item.find_all("span", {"class": "price-value"})[0].text
        except:
            pass
        appendhouses(scrape=[title,town,description,price])
        
def rent():
    
    search = input("Please enter town")
    soup=makesoup(url = "https://www.propertypal.com/property-to-rent/" + search)
    rentalscrape(g_data = soup.findAll("div", {"class": "propbox-details"}))
    
    button_next = soup.find("a", {"class": "btn paging-next"}, href=True)
    while button_next:
        time.sleep(2)#delay time requests are sent so we don't get kicked by server
        soup=makesoup(url = "https://www.propertypal.com{0}".format(button_next["href"]))
        rentalscrape(g_data = soup.findAll("div", {"class": "propbox-details"}))

        button_next = soup.find("a", {"class" : "btn paging-next"}, href=True)

def buy():
    
    search = input("Please enter town")
    soup=makesoup(url = "https://www.propertypal.com/property-for-sale/" + search)
    buyscrape(g_data = soup.findAll("div", {"class": "propbox-details"}))

    button_next = soup.find("a", {"class": "btn paging-next"}, href=True)
    while button_next:
        time.sleep(2)#delay time requests are sent so we don't get kicked by server
        soup=makesoup(url = "https://www.propertypal.com{0}".format(button_next["href"]))
        buyscrape(g_data = soup.findAll("div", {"class": "propbox-details"}))

        button_next = soup.find("a", {"class" : "btn paging-next"}, href=True)

def menu():
        strs = ('Enter 1 to search Rental Properties\n'
                'Enter 2 to search for Properties to Buy\n'
                'Enter 3 to Exit\n' )
        choice = input(strs)
        return int(choice) 

while True:          #use while True
    choice = menu()
    if choice == 1:
        rent()
        savefile()
        deletelist()
    elif choice == 2:
        buy()
        savefile()
        deletelist()
    elif choice == 3:
        break
