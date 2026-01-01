#Name: Kalia Hudson
#Date: 12-7-25
#Program Name: Harvestor 3.0
#Program Description: This application is an extension of harvestor a web scrapper.
#This version introduces proxie rotation and image handling while maintaining
#the previous gui from version 2.0.

#File Name: engine.py
#File Description: This file handles the web scraper logic

import requests
from bs4 import BeautifulSoup
  
#FUNCTION - Fetch html (process one)
def fetch_html(url, headers, proxy):
    try:
        response = requests.get(url, headers=headers, proxies=proxy)
    except requests.RequestException as e:
        print("Error: Unable to fetch the webpage.", e)
        return None

    status = response.status_code
    if status != 200:
        print(f"Error: Received status code {status}")
        return None

    ###TEST
    print("Process two called")
    return response.text
        
#FUNCTION - Parse (process two)
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')

    ###TEST
    print("Process three called")
    return soup

#FUNCTION - Extract (process three)
def extract_elements(soup, tag):
    elements = soup.find_all(tag)

    if tag.lower() == 'img':
        data_extracts = elements
    else:
        data_extracts = []

        for element in elements:
            text = element.get_text() if hasattr(element, 'get_text') else str(element)
            data_extracts.append(text.strip())

    return data_extracts
