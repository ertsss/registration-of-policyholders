class Person:
    def __init__(self, firstname, surname, age, number):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.number = number

    def __str__(self):
        return "{firstname}\t{surname}\t{age}\t{number}".format(firstname=self.firstname, surname=self.surname, age=self.age, number=self.number)
