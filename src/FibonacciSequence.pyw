"""
Engine for Fibonacci Series
"""

from NumberProgressions import FibonacciSequence

__memory__: list # will hold all the used variables
__supported__: float # variable to hold current size of __memory__, signifies the current supported iterator states
__iterator__: float # Iteration State variable
__current__: float # holder current iteration
__previous__: float # holder previous number

# assigns values to __memory__
def __assign__(iterator: float):
    global __memory__
    if iterator <= 1:
        __memory__[iterator] = 1
    else:
        __memory__[iterator] = __memory__[iterator  - 1] + __memory__[iterator - 2]

# automatically assigns data to __memory__ based on argument iterator state
def __auto__(iterator: float):
    global __memory__, __supported__
    if iterator > __supported__:
        for i in range(0, int(iterator - __supported__)):
            __memory__.append(float)
            __assign__(__supported__ + i)
        __supported__ = iterator
    else:
        return

# initialize engine
def init(support: float = 15):
    global __memory__, __supported__, __iterator__, __current__, __previous__
    __memory__ = list()
    __supported__ = 0
    __auto__(support)
    __iterator__ = 0
    __current__ = __memory__[__iterator__]
    __previous__ = float()

# flush memory
def flush():
    global __memory__, __supported__, __iterator__, __current__, __previous__
    del __memory__, __supported__, __iterator__, __current__, __previous__
    
