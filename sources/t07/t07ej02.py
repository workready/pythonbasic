# Lo mismo que map pero con una list comprehension
def upper(s):
    return s.upper()

print(" ".join([s.upper() for s in ['escribir', 'en', 'mayúsculas', 'se', 'considera', 'vocear']]))