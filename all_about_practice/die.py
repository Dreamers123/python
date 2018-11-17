from random import randint
import pygal

class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll_die(self):
        return randint(1, self.num_sides)

die_1=Die()
die_2=Die()
results=[]

for num_roll in range(100):
    result=die_1.roll_die()+die_2.roll_die()
    results.append(result)
print(results)


frequencies=[]

for frequency in range(1,13):
    frequency=results.count(frequency)
    frequencies.append(frequency)
print(frequencies)
hist = pygal.Bar()
max_result = die_1.num_sides + die_2.num_sides
hist.title = "Results of rolling two D6 1000 times."

hist.x_labels = [str(x) for x in range(2, max_result+1)]


hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual.svg')
