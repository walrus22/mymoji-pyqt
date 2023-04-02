import os
import time
import imghdr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import requests

options = Options()
# options.add_argument("--window-size=1920,1080") # for chrome
# options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--disable-gpu")    
options.add_argument("--no-sandbox")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

path_dc = './DC'

# try:
for id in range(116223,1200000):
    driver.get("https://dccon.dcinside.com/new/1#" + str(id))
    time.sleep(2)
    icons = driver.find_elements(By.XPATH, "//span[@class='img_dccon']")
    
    # check empty id
    if icons == []:
        print(str(id) + " is empty")
    else :
        print(str(id) + " is exist")        
        
        # mkdir save folder
        path_icon = os.path.join(path_dc, str(id))
        if os.path.exists(path_icon) == False:
            os.mkdir(path_icon)
        
        # save icon info
        info_date = driver.find_element(By.XPATH, "//span[@class='makeday']").text
        infos = driver.find_elements(By.XPATH, "//span[@class='seller_name']")
        info_creator = infos[0].text.replace(",", "")
        info_tag = infos[1].text.replace(" ,", ",").replace(", ", ",")
        info_txt = "creator: " + info_creator + "\ncreation date: " + info_date + "\ntag: " + info_tag + "\nplatform: dcinside"
        
        with open(os.path.join(path_icon, 'readme.txt'), 'w') as f:
            f.write(info_txt)   
        
        # index for icon
        i = 0
            
        for icon in icons:
            img = icon.find_element(By.XPATH, "./img")
            img_url = img.get_attribute("src")
            img_data = requests.get(img_url).content
            img_type = imghdr.what("", img_data)
            i += 1            
            
            with open(os.path.join(path_icon, str(id) + "_" + str(i) + "." + img_type), 'wb') as handler:
                handler.write(img_data)
        
            
# except Exception as e:
#     print(e)




