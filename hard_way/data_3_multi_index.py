import numpy as np
import random
import pandas as pd
df = pd.DataFrame(np.random.rand(4, 2),
index=[['a', 'b', 'a', 'b'], [1, 2, 3, 4]],columns=['data1', 'data2'])
index = [('California', 2000), ('California', 2010),
('New York', 2000), ('New York', 2010),
('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
18976457, 19378102,
20851820, 25145561]
pop = pd.Series(populations, index=index)
pop.index.names = ['State']

############################################################

indexs = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
names=['subject', 'type'])
data = np.round(np.random.randn(4,6),1)
data[:, ::2] *= 10
data += 37
health_data = pd.DataFrame(data,index=indexs, columns=columns)
population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}
population = pd.Series(population_dict)
area_dict = {'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995}
area = pd.Series(area_dict)
weather_dict = {'California': 42,
                 'Texas': 69,
                 'New York': 14,
                 'Florida': 17,
                 'Illinois': 14}
weather=pd.Series(weather_dict)
pop = pd.DataFrame({'population': population,'area': area, 'weather': weather })
pop.index.names = ['States']
#print(pop[pop > 22000000])
#print(pop[['population']])
#print(health_data.Guido['HR'])
data_mean = health_data.mean(level='Value')
#print(data_mean)