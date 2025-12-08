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

    return header
    
#FUNCTION - Fetch html (process two)

#FUNCTION - Parse (process three)

#FUNCTION - Extract (process four)
