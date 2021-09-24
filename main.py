from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = "https://gulayaka-edu.ru/login/index.php"
username = "id173427551"
password = "Kuza1502!"
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("loginbtn").click()
driver.get("https://gulayaka-edu.ru/mod/quiz/report.php?id=1922&mode=overview")#add hw selection
page_size = driver.find_element_by_id("id_pagesize")
page_size.clear()
page_size.send_keys("100")
driver.find_element_by_id("id_onlygraded").click()
driver.find_element_by_id("id_submitbutton").click()
