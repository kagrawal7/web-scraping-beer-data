# web-scraping-beer-data

This project is a "helper project" for the Beer Recommendation Project. It is fairly straightforward:

There is a website called BeerAdvocate that has thousands of reviews and ratings for thousands of different beers. Problem is, to access all beer pages you have to go to a page with links to different beer styles and each link with different beer styles have different beers, and each beer page only has a limited number of reviews and a link to a page with more reviews.

I scrape data from BeerAdvocate and attempt to create a data set mapping a list of random people to the beers they like and/or dislike. I will then use this data set for the Beer Recommendation Project.

I was first trying to get this data from the LCBO website but as it turns out their data was extremely disorganized and their HTML was unreadable by BeautifulSoup, and then I happily stumbled onto BeerAdvocate.

UPDATE 4:
Finally done!I Got each review for top 50 beers for each sub-style of beer. In total, more than 19,000 pages with reviews were scraped, taking about 23246 seconds or 387 minutes to run. I had to get rid of multithreading code for each beer's subpages because of the layout of the page; only a few beer subpages are available at any one page and you need the "next" tag to go to the next one, so instead I had to use a naive for loop. 

UPDATE 3:
Added some multithreading code for each beer's main page in concurrent_scraper branch (scraping up to 120 reviews for 500 beers across 2 styles takes about 158 seconds). Added more multithreading code for each beer's subpages as well (scraping up to 120 reviews for 500 beers across 2 styles takes about 148 seconds)

UPDATE 2:
I eliminated unnecessary login requests, which has sped up the process a bit, but it is still not enough (scraping up to 120 reviews for 500 beers across 2 styles takes about 527 seconds). I will be using parallelism and multithreading to speed up the process. Since I am not sure which approach will be better, I will implement both and see which works better on a subset of the beers.

UPDATE 1:
The LCBO site's html code was broken but luckily I discovered a site called beeradvocate.com, which stores reviews for thousands of different beers. I completed the code to scrape all beers and all reviews but realized this would take wayyy too long (we're talking days)! Currently in the process of figuring out ways to optimize this. Even if I were to scrape considerably less reviews and beers it would still take tens of hours. 