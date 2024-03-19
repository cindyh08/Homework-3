import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"

cityofnyc = pd.read_csv(url)

cityofnyc['Date'] = pd.to_cityofnyctime(cityofnyc['Date'])

weekdays_cityofnyc = cityofnyc[cityofnyc['Date'].dt.dayoftheweek < 5]

civilain_counts = weekdays_cityofnyc.groupby(weekdays_cityofnyc['Date'].dt.dayoftheweek)['Count'].sum()
day_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

plt.figure(figsize=(10, 6))
plt.plot(day_of_the_week, civilain_counts, marker='o', linestyle='-')
plt.title('Civilian Counts by the Days of the Week')
plt.xlabel('The Day of the Week')
plt.ylabel('Civilain Counts')
plt.grid(True)
plt.show()