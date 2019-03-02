import datetime

last_id = 0

class Todo:

    def __init__(self, works, tags=''):

        self.works = works
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    def match(self,filter):
        return filter in self.works or filter in self.tags
'''work_1=Todo("Buy a sandel")
print(work_1.works);'''