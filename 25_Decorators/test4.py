class Person(object):
    def __init__(self, first_name, last_name):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name


    @property
    def full_name(self):
        """return the full name"""
        return "%s %s" % (self.first_name, self.last_name)


person = Person("Mahedi", "Hasan")
print(person.full_name)
print(person.first_name)
person.first_name = "New"
print(person.full_name)