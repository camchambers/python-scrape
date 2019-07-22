# An example of scraping web pages with python using the BeautifulSoup library

# Used for making HTTP requests
import requests

# Used for scraping web pages
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://en.wikipedia.org/wiki/Monkey'

# Connect to the URL
response = requests.get(url)

# # Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

#Scrape content div
contentDiv = soup.find('div', {'id': 'bodyContent'}).findAll('p')

print(contentDiv[1].text)