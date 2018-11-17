import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
 reader = csv.reader(f)
 header_row = next(reader)
for index, column_header in enumerate(header_row):
 print(index, column_header)

with open(filename) as f:
 reader = csv.reader(f)
 header_row = next(reader)
 dates, highs, lows = [], [], []
 for row in reader:
  try:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    high = int(row[1])
    low = int(row[3])
  except ValueError:
    print(current_date, 'missing data')
  else:
   dates.append(current_date)
   highs.append(high)
   lows.append(low)

fig = plt.figure(dpi=120, figsize=(20, 6))
plt.plot(dates,highs, c='green',alpha=0.5)
plt.plot(dates, lows, c='blue',alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
print(highs)