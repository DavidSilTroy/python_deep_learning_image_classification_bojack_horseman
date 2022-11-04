from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import json
import os
import time


cast = {
    'bojack' : 'bojack horseman',
    'carolyn' : 'princess carolyn ',
    'diane' : 'diane nguyen',
    'peanutbutter' : 'mr. peanutbutter',
    'todd' : 'todd chavez',
}


def search_at_bing(search, to_folder):
    """This code was modified 
    by David Silva Troya, but 
    the real one was here: 
    https://stackoverflow.com/questions/64226325/is-there-a-way-i-can-download-images-from-any-search-engine-with-a-code-like-thi """
    
    # search = input("Search for: ")
    
    url = "https://www.bing.com/images/search"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }
    params = {"q": search, "form": "HDRSC2", "first": "1", "scenario": "ImageBasicHover"}
    r = requests.get(url, headers=headers, params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("div", {"class": "img_cont hoff"})

    for data in soup.find_all("a", {"class": "iusc"}):
        json_data = json.loads(data["m"])
        img_link = json_data["murl"]
        img_object = requests.get(img_link, headers=headers)
        title = img_link.split("/")[-1]

        # print("Getting: ", img_link)
        # print("Title: ", title + "\n")
        try:
            img = Image.open(BytesIO(img_object.content))
            img_path =f'./photos/{to_folder}/' 
            if not os.path.exists(img_path):
                os.makedirs(img_path)
                print(f'folder created for {to_folder}')
            img.save(img_path + title)
        except:
            print(f'Not Possible to download one image')


if __name__ == '__main__':
    cast_list = list(cast)
    print(f'From the option in {cast_list}')
    character = ""
    while True:
        number = input(f'Select a number from 0 to {len(cast_list)-1}: \n')
        try:
            number = int(number)
            if number>=len(cast_list) or number<0:
                print('Wrong number')
            else:
                character = cast_list[number]
                break
        except:
            print(f'Please, write a number of the list')
    
    print(f'from {character}:')
    search_at_bing(cast[character],character)
    search_at_bing(f'{cast[character]} happy',character)
    search_at_bing(f'{cast[character]} sad',character)
    search_at_bing(f'{cast[character]} only',character)
    search_at_bing(f'{cast[character]} normal',character)
    search_at_bing(f'{cast[character]} season 1',character)
    search_at_bing(f'{cast[character]} season 2',character)
    search_at_bing(f'{cast[character]} season 3',character)
    search_at_bing(f'{cast[character]} season 4',character)
    search_at_bing(f'{cast[character]} season 5',character)
    # print(key_list)
    # keys_of_interest = ['test2', 'test3']

    # for key in keys_of_interest:
    #     print('key: {}, index: {}'.format(key, key_list.index(key)))






### Some other code that I was trying:


# # -*- coding: utf-8 -*-
# """
# Created on Sun Jul 12 11:02:06 2020
# @author: OHyic
# """
# #Import libraries
# import os
# import concurrent.futures
# from GoogleImageScraper import GoogleImageScraper
# from patch import webdriver_executable


# def worker_thread(search_key):
#     image_scraper = GoogleImageScraper(
#         webdriver_path, image_path, search_key, number_of_images, headless, min_resolution, max_resolution)
#     image_urls = image_scraper.find_image_urls()
#     image_scraper.save_images(image_urls, keep_filenames)

#     #Release resources
#     del image_scraper

# if __name__ == "__main__":
#     #Define file path
#     webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
#     image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

#     #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
#     search_keys = list(set(["cat", "t-shirt"]))

#     #Parameters
#     number_of_images = 5                # Desired number of images
#     headless = True                     # True = No Chrome GUI
#     min_resolution = (0, 0)             # Minimum desired image resolution
#     max_resolution = (9999, 9999)       # Maximum desired image resolution
#     max_missed = 1000                   # Max number of failed images before exit
#     number_of_workers = 1               # Number of "workers" used
#     keep_filenames = False              # Keep original URL image filenames

#     #Run each search_key in a separate thread
#     #Automatically waits for all threads to finish
#     #Removes duplicate strings from search_keys
#     with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
#         executor.map(worker_thread, search_keys)



#########################################################

# import requests
# from bs4 import BeautifulSoup
# import os

# #url = 'https://www.airbnb.co.uk/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2020-11-01&checkout=2020-11-08&source=structured_search_input_header&search_type=autocomplete_click'

# def imagedown(url, folder):
#     try:
#         os.mkdir(os.path.join(os.getcwd(), folder))
#     except:
#         pass
#     os.chdir(os.path.join(os.getcwd(), folder))
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     images = soup.find_all('img')
#     for image in images:
#         name = image['alt']
#         link = image['src']
#         with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
#             im = requests.get(link)
#             f.write(im.content)
#             print('Writing: ', name)

# imagedown('https://www.airbnb.co.uk/s/Bratislava--Slovakia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJl2HKCjaJbEcRaEOI_YKbH2M&query=Bratislava%2C%20Slovakia&checkin=2020-11-01&checkout=2020-11-22&source=search_blocks_selector_p1_flow&search_type=search_query', 'bratislava')






# import os
# import requests
# from bs4 import BeautifulSoup

# # url = "https://www.airbnb.co.uk/s/Bratislava--Slovakia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJl2HKCjaJbEcRaEOI_YKbH2M&query=Bratislava%2C%20Slovakia&checkin=2020-11-01&checkout=2020-11-22&source=search_blocks_selector_p1_flow&search_type=search_query"
# url = "https://www.google.com/search?q=bojack+horseman+bojack&hl=es-419&sxsrf=ALiCzsadxQd1O2cCS7bvp0SDGaKqETwgXg:1667400531310&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjWufeC34_7AhXBzKQKHZcYC6wQ_AUoAXoECAEQAw&biw=1920&bih=933&dpr=1"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, 'html.parser')

# images = soup.find_all('img')

# for image in images:
#     # img_name = image['alt']
#     img_link = image['src']
#     print(f'::: {img_link} :::: {image}')


##########################################################################


# import requests
# from bs4 import BeautifulSoup

# params = {
#     "q": "batman wallpaper",
#     "tbm": "isch", 
#     "content-type": "image/png",
# }

# html = requests.get("https://www.google.com/search", params=params)
# soup = BeautifulSoup(html.text, 'html.parser')

# for img in soup.select("img"):
#   print(img["src"])


##########################################################################




# import requests
# # URL = "https://www.google.com/search?q=bojack+horseman+bojack&tbm=isch&ved=2ahUKEwjDg4bP4Y_7AhVmkP0HHVEzBtYQ2-cCegQIABAA&oq=Bojack&gs_lcp=CgNpbWcQARgAMgQIIxAnMgQIIxAnMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgAEENQ-AhY2BRgnhtoAHAAeACAAU-IAcsDkgEBN5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=C4ZiY4PSMOag9u8P0eaYsA0"
# URL = "https://www.bing.com/images/search?q=bojack+horseman+bojack&form=HDRSC3&first=1&tsc=ImageHoverTitle"
# page = requests.get(URL)


# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# image_tags = soup.find_all('img')
# links = []
# for image_tag in image_tags:
#     links.append(image_tag['src'])

# print(links)
# # import urllib.request
# # urllib.request.urlretrieve(links[0], "images/innovators.jpg")





##################################################



# #!/usr/bin/env python3
# from bs4 import BeautifulSoup
# import requests
# import re
# import sys
# import os
# import http.cookiejar
# import json
# import urllib.request, urllib.error, urllib.parse

# def get_soup(url,header):
#     #return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),
#     # 'html.parser')
#     return BeautifulSoup(urllib.request.urlopen(
#         urllib.request.Request(url,headers=header)),
#         'html.parser')

# query = sys.argv[1]
# query= query.split()
# query='+'.join(query)
# url="http://www.bing.com/images/search?q=" + query + "&FORM=HDRSC2"

# #add the directory for your image here
# DIR="Pictures"
# header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
# soup = get_soup(url,header)

# ActualImages=[]# contains the link for Large original images, type of  image
# for a in soup.find_all("a",{"class":"iusc"}):
#     #print a
#     #mad = json.loads(a["mad"])
#     #turl = mad["turl"]
#     m = json.loads(a["m"])
#     murl = m["murl"]

#     image_name = urllib.parse.urlsplit(murl).path.split("/")[-1]
#     print(image_name)

#     ActualImages.append((image_name, turl, murl))

# print("there are total" , len(ActualImages),"images")

# if not os.path.exists(DIR):
#     os.mkdir(DIR)

# DIR = os.path.join(DIR, query.split()[0])
# if not os.path.exists(DIR):
#     os.mkdir(DIR)

# ##print images
# for i, (image_name, turl, murl) in enumerate(ActualImages):
#     try:
#         #req = urllib2.Request(turl, headers={'User-Agent' : header})
#         #raw_img = urllib2.urlopen(req).read()
#         #req = urllib.request.Request(turl, headers={'User-Agent' : header})
#         raw_img = urllib.request.urlopen(turl).read()

#         cntr = len([i for i in os.listdir(DIR) if image_name in i]) + 1
#         #print cntr

#         f = open(os.path.join(DIR, image_name), 'wb')
#         f.write(raw_img)
#         f.close()
#     except Exception as e:
#         print("could not load : " + image_name)
#         print(e)


###################################################################

# import requests
# from bs4 import BeautifulSoup

# seartext = input("enter the search term: ")
# count = input("Enter the number of images you need:")

# adlt = 'off' # can be set to 'moderate'

# sear=seartext.strip()

# sear=sear.replace(' ','+')

# URL='https://bing.com/images/search?q=' + sear + '&safeSearch=' + adlt + '&count=' + count

# print('.......')
# print(URL)
# print('.......')

# USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# headers = {"user-agent": USER_AGENT}
# resp = requests.get(URL, headers=headers)
# results=[]
# soup = BeautifulSoup(resp.content, "html.parser")
# # print(soup)
# print('.......')
# wow = soup.find_all('a',class_='iusc')
# for i in wow:
#     try:
#         print(eval(i['m'])['murl'])
#         print()
#     except:
#         pass



####################################################################

