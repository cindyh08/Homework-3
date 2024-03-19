
import pandas as pd

url = " https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"


cityofnyc = pd.read_csv(url)

cityofnyc['Date'] = pd.to_datetime(cityofnyc['Date'])

cityofnyc_2019_brooklyn = cityofnyc[(cityofnyc['Date'].dt.year == 2019) & (cityofnyc['Place'] == 'Brookyln Bridge')]

civilian_count_brooklyn_weather = cityofnyc_2019_brooklyn.groupby('Weather Statis')['Count'].sum()

print(civilian_count_brooklyn_weather)

def sort_time_of_day(hour):
    if 5 <= hour <=12:
        return 'Morning'
    elif 12 <= hour <= 18:
        return 'Afternoon'
    elif 18 <= hour <= 21:
        return 'Evening'
    else:
        return 'Night'

cityofnyc['The time of day'] = cityofnyc['Hour'].apply(sort_time_of_day)

print(cityofnyc.head())