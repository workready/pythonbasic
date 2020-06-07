# Excepciones. Definelas aqui


# Clase para almacenar los datos de los usuarios: nombre, edad y email

class User:
    pass    # Tu codigo aqui

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
        directory[username] = User(username, age, email)
    except Exception as e:
        print(e.message)


for username, u in directory.items():
    print("{} => {}".format(username, u))