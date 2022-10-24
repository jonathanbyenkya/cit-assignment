# 1. Scrape CBS news https://www.cbsnews.com/latest/world/ and get the following data

# Title
# Link
# Image
# description
# Using SqlAlchemy create a table called cbs_news and insert the data into the table.

# Implement one route called /cbs_news that returns the data in json format.

import json 
from bs4 import BeautifulSoup
import requests
from sqlalchemy import text, engine 
import xml
from flask import Blueprint, request, redirect, render_template

cbviews = Blueprint('cbviews', __name__)

def get_cbs_news():
    url = 'https://www.cbsnews.com'
    response = requests.get(url)

    data = []

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())


    first_row = soup.find_all('div', class_ = 'item__title-wrapper')
    # print(first_row)

# get_cbs_news()

    
    title = first_row.find('h4', class_ = 'item__hed').text
    link = first_row.find('article', class_ = 'item  item--type-article item--topic lazyloaded').find('a')['href']
    print(link)
    image = first_row.find('span', class_ = 'img item__thumb item__thumb--crop-0').find('img')['src']
    description = first_row.find('p', class_ = 'item__dek').text

    data.append({
        'title': title,
        'link': link,
        'image': image,
        'description': description,
    })
    print(data)


get_cbs_news()

@cbviews.route('/cbnews', methods=['GET', 'POST'])
def cbsnews():
    if request.method == 'POST':
        return redirect('/')

    #new data from cbs news
    data = get_cbs_news()

    #existing data from database
    cbnews = cbsnews.get_all_news()

    #loop through the data 