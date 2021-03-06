class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
                "{} order to {}".format(order, self.name))

c=Contact("Abeer","abeer@gmail.com")
s=Supplier("Azad","azad@gmail.com")
print(c.email,c.name,s.name,s.email)
print(s.order("Wife"))
print([c.name for c in Contact.all_contacts.search('Abeer')])