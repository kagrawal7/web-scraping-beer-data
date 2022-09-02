from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



# We want to create a dictionary mapping reviewers to a list of beers they
# have left reviews for from the LCBO site

# def add_review() -> None:


if __name__ == '__main__':
    # run web scraper
    # some sort of for loop to go through every single beer page and get
    # the url of the page

    beer_url = "https://www.lcbo.com/en/stella-artois-17819"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(beer_url)
    time.sleep(1)
    page = driver.page_source
    print(page)
    driver.quit()

    # reviews = driver.find_elements(By.CLASS_NAME, "bv-content-item bv-content-top-review bv-content-review")
    # reviews = driver.find_elements(By.CSS_SELECTOR, "li.bv-content-item bv-content-top-review bv-content-review")
    # print(reviews)



    # # html = urlopen(beer_url)
    # # html_soup = BeautifulSoup(html, 'lxml')
    # # print(html_soup)
    # r = requests.get('http://localhost:8050/render.html', params={'url': beer_url})
    # print(r.text)

    # reviews = html_soup.find_all('li', {'itemprop': 'review'})
    # print(reviews)
