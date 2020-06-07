# Mala practica: formateador antiguo
def format_user_info(name, age, sex):
     return "Nombre: %s, Edad: %d, Sexo: %s" % (name, age, sex)

print(format_user_info("Jorge", 36, "Hombre"))