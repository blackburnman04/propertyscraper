# NI Property Rentals and Sales Scraper
Python 3 &amp; BeautifulSoup4 scraper which scrapes details about current rental and sale properties in Northern Ireland (Scraped from PropertyPal.com)

Dependencies:

-Python 3
-Beautifulsoup4

Imports Needed:

- Requests
- Time
- CSV

How to Use:

Run the Script, e.g. via Linux in Terminal 

python /home/directory/scraper.py

A GUI like the one in the image below will be displayed:

![alt tag](https://image.ibb.co/cBQsUG/Screenshot_20180124_021432.png)

Click on the button for the option you would like. The current options are:

1. Search Rental Properties
2. Search Sale Properties

Once your choice button has been clicked, you will be prompted to enter a town, you can enter the town by name, e.g. Newtownabbey, or the first four characters of the postcode (e.g. BT14). After this has been entered press the Enter button.

Once the enter button has been pressed, scraping will begin. The URL of the page being scraped from the PropertyPal is displayed under the third button (just above the PropertyPal logo). 

Once scraping has been completed, you will be prompted to enter a filename for the .csv file to be called that will contain the scraped data. Enter this filename and press the enter button.

Once entered, a .csv file will be created in the directory where this script is present. The .csv file will be called whatever name you entered when prompted to enter file name.

The scraped data will be oontained within this file.

The label that contained information on the URL being scraped should now state "CSV File Saved Successfully".


Work to be done:

- I need to add an error message for when a request to scrape is not successful. At the moment, if scraping is not successful, it will still prompt for filename to be entered, but when it is entered an empty .csv file is created. I will fix this soon.

