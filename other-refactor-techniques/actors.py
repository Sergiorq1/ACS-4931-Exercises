# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

class Person:
    def __init__(self, first_name, last_name, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.email = email
    def send_hiring_email(self):
        print("email sent to: ", self.email)
    def print_info_after_1985(self):
        if self.birth_year < 1985:
            return 
        print(self.first_name, self.last_name)
        print('Movies Played: ', end='')
        for m in movies[i]:
            print(m, end=', ')
    
for i in range(len(first_names)):
    new_person = Person(first_names[i], last_names[i], birth_year[i], emails[i])
    new_person.print_info_after_1985()
    new_person.send_hiring_email()


    

