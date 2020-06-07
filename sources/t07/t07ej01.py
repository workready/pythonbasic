# Uso básico de la función map
def upper(s):
    return s.upper()

print(" ".join(
	map(
		upper,
		['escribir', 'en', 'mayúsculas', 'se', 'considera', 'vocear']
		)
	))