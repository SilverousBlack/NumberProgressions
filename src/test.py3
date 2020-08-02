import ArithmeticSequence
import GeometricSequence
import FibonacciSequence

# iterate 5 times
base = 2
ratio = 2
difference = 2

for i in range(0, 100):
    iterator = i + 1
    arith = ArithmeticSequence.use(base, iterator, difference)
    geo = GeometricSequence.use(base, iterator, ratio)
    fib = FibonacciSequence.use(iterator)
    print("{0}: {1} | {2} | {3}".format(iterator, arith, geo, fib))
    