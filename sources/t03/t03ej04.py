# Buena practica: formateador nuevo
def format_user_info(name, age, sex):
     return "Nombre:{0}, Edad: {1}, Sexo: {2}".format(name, age, sex)

print(format_user_info("Jorge", 36, "Hombre"))