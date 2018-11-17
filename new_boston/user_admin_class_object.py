class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
       # print("  Login_attempts: " + str(self.login_attempts))

    def increament_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
     super(). __init__(first_name, last_name, username, email, location)
     self.previlages=Previlages()

class Previlages():
    def __init__(self, privileges=[]):
        self.privileges=privileges
    def show_privileges(self):
        if(self.privileges):
           print("The privileges are:")
           for privilege in self.privileges:
               print('\t'+privilege)
        else:
            print("No privilage to show")

u1=Admin('Abeer','Azad','Dreamer','ab@gmail.com','Dhaka')
u1.describe_user()
u1.previlages.privileges=['Can have sex','can get blow','can press her tits']
u1.previlages.show_privileges()
u1.increament_login_attempts()
u1.reset_login_attempts()
