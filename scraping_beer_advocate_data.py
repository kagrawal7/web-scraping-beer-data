from bs4 import BeautifulSoup, NavigableString, Tag
import re
import credentials
import requests
import pandas as pd


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


def each_beer_main_helper(html_soup: BeautifulSoup, user_dict: dict) -> None:
    """Helper for each_beer_main"""
    beer_name = extract_beer_name(html_soup)
    scrape_reviews_info(html_soup, beer_name, user_dict)


def each_beer_main(website: str, user_dict: dict, login_link: str,
                   creds: dict, beer_url: str) -> None:
    """ The main function for getting reviews for each beer"""
    html_soup = login_get_soup(login_link, creds, beer_url)

    multiple_pages_tag = html_soup.find('span', {'style': 'font-weight:bold;'})
    each_beer_main_helper(html_soup, user_dict)

    if multiple_pages_tag is not None:
        j = 0
        for des in multiple_pages_tag.children:
            j += 1
            if j >= 5 and isinstance(des, Tag) and \
                    des.string not in ['next', 'last']:
                each_beer_main_helper(login_get_soup(
                    login_link, creds, website + des['href']), user_dict)


def each_style_main_helper(website: str, user_dict: dict, login_link: str,
                   creds: dict, style_soup: BeautifulSoup) -> None:
    """Helper for each_style_main"""
    td_tags = style_soup.find_all('td',
                                  {'valign': 'top', 'class': 'hr_bottom_light'})
    for td_tag in td_tags:
        beer_tag = td_tag.find('a')
        if beer_tag is not None:
            each_beer_main(website, user_dict, login_link, creds,
                           website + beer_tag['href'])


def each_style_main(website: str, user_dict: dict, login_link: str,
                   creds: dict, style_link: str) -> None:
    """Main function for each style
    Scrape info from each beer, check for more sub-pages for same style
    """
    style_soup = login_get_soup(login_link, creds, style_link)
    # scrape main style page and then check for more for each style
    each_style_main_helper(website, user_dict, login_link, creds, style_soup)
    # multiple_pages_tag = style_soup.find('span', {'style': 'font-weight:bold;'})
    # if multiple_pages_tag is not None:
    #     j = 0
    #     for des in multiple_pages_tag.children:
    #         j += 1
    #         if j == 5 and isinstance(des, Tag) and \
    #                 des.string not in ['next', 'last']:
    #             each_style_main_helper(website, user_dict, login_link, creds,
    #                                    login_get_soup(login_link, creds,
    #                                                   website + des['href']))


def login_get_soup(login_link: str, creds: dict, page_url: str) \
        -> BeautifulSoup:
    """Login with credentials in payload and
    return BeautifulSoup of page"""
    with requests.session() as s:
        s.post(login_link, data=creds)
        r = s.get(page_url)
        return BeautifulSoup(r.content, 'html.parser')


if __name__ == '__main__':
    # run web scraper
    site = "http://beeradvocate.com"
    login_url = "https://www.beeradvocate.com/community/login/login"
    payload = {'login': credentials.username,
               'password': credentials.password}
    data_set = {}

    # run for loop over all beers
    beer_styles_link = "https://www.beeradvocate.com/beer/styles/"
    styles_soup = login_get_soup(login_url, payload, beer_styles_link)
    style_tags = styles_soup.find_all('div', {'class': 'stylebreak'})
    for style_tag in style_tags:
        a_tags = style_tag.find_all('a')
        for a_tag in a_tags:
            style_url = site + a_tag['href']
            each_style_main(site, data_set, login_url, payload, style_url)

    df = pd.DataFrame(data_set).transpose()
    df.to_csv("/Users/macbook/Desktop/Kush Independent Projects/"
              "Web Scraping Beer Data/web-scraping-beer-data/user_data.csv")
