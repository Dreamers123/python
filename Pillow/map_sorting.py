import heapq
from collections import Counter
income=[10,25,40,723,5876,38,546,65,765]
text="I am Abeer,I am a good boy,I do good work but I love porn I I I"
word=text.split()
counter=Counter(word)
print(counter.most_common(3))
def IncomeIncrease(dollars):
    return dollars* 2

new_income=list(map(IncomeIncrease,income))
print(new_income)
sorted=heapq.nlargest(3,income)
print(sorted)
stocks=[{'name':'Abeer' ,'prize':720},
        {'name':'Lisa' ,'prize':903},
        {'name':'Esika' ,'prize':30},
        {'name':'Swara' ,'prize':397},
        {'name':'Anika' ,'prize':765}
]
St_sort=heapq.nsmallest(2,stocks,key=lambda stocks:stocks['prize'])
print((St_sort))