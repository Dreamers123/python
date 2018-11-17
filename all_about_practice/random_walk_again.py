from random import choice

class RamdomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points

        self.x_values=[0]
        self.y_values=[0]

    def get_step(self):

        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4,5,6,7,8])
        step = direction * distance
        return step

    def fillwalk(self):
        while len(self.x_values) < self.num_points:
            x_step=self.get_step()
            y_step=self.get_step()

            if x_step==0 and y_step==0:
               continue
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
