'''
This program will crawl flight information from Miles & More website to determine if countries are continental or not.
'''

#import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random

#set up the url
url = 'https://www.miles-and-more.com/row/en/program/status-benefits/new-statusprogramme/status-achievement.html'

#set up the header
headers = {'User-Agent': 'Mozilla/5.0'}

#set up the request
response = requests.get(url, headers=headers)

#set up the soup
soup = BeautifulSoup(response.text, 'html.parser')

#find the table

