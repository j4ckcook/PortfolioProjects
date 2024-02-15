import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Import Data from excel
data = pd.read_excel("employMvMd.xlsx", header = 0)

# Convert columns that start with 'E' to numeric
data.loc[:, data.columns.str.startswith('E')] = data.loc[:, data.columns.str.startswith('E')].apply(pd.to_numeric, errors='coerce')

# Add a time column as a integer from 1 to N
# Create a new column 'time' representing the integer from 1 to N
data['time'] = range(1, len(data) + 1)
# Converting 'DATE' column to monthly date format
data['mdate'] = pd.to_datetime(data['DATE'], format='%Y:%m').dt.to_period('M')


# Focus on the time window from 2007 to 2012
data = data[(data['mdate'].dt.year >= 2007) & (data['mdate'].dt.year <= 2012)]

# Convert 'mdate' to string representation
data['mdate'] = data['mdate'].astype(str)


# Calculate mean for each variable at time 817 (assuming 'time' is the index)
for var in ['EMPLOY08M12', 'EMPLOY10M12', 'EMPLOY23M8']:
    mean_value = data.loc[data['time'] == 817, var].mean()
    data[var] = data[var] / mean_value

#Plot the Graph

plt.figure(figsize=(10,6))
plt.plot(data['mdate'], data['EMPLOY08M12'], label= 'Dec 2008')
plt.plot(data['mdate'], data['EMPLOY10M12'], label='Dec 2010')
plt.plot(data['mdate'], data['EMPLOY23M8'], label='Today')
plt.title('The Great Recession')
plt.xlabel('Months since January 2007')
plt.ylabel('Cumulative change in employment')
plt.legend()
# Set x-axis ticks every 5 ticks and rotate 45 degrees
# Set x-axis ticks every 5 ticks
tick_positions = np.arange(0, len(data), 5)
plt.xticks(tick_positions, data['mdate'].iloc[tick_positions], rotation=45)
plt.show()