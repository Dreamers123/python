income=[20,30,50]
a=25
b=50
c=a & b
d=c >> 2
def double_income(incomes):
    return incomes * 2

new_income=list(map(double_income,income))
print(new_income)
print(d)
