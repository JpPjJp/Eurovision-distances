from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time 
import csv
import copy

options = Options()
options.headless = True

for year in range(2000, 2020):

    xpath = "//a[@href='/eurovision/"+str(year)+"']"
    euDriver = webdriver.Firefox(options=options)
    euDriver.get("https://eurovisionworld.com/eurovision/"+str(year))
    
    place = euDriver.find_elements_by_xpath("//div[@id='voting_table']/table[1]/tbody/tr/td[1]")
    country = euDriver.find_elements_by_xpath("//div[@id='voting_table']/table[1]/tbody/tr/td[2]")
    points = euDriver.find_elements_by_xpath("//div[@id='voting_table']/table[1]/tbody/tr/td[4]")
    
    hostCountry = euDriver.find_element_by_xpath(xpath).text
    hostCountry = hostCountry.split(" ")
    hostCountry1 = " ".join(hostCountry[0:-1])
    
    for iteration, element in enumerate(country):
        country[iteration] = country[iteration].text
        points[iteration] = points[iteration].text
        place[iteration] = place[iteration].text
        
    euDriver.close()
    
    distanceList = []
    
    for iteration, element in enumerate(country):
        distanceDriver = webdriver.Firefox(options=options)
        distanceDriver.get("https://www.freemaptools.com/how-far-is-it-between.htm")
        try:
            acceptCookies = distanceDriver.find_element_by_xpath("//p[@class='fc-button-label']")
            acceptCookies.click()
        except:
            print("Unable to locate the Accept Cookies button..")
        startingPoint = distanceDriver.find_element_by_xpath("//input[@name='pointa']")
        finishingPoint = distanceDriver.find_element_by_xpath("//input[@name='pointb']")
        submitButton = distanceDriver.find_element_by_xpath("//p[@class='fmtbutton']")
        distance =distanceDriver.find_element_by_xpath("//input[@id='distance']")
        
        finishingPoint.send_keys(country[iteration])
        startingPoint.send_keys(hostCountry1)

        submitButton.click()
        time.sleep(5)
        distanceList.append(distance.get_property('value'))
        distanceDriver.close()
 
    with open('eurovision'+str(year)+'.csv', 'w', newline='') as csvfile:
        country_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for iteration, element in enumerate(country):
            country_writer.writerow([place[iteration], country[iteration], points[iteration], hostCountry1, hostCountry[-1], distanceList[iteration]])
   
