#Name: Kalia Hudson
#Date: 12-16-25
#Program Name: Harvestor 3.0
#Program Description: This application is an extension of harvestor a web scrapper.
#This version introduces proxie rotation and image handling while maintaining
#the previous gui from version 2.0.

#File Name: imgHandler.py
#File Description: This file handles image downloading and saving.

from urllib.parse import urljoin

#Function - Get image URLs
def get_image_urls(extracts, base_url):

    #create an array to store image urls
    img_urls = []

    #store the count of images which have no src attribute
    no_src_count = 0

    #loop through extracted elements
    for img in extracts:
       src = img.get('src')
       if src:
           full_url = urljoin(base_url, src)
           img_urls.append(full_url)
       else:
           #increment no src count
            no_src_count += 1

    print(f"Images with no src attribute: {no_src_count}")
    return img_urls