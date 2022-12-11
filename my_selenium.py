import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

s = Service(executable_path="D:\edgedriver_win64\msedgedriver.exe")
options = Options()
options.add_argument('disable-blink-features=AutomationControlled')


browser = webdriver.Edge(service=s,options=options)

browser.get('https://www.baidu.com')
time.sleep(5)
print(browser.title)