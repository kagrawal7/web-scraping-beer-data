import pytest
import scraping_beer_advocate_data as scraping_file
import credentials
# Here we will test that our scraping code works for single beer pages,
# meaning that we will only be testing each_beer_main; not the code
# that accesses every single beer on the website
# also note that a few reviews are bound to be lost due to anomalies in
# html code

#       test cases:
# a: multiple review pages for single beer
# b: single review page for a beer
# c: combined


def setup_tests() -> list:
    site = "http://beeradvocate.com"
    login_url = "https://www.beeradvocate.com/community/login/login"
    payload = {'login': credentials.username,
               'password': credentials.password}
    url_a = "https://www.beeradvocate.com/beer/profile/1199/611752/"
    url_b = "https://www.beeradvocate.com/beer/profile/45723/460275/"
    data_set_a = {'valdez_mescalito': {'Ultimate Oktoberfest': 4.06}, 'braunmeister_1943': {'Ultimate Oktoberfest': 4.05},
                  'ssgcujo': {'Ultimate Oktoberfest': 3.75}, 'cm55': {'Ultimate Oktoberfest': 4.36}, 'jzeilinger': {'Ultimate Oktoberfest': 3.78},
                  'phineasmcclintock': {'Ultimate Oktoberfest': 4}, 'zeff80': {'Ultimate Oktoberfest': 4.37}, 'socon67': {'Ultimate Oktoberfest': 4.1},
                  'ozzylizard': {'Ultimate Oktoberfest': 3.71}, 'sjones5045': {'Ultimate Oktoberfest': 4.09}, 'cryptichead': {'Ultimate Oktoberfest': 4},
                  'brumaster77': {'Ultimate Oktoberfest': 4.56}, 'ovaltine': {'Ultimate Oktoberfest': 4.19}, 'bigironh': {'Ultimate Oktoberfest': 4.25},
                  'budlum': {'Ultimate Oktoberfest': 3.8}, 'theepeeist': {'Ultimate Oktoberfest': 4.13}, 'sludgeman': {'Ultimate Oktoberfest': 4.13},
                  'taenim': {'Ultimate Oktoberfest': 4}, 'micada': {'Ultimate Oktoberfest': 3.43}, 'greenbayba': {'Ultimate Oktoberfest': 3.92},
                  'greywulfken': {'Ultimate Oktoberfest': 4}, 'tla': {'Ultimate Oktoberfest': 4.28}, 'sparty76': {'Ultimate Oktoberfest': 4.39},
                  'beerformuscle': {'Ultimate Oktoberfest': 4.14}, 'paulish': {'Ultimate Oktoberfest': 4}, 'oberon': {'Ultimate Oktoberfest': 4.14},
                  'cotton_27': {'Ultimate Oktoberfest': 4.24}, 'jkblr': {'Ultimate Oktoberfest': 3.43}, 'manta200': {'Ultimate Oktoberfest': 4.02},
                  'johnnyhopps': {'Ultimate Oktoberfest': 4}, 'chocolatefreak': {'Ultimate Oktoberfest': 4.33}, 'cjgiant': {'Ultimate Oktoberfest': 3.8},
                  'beergorrilla': {'Ultimate Oktoberfest': 4.02}, 'dinglehacker': {'Ultimate Oktoberfest': 4.23},
                  'coasterguy': {'Ultimate Oktoberfest': 3.74}, 'bouleboubier': {'Ultimate Oktoberfest': 3.67}, 'zap': {'Ultimate Oktoberfest': 4.25}, 'zaphog': {'Ultimate Oktoberfest': 4},
                  'grumpygas': {'Ultimate Oktoberfest': 4.18}, 'selekt0r': {'Ultimate Oktoberfest': 4.46}, 'puboflyons': {'Ultimate Oktoberfest': 4.01},
                  'beerchitect': {'Ultimate Oktoberfest': 3.81}, 'jaxon53': {'Ultimate Oktoberfest': 4.37}, 'cdriver0414': {'Ultimate Oktoberfest': 4.81},
                  'phoodcritic': {'Ultimate Oktoberfest': 4.08}}
    data_set_b = {'ironrakkasan': {'Cherry and the Hendersons': 3.51}}

    return [site, login_url, payload, url_a, url_b,
            data_set_a, data_set_b]


def test_multiple_review_pages() -> None:
    """ """
    lst = setup_tests()
    beer = 'Ultimate Oktoberfest'
    result = {}
    scraping_file.each_beer_main(lst[0], result, lst[1], lst[2], lst[3])
    for reviewer in result:
        assert result[reviewer][beer] == lst[5][reviewer][beer]


def test_single_review_pages() -> None:
    """ """
    lst = setup_tests()
    beer = 'Cherry and the Hendersons'
    result = {}
    scraping_file.each_beer_main(lst[0], result, lst[1], lst[2], lst[4])
    for reviewer in result:
        assert result[reviewer][beer] == lst[6][reviewer][beer]


def test_combined_review_pages() -> None:
    """ """
    lst = setup_tests()
    result = {}
    lst[5].update(lst[6])
    scraping_file.each_beer_main(lst[0], result, lst[1], lst[2], lst[3])
    scraping_file.each_beer_main(lst[0], result, lst[1], lst[2], lst[4])
    for reviewer in result:
        if 'Ultimate Oktoberfest' in result[reviewer]:
            beer = 'Ultimate Oktoberfest'
            assert result[reviewer][beer] == lst[5][reviewer][beer]
        else:
            beer = 'Cherry and the Hendersons'
            assert result[reviewer][beer] == lst[5][reviewer][beer]


if __name__ == '__main__':
    pytest.main(['test_scraping_beer_advocate_data.py'])
