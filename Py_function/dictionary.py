import  pprint

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
 print('Enter a name: (blank to quit)')
 name = input()
 if name == '':
   break
 if name in birthdays:
  print(birthdays[name] + ' is the birthday of ' + name)
 else:
  print('I do not have birthday information for ' + name)
  print('What is their birthday?')
  bday = input()
  birthdays[name] = bday
  print('Birthday database updated.')
for name in birthdays.keys():
    print(name)
for value in birthdays.values():
    print(value)
for items in birthdays.items():
    print(items)
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
 count.setdefault(character, 0)
 count[character] = count[character] + 1
pprint.pprint(count)