sandwich_orders = ['veggie',  'pastrami', 'grilled cheese', 'turkey',   'pastrami','roast beef',  'pastrami']
finished_sandwiches = []


while 'veggie' in sandwich_orders:
    sandwich_orders.remove('veggie')

while sandwich_orders:
    current_sandwize=sandwich_orders.pop()
    print("I am working on your current " +current_sandwize)
    finished_sandwiches.append(current_sandwize)

for sandwich in finished_sandwiches:
    print(sandwich)