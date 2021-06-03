from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv

options = Options()
options.headless = True

for year in range(2000, 2020):
    print ("start " + str(year))
    xpath = "//a[@href='/eurovision/"+str(year)+"']"
    euDriver = webdriver.Firefox(options=options)
    euDriver.get("https://eurovisionworld.com/eurovision/"+str(year))
    
    #find necessary elements (place, country, points won)
    place = euDriver.find_elements_by_xpath("//div[@id='voting_table']/table[1]/tbody/tr/td[1]")
    country = euDriver.find_elements_by_xpath("//div[@id='voting_table']/table[1]/tbody/tr/td[2]")
    points = euDriver.find_elements_by_xpath("//div[@id='voting_table']/table[1]/tbody/tr/td[4]")
    
    #find city
    hostCity = euDriver.find_element_by_xpath(xpath).text
    hostCity = hostCity.split(" ")
    hostCity1 = " ".join(hostCity[0:-1])

    #for each place, etc. element found, extract its text
    for iteration, element in enumerate(country):
        country[iteration] = country[iteration].text
        points[iteration] = points[iteration].text
        place[iteration] = place[iteration].text
        
    print ("end " + str(year))
    #close driver
    euDriver.close()

    #write results for that year to csv
    with open('eurovision'+str(year)+'.csv', 'w', newline='') as csvfile:
        country_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for iteration, element in enumerate(country):
            country_writer.writerow([place[iteration], country[iteration], points[iteration], hostCity1, hostCity[-1]])
   
