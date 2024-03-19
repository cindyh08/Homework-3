import pandas as pd

url = " https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"


cityofnyc = pd.read_csv(url)

cityofnyc['Date'] = pd.to_datetime(cityofnyc['Date'])

cityofnyc_2019_brooklyn = cityofnyc[(cityofnyc['Date'].dt.year == 2019) & (cityofnyc['Place'] == 'Brookyln Bridge')]

civilian_count_brooklyn_weather = cityofnyc_2019_brooklyn.groupby('Weather Statis')['Count'].sum()

print(civilian_count_brooklyn_weather)
