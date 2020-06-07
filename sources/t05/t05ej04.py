import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="Muestra el número que le hayamos pasado elevado al cuadrado", type=int) # <1>
args = parser.parse_args()
print(args.square**2)
