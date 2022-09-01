from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# We want to create a dictionary mapping reviewers to a list of beers they
# have left reviews for from the LCBO site

# def add_review() -> None:


if __name__ == '__main__':
    # run web scraper
    # some sort of for loop to go through every single beer page and get
    # the url of the page

    beer_url = "https://www.lcbo.com/en/stella-artois-17819"
    html = urlopen(beer_url)
    html_soup = BeautifulSoup(html, 'html.parser')
    print(html_soup)



