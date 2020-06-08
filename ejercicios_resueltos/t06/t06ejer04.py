# Excepciones. Definelas aqui
class DuplicatedUsernameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class UnderageError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

# Clase para almacenar los datos de los usuarios: nombre, edad y email

class User:
    def __init__(self, username, age, email):
        self.username = username
        self.age = age
        self.email = email

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if int(a) < 0:
            raise InvalidAgeError("La edad no puede ser menor que cero")
        elif int(a) < 18:
            raise UnderageError("El usario es menor de 18 años")
        else:
            self._age = int(a)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, e):
        if '@' not in e:
            raise InvalidEmailError("El email no tiene un formato correcto")
        else:
            self._email = e


    def __str__(self):
        return "{} is {} years old and has the email {}".format(self.username, self.age, self.email)

example_list = [
    ("jane", "jane@example.com", 21),
    ("bob", "bob@example", 19),
    ("jane", "jane2@example.com", 25),
    ("steve", "steve@somewhere", 15),
    ("joe", "joe", 23),
    ("anna", "anna@example.com", -3),
]

directory = {}

for username, email, age in example_list:
    try:
        if username in directory.keys():
            raise DuplicatedUsernameError("El usuario {} ya existe".format(username))
        
        directory[username] = User(username, age, email)
    except Exception as e:
        print(e)

for username, u in directory.items():
    print("{} => {}".format(username, u))