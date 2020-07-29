"""
Module Containing Necessary Mathematical Functions for Numerical Progression

Currently Supports:
* Arithmetic Sequence
* Geometric Sequence
* Fibonacci Sequence

"""

def ArithmeticSequence(a_1: float, n: float, d: float):
    return (a_1 + ((n - 1) *d))

def GeometricSequence(a_1: float, n: float, r: float):
    return (a_1 * pow(r, n - 1))

def FibonacciSequence(n: float):
    if n <= 1:
        return n
    else:
        return FibonacciSequence(n - 1) + FibonacciSequence(n - 2)
