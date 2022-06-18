import time
import requests
import shutil

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

tags = input("Enter the tags: ")
tag_list = tags.split(" ")

all_urls = []
number = 0

serv = Service("PATH_TO_GECKO_WEBDRIVER")

driver = webdriver.Firefox(service = serv)

for tag in tag_list:

    print("Searching for tag #" + tag)

    driver.get("https://www.instagram.com/explore/tags/" + tag)
    time.sleep(10)

    images = driver.find_elements(By.CLASS_NAME, "_aagt")

    print("Total Results found for #" + tag + " : " + str(len(images)))

    for image in images:
        url = image.get_attribute('src')
        all_urls.append(str(url))

    try:
        for i in range(len(all_urls)):
            file_name = "Image-" + str(i+number) + ".jpg"
            res = requests.get(all_urls[i+number], stream = True)

            if res.status_code == 200:
                with open(file_name, "wb") as f:
                    shutil.copyfileobj(res.raw, f)
            else:
                print("Download failed for " + file_name + ".")
    except:
        print("Oops! Something went wrong.")
    
    number = number + len(images)

driver.quit()
