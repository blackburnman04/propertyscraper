import requests
import time
import csv
import sys
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image


path = "propertypal.jpg" # image file name for logo to be displayed in root window (must be in same directory as running script)


houses = []

# Code to delete previous scraped data from list, so previously scraped data isn't present in new scraped data


def deletelist():
    houses.clear()


def gui_input(prompt):

    root = tk.Toplevel()
    # this will contain the entered string, and will
    # still exist after the window is destroyed
    var = tk.StringVar()

    # create the GUI
    label = tk.Label(root, text=prompt)
    entry = tk.Entry(root, textvariable=var)
    label.pack(side="left", padx=(20, 0), pady=20)
    entry.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # Let the user press the return key to destroy the gui
    entry.bind("<Return>", lambda event: root.destroy())

    # this will block until the window is destroyed
    root.wait_window()

    # after the window has been destroyed, we can't access
    # the entry widget, but we _can_ access the associated
    # variable
    value = var.get()
    return value


# Display a string in `out_label`
def print_to_gui(text_string):
    status_label.config(text=text_string)
    # Force the GUI to update
    root.update()
    
    

    # Output scraped data to CSV


def savefile():
    filename = gui_input("Please input name of file to be saved")
    with open (filename + '.csv','w') as file:
       writer=csv.writer(file)
       writer.writerow(['Address','Town', 'Price', 'Period'])
       for row in houses:
          writer.writerow(row)
    print_to_gui("CSV File Saved Successfully")


    
    # Append scraped data to list called houses to be outputted to CSV

def appendhouses(scrape):
    houses.append(scrape)

    # Code to being scraping urls

    
def makesoup(url):
    page=requests.get(url)
    print_to_gui(url + "  scraped successfully")
    return BeautifulSoup(page.text,"lxml")

# Code to perform rental property scrape from Propertypal


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

        
# Code to perform sale property scrape from Propertypal
        
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
        
# Code for rental properties scrape

def rent():

    search = gui_input("Please enter town")
    soup=makesoup(url = "https://www.propertypal.com/property-to-rent/" + search)
    rentalscrape(g_data = soup.findAll("div", {"class": "propbox-details"}))

    button_next = soup.find("a", {"class": "btn paging-next"}, href=True)
    while button_next:
        time.sleep(2)#delay time requests are sent so we don't get kicked by server
        soup=makesoup(url = "https://www.propertypal.com{0}".format(button_next["href"]))
        rentalscrape(g_data = soup.findAll("div", {"class": "propbox-details"}))

        button_next = soup.find("a", {"class" : "btn paging-next"}, href=True)
    savefile()
    deletelist()
    
# Code for sale properties scrape

def buy():

    search = gui_input("Please enter town")
    soup=makesoup(url = "https://www.propertypal.com/property-for-sale/" + search)
    buyscrape(g_data = soup.findAll("div", {"class": "propbox-details"}))

    button_next = soup.find("a", {"class": "btn paging-next"}, href=True)
    while button_next:
        time.sleep(2)#delay time requests are sent so we don't get kicked by server
        soup=makesoup(url = "https://www.propertypal.com{0}".format(button_next["href"]))
        buyscrape(g_data = soup.findAll("div", {"class": "propbox-details"}))

        button_next = soup.find("a", {"class" : "btn paging-next"}, href=True)
    savefile()
    deletelist()


def quit():
    root.quit()
    
# GUI Code Tkinter

root = tk.Tk()
root.resizable(False, False)
root.geometry("600x600")
root.wm_title("Property Pal- Rental and Sale Property Search")
Label = tk.Label(root, text = 'Property Pal\n Search Rental and Sale Properties', font = ('Comic Sans MS',18))
button = tk.Button(root, text="Search Rental", command=rent)
button2 = tk.Button(root, text="Search For Sale", command=buy)
button3 = tk.Button(root,  text = "Quit Program", command=quit)
Label.pack()
button.pack()
button2.pack()
button3.pack()
status_label = tk.Label(text="")
status_label.pack()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()

