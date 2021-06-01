# Eurovision-web-scraper
Selenium driver web scraper for eurovision results + the distance between participant countries and host country

I thought it would be interesting to see if the old theory that countries only vote for their nearest neighbours was true, but needed data for it! So this 
scrapes the Eurovision website for the results from 2000-2019 and adds it to a CSV file for each year. The code also then scrapes a "distance between" website
to get the distance between the performer's country capital and the host city. There is no doubt a more efficient way to get this information, but it does the job XD!

Just the results of the final for the years 2000-2019 (inclusive) can be seen in the [eurovision.csv](https://github.com/JpPjJp/Eurovision-web-scraper/blob/main/eurovision.csv) file

The results with the additional column containing the distance between the participant country's capital and the host city can be seen in the [results_with_distance.csv](https://github.com/JpPjJp/Eurovision-web-scraper/blob/main/results_with_distance.csv) file
