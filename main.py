from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.by import By

url = "https://bus.gov.ru/registry"
ser = Service("C:\\Users\\mrtik\\PycharmProjects\\parseSelenium\\chromedriver\\chromedriver.exe")
option = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=ser, options=option)

try:
    browser.get(url=url)
    # k = browser.find_element(by=By.LINK_TEXT, value='Результаты независимой оценки').get_attribute('href')
    # print(k)
    input_button = browser.find_element(by=By.CSS_SELECTOR, value=
    'body > div.main > ui-view > ui-view-ng-upgrade > ui-view > app-registry > app-registry-filter > form > div:nth-child(1) > div:nth-child(1) > label > div.search__col.search__col_type_2 > input')
    print(input_button)
    input_button.send_keys('онкологический диспансер')  # request in input
    # input_button.send_keys(Keys.ENTER)  # use enter
    show_button = browser.find_element(by=By.XPATH,
                                       value='/html/body/div[2]/ui-view/ui-view-ng-upgrade/ui-view/app-registry/app-registry-filter/form/div[2]/div/div[2]/div/button')
    show_button.click()  # use button
    soup = BeautifulSoup(browser.page_source, 'lxml')
    print(soup)
    reg_link = 'https://bus.gov.ru/registry'+soup.find('a', class_='result__button result__button_registry result__button_href-button').get('href')
    print(reg_link)
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
