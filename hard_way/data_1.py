import numpy as np
import pandas as pd
population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135
}

population = pd.Series(population_dict)

area_dict = {
             'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995
             }
area = pd.Series(area_dict)

weather_dict = {
                 'California': 42,
                 'Texas': 69,
                 'New York': 14,
                 'Florida': 17,
                 'Illinois': 14
                }

weather=pd.Series(weather_dict)

states = pd.DataFrame({'population': population,'area': area, 'weather': weather })
states['density'] = states['population'] / states['area']
#print(states.T)
#print(states.loc[states.density > 100, ['pop', 'density']])
data = [{'a': i, 'b': 2 * i} for i in range(3)]

#print(pd.DataFrame(data))
#print(pd.DataFrame(np.random.rand(5, 2),columns=['foo', 'bar'],index=['a', 'b', 'c', 'd', 'e']))
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
data = pd.Series([0.25, 0.5, 0.75, 1.0],index=['a', 'b', 'c', 'd'])
#print(data['a':'c'])
#print(indA | indB)
#print(states)
#states.loc[:'Illinois', :'pop']
#print(states.iloc[:3, 2:4])