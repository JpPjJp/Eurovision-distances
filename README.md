# Eurovision-distances-python
This repository uses selenium to scrape for eurovision results + pandas / matplotlib to see if countries closer to the host do better in the contest. 

I thought it would be interesting to see if distance played a role in how well countries did in Eurovision! So this repository contains a web scraper for the Eurovision website to get the results from 2000-2019 and adds it to a CSV file for each year ([eu.py](https://github.com/JpPjJp/Eurovision-distances/blob/main/eu.py)). I then used pandas to add an additional column showing the distance between the performer's country capital and the host city ([distance_calc.py](https://github.com/JpPjJp/Eurovision-distances/blob/main/distance_calc.py)). 

Just the results of the final for the years 2000-2019 (inclusive) can be seen in the [eurovision.csv](https://github.com/JpPjJp/Eurovision-web-scraper/blob/main/eurovision.csv) file

The results with the additional column containing the distance between the participant country's capital and the host city can be seen in the [results_with_distance.csv](https://github.com/JpPjJp/Eurovision-web-scraper/blob/main/results_with_distance.csv) file

After this, I plotted the results using matplotlib ([plotting_eurovision_results.py](https://github.com/JpPjJp/Eurovision-distances/blob/main/plotting_eurovision_results.py)). There seems to be a little merit in saying that countries closest to the host do better than country's further away. The top 7 places generally were closer than the middle 14 places.
![results](https://github.com/JpPjJp/Eurovision-web-scraper/blob/main/eurovision%20plot.png)
