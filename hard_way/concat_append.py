import pandas as pd
import numpy as np
def make_df(cols, ind):
   data = {c: [str(c) + str(i) for i in ind ] for c in cols}
   return pd.DataFrame(data, ind)
# example DataFrame
#print(make_df('ABC', range(3)))
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
concat=(np.concatenate([x]))
x = [[1, 2],
[3, 4]]
df1 = make_df('AB', [1, 2])
df2 = make_df('CD', [3, 4])
#print(df1)
#print('-'*10)
df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
#print(df3);
# #print(df4);
#print(pd.concat([df3, df4], axis=1))
#print(np.concatenate([x, x], axis=1))



