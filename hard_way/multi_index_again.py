import numpy as np
import random
import pandas as pd
index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2, 3]])
data = pd.Series(np.random.rand(9), index=index, )
data.index.names = ['char', 'int']
pop = pd.DataFrame({'Match': index,'Value': data })
print(pop)