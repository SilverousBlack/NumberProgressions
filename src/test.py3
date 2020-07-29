import ArithmeticSequence
import GeometricSequence
import FibonacciSequence

# iterate 5 times
base = 2
ratio = 2
difference = 2

FibonacciSequence.init(100)

for i in range(0, 100):
    iterator = i + 1
    arith = ArithmeticSequence.use(base, iterator, difference)
    geo = GeometricSequence.use(base, iterator, ratio)
    print("{0}: {1:.0f} | {2:.0f} | {3:.0f}".format(iterator, arith, geo, fib))
    