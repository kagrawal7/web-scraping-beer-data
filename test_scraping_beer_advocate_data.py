import pytest
import scraping_beer_advocate_data
import credentials
import requests

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
    url_a = "https://www.beeradvocate.com/beer/profile/1199/611752/"
    url_b = "https://www.beeradvocate.com/beer/profile/45723/460275/"
    data_set_a = {'1971bernat': {'Ultimate Oktoberfest': 4}, 'metnut': {'Ultimate Oktoberfest': 4.92}, 'skabiski': {'Ultimate Oktoberfest': 4.3},
                  'nerofiddled': {'Ultimate Oktoberfest': 4.16}, 'lifesanesthesia': {'Ultimate Oktoberfest': 4.33}, 'jera1350': {'Ultimate Oktoberfest': 4.29},
                  'gkruszewski': {'Ultimate Oktoberfest': 4.25}, 'mothman': {'Ultimate Oktoberfest': 4.1}, 'tangowhiskey': {'Ultimate Oktoberfest': 4.37},
                  'msscott1973': {'Ultimate Oktoberfest': 4.24}, 'cpmitchno1': {'Ultimate Oktoberfest': 4.09}, 'darklordscott': {'Ultimate Oktoberfest': 4.28},
                  'soneast': {'Ultimate Oktoberfest': 4.09}, 'dalkri': {'Ultimate Oktoberfest': 5}, 'chuckdiesel24': {'Ultimate Oktoberfest': 4},
                  'roguer': {'Ultimate Oktoberfest': 3.52}, 'ducksfan16': {'Ultimate Oktoberfest': 4.2}, 'admiralozone': {'Ultimate Oktoberfest': 4.42},
                  'mikeward': {'Ultimate Oktoberfest': 3.76}, 'fordcoyote15': {'Ultimate Oktoberfest': 4.12}, 'elgallo': {'Ultimate Oktoberfest': 4.13},
                  'zebulonxzogg': {'Ultimate Oktoberfest': 3.79}, 'chinchill': {'Ultimate Oktoberfest': 4.25}, 'brewstl': {'Ultimate Oktoberfest': 4.25},
                  'fehrminator': {'Ultimate Oktoberfest': 4}, 'macmalt': {'Ultimate Oktoberfest': 3.85}, 'peach63': {'Ultimate Oktoberfest': 4.16},
                  'valdez_mescalito': {'Ultimate Oktoberfest': 4.06}, 'braunmeister_1943': {'Ultimate Oktoberfest': 4.05},
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

    return [site, url_a, url_b, data_set_a, data_set_b]


def test_multiple_review_pages() -> None:
    """ """
    site, url_a, url_b, data_set_a, data_set_b = \
        setup_tests()
    beer = 'Ultimate Oktoberfest'
    result = {}
    scraping_beer_advocate_data.beer_main(site, result, url_a)
    for reviewer in result:
        assert result[reviewer][beer] == data_set_a[reviewer][beer]


def test_single_review_pages() -> None:
    """ """
    site, url_a, url_b, data_set_a, data_set_b = \
        setup_tests()
    beer = 'Cherry and the Hendersons'
    result = {}
    scraping_beer_advocate_data.beer_main(site, result, url_b)
    for reviewer in result:
        assert result[reviewer][beer] == data_set_b[reviewer][beer]


def test_combined_review_pages() -> None:
    """ """
    site, url_a, url_b, data_set_a, data_set_b = \
        setup_tests()
    result = {}
    data_a = data_set_a.copy()
    data_b = data_set_b.copy()
    data_a.update(data_b)
    scraping_beer_advocate_data.beer_main(site, result, url_a)
    scraping_beer_advocate_data.beer_main(site, result, url_b)
    for reviewer in result:
        if 'Ultimate Oktoberfest' in result[reviewer]:
            beer = 'Ultimate Oktoberfest'
            assert result[reviewer][beer] == data_a[reviewer][beer]
        else:
            beer = 'Cherry and the Hendersons'
            assert result[reviewer][beer] == data_a[reviewer][beer]


if __name__ == '__main__':
    login_url = "https://www.beeradvocate.com/community/login/login"
    login_info = {'login': credentials.username,
                  'password': credentials.password}
    with requests.session() as scraping_beer_advocate_data.s:
        scraping_beer_advocate_data.s.post(login_url, data=login_info)
        # pytest.main(['test_scraping_beer_advocate_data.py'])
        test_multiple_review_pages()
        test_single_review_pages()
        test_combined_review_pages()