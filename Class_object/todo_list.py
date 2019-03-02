from todo_object import Todo

class Works:
    def __init__(self):
        self.work_list=[]
    def add_works(self,works,tags=''):
        self.work_list.append(Todo(works,tags))
    def _find_work(self,works_id):
        for work in self.work_list:
            if str(work.id)== str(works_id):
                return work
        return None
    def modify_works(self,work_id,works):
        work=self._find_work(work_id)
        if work:
           work.works=works
    def search(self,filter):
        return [work for work in self.work_list if
                work.match(filter)]


'''work_1=Works()
work_1.add_works("Visit to Jamuna")
print(work_1.work_list[0].works)
print(work_1.search('Jamunaa'))'''