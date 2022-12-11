import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


path = r"D:\chromedriver_win32\chromedriver.exe"

class JdSearch:

    def __init__(self):
        service = Service(executable_path=path)
        chrome_options = Options()
        chrome_options.add_argument("disable-blink-features=AutomationControlled")
        self.browser = webdriver.Chrome(service=service, options=chrome_options)

    def pase(self,response):
        soup = BeautifulSoup(response, 'lxml')
        item_arr = soup.select("ul[class = 'gl-warp clearfix'] li")
        result_list = []
        for item in item_arr:
            try:
                sku_id = item.attrs['data-sku']
                img = item.select('div.p-img')
                title = item.select('div[class = "p-name p-name-type-2"]')
                shop = item.select('div.p-shop')
                icons = item.select('div.p-icons')
                price = item.select('div.p-price')

                img = img[0].img.attrs['data-lazy-img']
                title = title[0].text.strip()
                shop = shop[0].text.strip()
                icons = icons[0].select('i')
                icons = [item_icons.text.strip() for item_icons in icons]
                icons = json.dumps(icons)
                price = price[0].i.text

                result_list.append((sku_id,img,title,shop,icons,price))

            except Exception as e:
                print(e.args)
        return result_list

    def sim_search(self,keyword, url):
        self.browser.get(url)
        search_input = self.browser.find_element("id", "key")
        search_input.send_keys(keyword)
        search_button = self.browser.find_element(By.CSS_SELECTOR, "button[aria-label = '搜索']")
        # search_button.click()
        ac = ActionChains(self.browser)
        ac.move_to_element(search_button).click()
        ac.send_keys(Keys.ENTER).perform()


    def main(self,keyword, url):
        self.sim_search(keyword, url)
        time.sleep(3)
        item_arr = self.pase(self.browser.page_source)
        self.browser.ex
        print(item_arr)
        self.browser.close()


if __name__ == '__main__':
    url = 'https://www.jd.com/'
    jd_search = JdSearch()
    jd_search.main('鼠标', url)
