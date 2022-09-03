from urllib.request import Request, urlopen
from bs4 import BeautifulSoup, NavigableString
import re
import credentials
# We want to create a dictionary mapping reviewers to a list of beers they
# have left reviews for from the beer advocacy site


def extract_beer_name(html_soup) -> str:
    """ Given a header tag, return the beer name"""
    header_tag = html_soup.find('div', {'class': 'titleBar'})

    i = -1
    for des in header_tag.descendants:
        if i >= 0 and isinstance(des, NavigableString):
            return des
        i += 1


def extract_rating(html_soup: BeautifulSoup) -> float:
    """ Extract the score given a span tag in a rating only section"""
    i = 0
    for des in html_soup.descendants:
        if i == 2:
            if not isinstance(des, NavigableString):
                return -1
            try:
                float(str(des))
            except ValueError:
                return -1
            else:
                return float(str(des))
        i += 1


def get_soup(beer_url: str) -> BeautifulSoup:
    """ Given link for beer, extract the html soup"""
    beer_url_request = Request(url=beer_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(beer_url_request)
    return BeautifulSoup(html)


def scrape_reviews_info(
        html_soup: BeautifulSoup, beer_name: str, user_dict: dict) -> None:
    """ Go through each review, get relevant info and add to user_dict
    """
    reviews = html_soup.find_all('div', {'id': 'rating_fullview_content_2'})

    for review in reviews:
        reviewer_link = review.find('a', {'class': 'username'})['href']
        name = re.split(r"/|\.", reviewer_link)[3]

        # Have to add an if statement for whether or not reviewer left a
        # review or only left a rating
        span_tag = review.find('span', {'class': 'muted'})
        span_tag_string = []
        for des in span_tag.descendants:
            span_tag_string.append(des)
            break

        rev_or_rate = re.split(r" |:", span_tag_string[0])[0]

        if rev_or_rate == 'Reviewed':
            score = float(review.find('span', {'class': 'BAscore_norm'}).string)
        elif rev_or_rate == 'Rated':
            returned_val = extract_rating(span_tag)
            if returned_val < 0:
                # some error occurred AKA incorrect html code,
                # so we ignore this review
                continue
            else:
                score = returned_val
        else:
            continue

        # add relevant info to user_dict
        if name not in user_dict:
            user_dict[name] = {beer_name: score}
        else:
            user_dict[name][beer_name] = score


def each_beer_main(html_soup: BeautifulSoup, user_dict: dict) -> None:
    """ The main function for getting reviews for each beer"""
    beer_name = extract_beer_name(html_soup)
    scrape_reviews_info(html_soup, beer_name, user_dict)


def login() -> None:
    login_url = "https://www.beeradvocate.com/community/login/"
    payload = {'username': credentials.username,
               'password': credentials.password}
    

    return


if __name__ == '__main__':
    # run web scraper
    # some sort of for loop to go through every single beer page and get
    # the url of the page
    login()
    data_set = {}
    url = "https://www.beeradvocate.com/beer/profile/1199/611752/"
    soup = get_soup(url)
    each_beer_main(soup, data_set)
    # print(data_set)
    # print(len(data_set))
    # ba_content_tag = soup.find('div', {'id': 'ba-content'})
    # descendants = ba_content_tag.descendants
    # i = 0
    # for x in descendants:
    #     i += 1
    # print(i)

    multiple_pages_tag = soup.find('span', {'style': 'font-weight:bold;'})
    print(soup)
    # if multiple_pages_tag is not None:
    #     # multiple pages
    #     print("\n")
    #
    #     # each_beer_main(soup, data_set)
    # else:
    #     each_beer_main(soup, data_set)

