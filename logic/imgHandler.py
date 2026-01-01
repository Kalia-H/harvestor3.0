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
from tkinter import filedialog
import os

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
        # Try to get the src attribute (for Tag objects) otherwise treat img as a URL string
        src = None
        if hasattr(img, 'get'):
            src = img.get('src')
        else:
            src = str(img).strip()
            if not src:
                no_src_count += 1
                continue

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

    this_image = requests.get(img_urls, headers=headers, proxies=proxy, timeout=10)

    return this_image

#Function - Save images to disk
def saveImages(images):
    #Ask user where to save images
    save_directory = filedialog.askdirectory(title="Select Directory to Save Images")

    if not save_directory:
        print("No directory selected. Aborting save operation.")
        return

    os.makedirs(save_directory, exist_ok = True)
     
    for img in images:
        #TEST
        print("Saving image..")
        
        ###Determine image name

        #count images to create unique names
        imageCount = 1

        #convert count to string
        imageCount = str(imageCount)

        #create image name
        imageName = "image_" + imageCount

        #create full path
        full_path = os.path.join(save_directory, imageName + ".jpg")

        #write image to disk
        with open(full_path, 'wb') as f:
            f.write(img)




        
