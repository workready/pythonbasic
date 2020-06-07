import argparse
import numpy

# Tu código aquí: construye un procesador de argumentos de entrada usando argparse.ArgumentParser

# Parse the command line
arguments = parser.parse_args()

# Create the graph
# Matplotlib is slow to load so put it here to not delay the parsing
import matplotlib.pyplot as pyplot

npts = arguments.npts
limit = arguments.limit
x = numpy.linspace(-1.0*limit, limit, npts)

# Run through the Chebyshev polynomials
M = arguments.min
N = arguments.max + 1
for order in range(M,N):
    y = numpy.where(
        numpy.abs(x) < 1.0,
        numpy.cos(order*numpy.arccos(x)),
        numpy.where(
            x > 0.0,
            numpy.cosh(order*numpy.arccosh(x)),
            (-1.0)**order*numpy.cosh(order*numpy.arccosh(numpy.abs(x)))
            )
        )

    pyplot.plot(x,y)

if arguments.title:
    pyplot.suptitle(arguments.title)

f = arguments.file
pyplot.savefig(f)
f.close()

