#Name: Kalia Hudson
#Date: 12-16-25
#Program Name: Harvestor 3.0
#Program Description: This application is an extension of harvestor a web scrapper.
#This version introduces proxie rotation and image handling while maintaining
#the previous gui from version 2.0.

#File Name: imgHandler.py
#File Description: This file handles image downloading and saving.

from urllib.parse import urljoin
import requests

#Function - Get image URLs
def get_image_urls(extracts, base_url):

    #create an array to store image urls
    img_urls = []

    #store the count of images which have no src attribute
    no_src_count = 0

    #store the count of images processed
    processed_count = 0

    #loop through extracted elements
    for img in extracts:
       #get the src attribute aka image url
       src = img.get('src')
       if src:
           #construct full url
           full_url = urljoin(base_url, src)
           img_urls.append(full_url)
           processed_count += 1
       else:
           #increment no src count
            no_src_count += 1

    #TEST
    print(f"Images with no src attribute: {no_src_count}")
    print(f"Total images processed: {processed_count}")

    return img_urls

#Function - Download and save images
def download_and_save_images(img_urls, headers, proxy):
    print("Starting image download...")
