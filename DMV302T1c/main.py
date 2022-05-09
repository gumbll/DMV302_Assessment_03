# import libs
import matplotlib.pyplot as plt
import pandas as pd

# read datafile into dataframe
col_list = ['date',
            'act_avg_temp',
            'act_min_temp',
            'act_max_temp',
            'avg_min_temp',
            'avg_max_temp',
            'lowest_temp',
            'highest_temp',
            'act_amt_rain',
            'avg_amt_rain',
            'highest_amt_rain']
df = pd.read_csv("Data/Dataset2.csv", usecols=col_list)

# from this we are able to derive the average minimum and
# maximum temps each day and see that in the winter period it is significantly colder
# if we had data from the following year we would be able to make
# a comparison and determine if there was an increase or decrease in temperature.
ax = df.plot(x='date', y='avg_min_temp', kind='line', color='#CFEB1B', label='average minimum temp')
df.plot(x='date', y='avg_max_temp', kind='line', color='#E62371', label='average maximum temp',
        xlabel='Over Time', ylabel='Temperature', ax=ax)


# from this chart we are able to see the amount of rain over the minimum temp and
# compare to see if lower temps are possibly the effect of the amount of rain
fig, ax1 = plt.subplots()
ax1.set_xlabel('time over one year')
ax1.set_ylabel('actual minimum temp', color='black')
ax1.plot(df['date'], df['act_min_temp'], color='red')
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'black'
ax2.set_ylabel('actual amount of rain', color='black')
ax2.plot(df['date'], df['act_amt_rain'], color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# from this chart we are able to see the amount of rain over the maximum temp and
# compare to see if higher temps are possibly the effect of the amount of rain
fig, ax1 = plt.subplots()
ax1.set_xlabel('time over one year')
ax1.set_ylabel('actual max temp', color='black')
ax1.plot(df['date'], df['act_max_temp'], color='red')
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'black'
ax2.set_ylabel('actual amount of rain', color='black')
ax2.plot(df['date'], df['act_amt_rain'], color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# make everything fit correctly
plt.xticks(rotation=90) # we have way too many dates to be able to show them effectively
plt.tight_layout()

# present data graph
plt.show()
