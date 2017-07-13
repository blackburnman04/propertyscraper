# Property Rentals and Sales Scraper
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

You will be prompted with a Command Line menu containing three options:

1. Rental Properties
2. Sale Properties
3. Exit

Enter a number depending on what you want to do 

If you select 1 or 2 you will be prompted with a message asking to input town.

Input the town you would like to search for Rental or Properties to Buy e.g. Newtownabbey

The scraper will then scrape data from PropertyPal.com for the town/area you entered. (URLs for each page being scraped will be displayed in the terminal, with scraped successfully beside them).

One scraping is completed, you will be prompted with a message stating to "Enter a filename to save". Enter a filename here, e.g. NewtownabbeyRentals.

Once entered, a .csv file will be created in the directory where this script is present. The .csv file will be called whatever name you entered when prompted to enter file name.

The scraped data will be oontained within this file.


Work to be done:

- I need to add an error message for when a request to scrape is not successful. At the moment, if scraping is not successful, it will still prompt for filename to be entered, but when it is entered an empty .csv file is created. I will fix this soon.

