#Name: Kalia Hudson
#Date: 12-9-25
#Program Name: Harvestor 3.0
#Program Description: This application is an extension of harvestor a web scrapper.
#This version introduces proxie rotation and image handling while maintaining
#the previous gui from version 2.0.

#File Name: ips.py
#File Description: This file contains proxy IP configurations for requests.

#creating an array of ips.
ips = []

#Function to get a "random" ip
def get_random_ip(index, ips):
    length = len(ips)
    return ips[index % length]


