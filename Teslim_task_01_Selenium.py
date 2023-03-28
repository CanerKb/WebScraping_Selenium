import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time    # 21.ve 22. kod satirini durdurur!
# selenium u kullan bekletmede.

service = Service(executable_path="./chromedriver.exe")
# Driver'i gizli sekmede acmak icin.
# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument("--incognito") # Driver'i gizli sekmede acmak icin.
# chromeOptions.add_argument("--headless") # pencereyi acmaz.
# driver = webdriver.Chrome(chromeOptions= chromeOptions)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://phishtank.org")
# phishtank web sitesine giris yaptiktan sonra. "See more suspected phishes..." tiklanir
    # ve tum seceneklere ait phising'ler sayfada acilir.
driver.find_element(By.XPATH, "//div/p/a[@href='phish_search.php?verified=u&active=y']").click()
# "See all submissions in the phish archive" tiklanarak tum phising siteleri goruntuleniyor.
driver.find_element(By.XPATH, "//div/p/a[contains(text(), 'See all')]").click()
# tum bu islemlerden sonra 1 sn. selenium bekletiliyor.
time.sleep(1)
# driver.implicitly_wait(1) # 1sn beklemesini bu sekilde de ayarlayabilir.
def web_elements_get_Append():
    phising_url_name = driver.find_elements(By.XPATH, "//table/tbody//tr//td[contains(text(), '://')]")      # //table/tbody//tr//td[contains(text(), '://') # //table/tbody//tr//td[contains(text(), '://')]
    for phising in phising_url_name:
        phising_list_selenium.append(phising.text)

def older():
    driver.find_element(By.XPATH, "//table/tbody/tr/td/b/a[contains(text(), 'Older')]").click()    #  # //table/tbody/tr/td/b/a[contains(text(), 'Older')]


# BASARILI
# total_phising_selenium = 0
# phising_list_selenium = []
# while True:
#     phising_url_name = driver.find_elements(By.XPATH, "//table/tbody//tr//td[contains(text(), 's://')]")
#     for phising in phising_url_name:
#         phising_list_selenium.append(phising.text)
#     if "18th" in phising_list_selenium[-1]:
#         break
#     else:
#         older()
#         time.sleep(1)
#         web_elements_get_Append()
#         total_phising_selenium +=1
# print(total_phising_selenium)
# driver.quit()


# # str olusturma


total_phising_selenium = 0
phising_str_selenium_name = ""
phising_str_selenium_date = ""
while True:
    phising_url_name = driver.find_elements(By.XPATH, "//table/tbody//tr//td[contains(text(), '://')]")    # tekrar find de.  # //table/tbody//tr//td[contains(text(), '://')] # //table/tbody//tr//td[contains(text(), '://')]
    phising_url_date = driver.find_elements(By.XPATH, "//table/tbody//tr//td/span[contains(text(), 'added')]")
    for phising_name in phising_url_name:
        phising_str_selenium_name= phising_str_selenium_name + ' ' + phising_name.text
    for phising_date in phising_url_date:
        phising_str_selenium_date= phising_str_selenium_date + phising_date.text
    if "AM" in phising_str_selenium_date:
        break
    else:
        older()
        time.sleep(1) # selenium kullan
        web_elements_get_Append()
        total_phising_selenium +=1
print(total_phising_selenium)
driver.quit()

import pandas as pd
import numpy as np

def dataframe_phising_tablo(phising_str_selenium_name):
    df_ = pd.DataFrame(phising_str_selenium_name.split(sep=" "))
    df_url_ham = df_.iloc[1:-1:7]
    df_url_ham.index = np.arange(0, len(df_url_ham))
    new_url = ""
    for value in df_url_ham.values:
        new_url = new_url + ' ' +value[0][0:-6]
    new_url= new_url.strip().split(" ")
    df_url = pd.DataFrame(new_url)
    df_url.columns= ['Phising_URL']
    return df_url
df_url.tail()
# df_url.tail()
#                                            Phising_URL
# 193  https://43.134.167.94/v3/signin/identifier?dsh...
# 194  https://129.226.210.78/v3/signin/identifier?ds...
# 195                      http://fiverr.brandcoders.net
# 196                                  https://asdwg.ga/
# 197        https://tokensplatform.top/bone/?prt=192374
df_url.head()
#                                          Phising_URL
# 0                     http://site.tokeape.com/s/gcIK
# 1  https://t.co/ldJvaAvlAn?signature=newsletter&t...
# 2                 https://ollx.72123214.xyz/705nlr8s
# 3  http://www.webs10.net/bbva-es-particulares-cue...
# 4                            http://rebrand.ly/it53c


df_url.to_csv("Phising_Url.csv")





#
# phising_str_selenium_name2 = phising_str_selenium_name
# phising_str_selenium_name2
# phising_str_selenium_name2.split(sep="\n")
#
#
# df_ = pd.DataFrame(phising_str_selenium_name2.split(sep=" "))    # lstrip # strip('ne yazarsan')
# df_.head(40)
# df_url_ham = df_.iloc[1:-1:7]
# df_url_ham.index = np.arange(0,len(df_url_ham))
# new_url = ""
# for value in df_url_ham.values:
#     new_url = new_url + ' ' + value[0][0:-6]
# new_url = new_url.strip().split(" ")
# df_url = pd.DataFrame(new_url)
# df_url.columns = ['Phising_URL']

