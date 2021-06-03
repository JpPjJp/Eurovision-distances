import pandas as pd
import geopy.distance

def distanceCalc(row):
    city1 = row.loc['capital_city']
    city2 = row.loc['host_city']

    city1cords = [series.loc[city1, 'lat'], series.loc[city1, 'lng']]
    city2cords = [series.loc[city2, 'lat'], series.loc[city2, 'lng']]
    
    return (geopy.distance.geodesic(city1cords, city2cords).km)

#set up world cities dataframe
citiesandcountries = pd.read_csv("worldcities.csv")
citiesandcountries.set_index('country', inplace = True)
citiesandcountries = citiesandcountries.loc[citiesandcountries.capital == 'primary']

#set up eurovision results dataframe
euresults = pd.read_csv("eurovision.csv", header=None)
euresults.columns = ['place', 'country', 'points', 'host_city', 'year']
euresults = euresults.drop(euresults.index[502])

#find capital of participant country, create a new column in euresults containing this
capitals = euresults.country.apply(lambda x: citiesandcountries.loc[x, 'city'])
euresults = euresults.assign(capital_city = capitals.to_frame())

#reorder columns
old_cols = euresults.columns.values
new_cols = ['place', 'country', 'capital_city', 'points', 'year', 'host_city']
euresults = euresults.reindex(columns=new_cols)
euresults.to_csv('euresults.csv')

#select a subset of columns from euresults
citypairs = euresults.loc[:, ['capital_city','country', 'host_city']]
citypairs.columns = ['capital_city','country', 'host_city']

#filter the worldcities.csv to contain only cities listed in the capital_city column and host_city column of citypairs
citiesandcountries2 = pd.read_csv("worldcities2.csv")
capitalcities = citiesandcountries2.loc[citiesandcountries2.city.isin(citypairs.loc[:,'capital_city'])]
hostcities = citiesandcountries2.loc[citiesandcountries2.city.isin(citypairs.loc[:,'host_city'])]

#remove non-european cities 
capitalcities = capitalcities.loc[~capitalcities.iso3.isin(['USA', 'CAN'])]
hostcities = hostcities.loc[~hostcities.iso3.isin(['USA', 'CAN'])]

#combines capitalcities and hostcities, drop any duplicates
series = pd.concat([capitalcities, hostcities])
series = series.drop_duplicates()
series.set_index('city', inplace=True)

#calculate distance between participantcity and hostcity
citypairs = citypairs.apply(distanceCalc, axis=1)

#add new column containing distance to euresults csv
euresults = euresults.assign(dist_between_host_and_participant = citypairs.to_frame())
euresults = euresults.round(decimals = 0)
euresults.to_csv('results_with_distance.csv')


