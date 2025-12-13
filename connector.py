#Name: Kalia Hudson
#Date: 12-6-25
#Program Name: Harvestor 3.0
#Program Description: This application is an extension of harvestor a web scrapper.
#This version introduces proxie rotation and image handling while maintaining
#the previous gui from version 2.0.

#File Name: connector.py
#File Description: This file acts as a connector for the front and back end.

#Creating a variable to hold the number of requests made
request_count = 0

import logic.engine as core
import gui.interface as face
from gui.interface import mainWindow
import config.headers as headers
import config.ips as ips
import tkinter as tk

#FUNCTION - Logic Flow
def run_scraper(window, request_count):
    ###TEST
    print("Run_scraper called")

#FUNCTION - Handling submit button
def on_submit(window):  
    ####TEST  
    print("on_submit called")

#FUNCTION - handling export button
def on_export(window):
    ###TEST
    print("on_export called")

#creating an instance of the mainWindow class from interface.py
active_window = mainWindow()

#running the window
active_window.run()

