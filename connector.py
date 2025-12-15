#Name: Kalia Hudson
#Date: 12-6-25
#Program Name: Harvestor 3.0
#Program Description: This application is an extension of harvestor a web scrapper.
#This version introduces proxie rotation and image handling while maintaining
#the previous gui from version 2.0.

#File Name: connector.py
#File Description: This file acts as a connector for the front and back end.

import logic.engine as core
import gui.interface as face
from gui.interface import mainWindow
import config.headers as headers
import config.ips as ips
import tkinter as tk

#FUNCTION - Logic Flow
def run_scraper(window):

    #getting request count
    request_count = window.request_count

    #getting list of referrers and user agents
    referers_list = headers.referers
    user_agents_list = headers.user_agents

    #getting list of ips
    ips_list = ips.ips

    #getting assigned referer and user agent
    referer = headers.get_random_referer(request_count, referers_list)
    userAgent = headers.get_random_agent(request_count, user_agents_list)

    #getting header
    hdr = headers.get_header(referer, userAgent)

    #getting proxy (string) and convert to requests' proxies dict
    proxy_ip = ips.get_random_ip(request_count, ips_list)
    proxy = ips.get_proxie_dict(proxy_ip)

    #getting tag
    tag = face.get_tag(window)

    #getting url
    url = face.get_url(window)
    #validating 
    if not url.startswith("http"):
        url = "http://" + url
    ###TEST
    print("Validated URL:", url)
    
    #running process one - fetching html
    raw_html = core.fetch_html(url, headers=hdr, proxy=proxy)

    #checking if html was fetched successfully
    if raw_html:

        #running process two - parsing html
        site_soup = core.parse_html(raw_html)

        #running process three - extracting elements
        extracted_data = core.extract_elements(site_soup, tag)

        #TEST
        print("Extracted Data:", extracted_data)
    else:
        #print error message
        print("Failed to retrieve HTML content.")

    #incrementing request count
    window.request_count += 1

    ###TEST
    print("Run_scraper called successfully")


#FUNCTION - Handle submit button
def on_submit(window):  
    ####TEST  
    print("on_submit called")

    run_scraper(window)

#FUNCTION - Handle export button
def on_export(window):
    ###TEST
    print("on_export called")

#create an instance of the mainWindow class from interface.py
active_window = mainWindow()

#creating an attribute to hold request count
active_window.request_count = 0

#binding the submit and export buttons
active_window.buttonSubmit.config(command=lambda: on_submit(active_window))
active_window.buttonExport.config(command=lambda: on_export(active_window))

#running the window
active_window.run()

