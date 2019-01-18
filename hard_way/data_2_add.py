import numpy as np
import random
import pandas as pd
A = pd.DataFrame(np.random.rand(4, 2),
columns=list('AB'))
#print(A)
B = pd.DataFrame(np.random.rand(5, 3),
columns=list('BAC'))
#print(B)
#print(A+B)
index = [('California', 2000), ('California', 2010),
('New York', 2000), ('New York', 2010),
('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
18976457, 19378102,
20851820, 25145561]
pop = pd.Series(populations, index=index)
index = pd.MultiIndex.from_tuples(index)
#print(pop.reindex(index))
pop_df = pd.DataFrame({'total': pop,'under18': [9267089, 9284094,4687374, 4318033,5906301,6879014],
                       'random':[1,2,3,4,67,65]})
print(pop_df)