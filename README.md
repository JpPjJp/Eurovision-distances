# Eurovision-web-scraper
Selenium driver web scraper for eurovision results + the distance between participant countries and host country

I thought it would be interesting to see if the old theory that countries only vote for their nearest neighbours was true, but needed data for it! So this 
scrapes the Eurovision website for the results from 2000-2019 and adds it to a CSV file for each year. I then used pandas to add an additional column showing the distance between the performer's country capital and the host city. 

Just the results of the final for the years 2000-2019 (inclusive) can be seen in the [eurovision.csv](https://github.com/JpPjJp/Eurovision-web-scraper/blob/main/eurovision.csv) file

The results with the additional column containing the distance between the participant country's capital and the host city can be seen in the [results_with_distance.csv](https://github.com/JpPjJp/Eurovision-web-scraper/blob/main/results_with_distance.csv) file

I then plotted the results using matplotlib. There doesn't seem to be any merit in saying that countries closest to the host do better than country's further away.
![results](https://github.com/JpPjJp/Eurovision-web-scraper/blob/main/eurovision%20plot.png)
