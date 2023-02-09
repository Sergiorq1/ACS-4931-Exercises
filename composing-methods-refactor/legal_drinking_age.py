# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.


class Person:
    def __init__(self, my_age):
        self.age = my_age
        self.LEGAL_DRINKING_AGE = 18
        
    def enter_night_club(self):
        if self.age >= self.LEGAL_DRINKING_AGE:
            print("You are at least 18 and are allowed to enter and drink")
        else:
            print("Entrance of minors is denied. Minor con not drink legally either")
  
person = Person(18)
person.enter_night_club()
        
