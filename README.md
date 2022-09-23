# web-scraping-beer-data

This project is a "helper project" for the Beer Recommendation Project. It is fairly straightforward; 
 I scrape data from LCBO and attempt to create a data set mapping a list of random people to the beers they like and/or dislike. I will then use this data set for the Beer Recommendation Project.

I had never learned web scraping before, so I learned along the way. I first tried using BeautifulSoup, but realized it was incorrectly reading the html code on LCBO's website so decided to switch to something else (TBD).

UPDATE 3:
Added some multithreading code for each beer's main page in concurrent_scraper branch (scraping up to 120 reviews for 500 beers across 2 styles takes about 158 seconds). Added more multithreading code for each beer's subpages as well (scraping up to 120 reviews for 500 beers across 2 styles takes about 148 seconds)

UPDATE 2:
I eliminated unnecessary login requests, which has sped up the process a bit, but it is still not enough (scraping up to 120 reviews for 500 beers across 2 styles takes about 527 seconds). I will be using parallelism and multithreading to speed up the process. Since I am not sure which approach will be better, I will implement both and see which works better on a subset of the beers.

UPDATE 1:
The LCBO site's html code was broken but luckily I discovered a site called beeradvocate.com, which stores reviews for thousands of different beers. I completed the code to scrape all beers and all reviews but realized this would take wayyy too long (we're talking days)! Currently in the process of figuring out ways to optimize this. Even if I were to scrape considerably less reviews and beers it would still take tens of hours. 