import sys
from todo_list import Works

class Menu:
    def __init__(self):
        self.work_menu=Works()
        self.choices={
                "1": self.show_works,
                "2": self.search_works,
                "3": self.add_work,
                "4": self.modify_work,
                "5": self.quit
                }
    def display_menu(self):
        print("""
Workbook Menu

1. Show all Works
2. Search Works
3. Add Work
4. Modify Work
5. Quit
""")
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    def add_work(self):
        work=input("Enter a Work: ")
        self.work_menu.add_works(work)
        print("Your work has been added.")
    def search_works(self):
        filter=input("Enter the work: ")
        work=self.work_menu.search(filter)
        self.show_works(work)
    def modify_work(self):
        work_id=input("Enter Work ID: ")
        works=input("Enter Modified work: ")
        if works:
            self.work_menu.modify_works(work_id,works)
    def show_works(self,works=None):
       if not works:
        works=self.work_menu.work_list
       for work in works:
           print("{0}: {1}\n{2}".format(
                work.id, work.tags, work.works))
    def quit(self):
        print("Thank you for using your Workbook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
