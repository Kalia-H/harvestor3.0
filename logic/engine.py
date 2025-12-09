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

#FUNCTION - Get header (process one)
def get_header(referer, userAgent):
    header = {
        "Accept": "application/json, text/html, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": referer,
        "User-Agent": userAgent
    }
    ###TEST
    print("Process one called")

    return header
    
#FUNCTION - Fetch html (process two)
    def fetch_html(url, headers, proxy):
        status = response.status_code
        if(status != 200):
            print("Error: Unable to fetch the webpage.")
        else:
            response = requests.get(url, headers=headers, proxies=proxy)
            return response.text
        
    ###TEST
    print("Process two called")
        
#FUNCTION - Parse (process three)
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')

    ###TEST
    print("Process three called")
    return soup
#FUNCTION - Extract (process four)
