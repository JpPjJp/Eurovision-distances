import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#grouping by final position (place) and then finding the avg distance for each position
test = pd.read_csv('results_with_distance.csv')
test = test.groupby('place').dist_between.agg(['mean'])

#plotting above
plt.bar(test.index,test.loc[:, 'mean'], color='white',edgecolor='black')

#finding the average distance for the 0-7, 8-13, 14-21, 22-27 position brackets
avg7 = test.loc[0:7, 'mean'].mean()
avg13 = test.loc[8:13, 'mean'].mean()
avg20 = test.loc[14:21, 'mean'].mean()
avg27 = test.loc[22:27, 'mean'].mean()

#plotting above
plt.axhline(y = avg7, xmin=0, xmax=0.25, color='red', linewidth=7)
plt.axhline(y= avg13,xmax=0.5, xmin=0.25, color='green', linewidth=7)
plt.axhline(y= avg20,xmax=0.75, xmin=0.50, color='orange', linewidth=7)
plt.axhline(y= avg27,xmax=1, xmin=0.75, color='yellow', linewidth=7)

#ticks, labels
plt.xticks(np.arange(1, 28, step=1))
plt.title('Eurovision')
plt.ylabel('Average distance to host for given position (km)')
plt.xlabel('Place')
plt.show()