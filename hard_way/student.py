class Student:

    def __init__(self,name,major,gpa,is_on_probation):
        self.name=name
        self.major=major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


student_1=Student('Abeer Azad','CSE',2.68,False)

print(student_1.name)