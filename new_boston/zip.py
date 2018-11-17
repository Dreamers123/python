first_name=['Abeer','Lisa','Jannat']
last_name=['Azad','Biswas','Ferdaous']
dict={
    'Google':800.00,
    'Facebook':677.89,
    'Twitter':697.9,
    'Youtube':745.88
}
print(max(zip(dict.values(),dict.keys())))

name=zip(first_name,last_name)
for a,b in name:
    print(a,b)