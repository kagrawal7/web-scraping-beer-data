from urllib.request import Request, urlopen
from bs4 import BeautifulSoup, NavigableString
import re
import requests


# We want to create a dictionary mapping reviewers to a list of beers they
# have left reviews for from the beer advocacy site

# def add_review() -> None:

def get_beer_name(soup) -> str:
    """ Given a header tag, return the navigable string"""
    i = -1
    for des in beer_tag.descendants:
        if i >= 0 and isinstance(des, NavigableString):
            return des
        i += 1


if __name__ == '__main__':
    # run web scraper
    # some sort of for loop to go through every single beer page and get
    # the url of the page


    # For each beer
    # for each subpage in a beer page
    beer_url = "https://www.beeradvocate.com/beer/profile/1199/611752/"
    beer_url_request = Request(url=beer_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(beer_url_request)
    html_soup = BeautifulSoup(html, 'lxml')

    beer_tag = html_soup.find('div', {'class': 'titleBar'})
    beer_name = get_beer_name(beer_tag)

    reviews = html_soup.find_all('div', {'id': 'rating_fullview_content_2'})
    user_dict = {}

    for review in reviews:
        reviewer_link = review.find('a', {'class': 'username'})['href']
        name = re.split(r"/|\.", reviewer_link)[3]

