# Uso de operator + functools
import operator, functools

print(functools.reduce(operator.concat, ['BER', 'BER', 'ECHO']))    # BERBERECHO