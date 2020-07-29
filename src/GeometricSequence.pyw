"""
Engine for Geometric Sequence
"""

from NumberProgressions import GeometricSequence

__base__: float # beginning sequence variable, `a_1`
__iterator__: float # current sequence iterator, `n`
__ratio__: float # sequence ratio variable, `r`
__current__: float # saved state for current value at iterator
__previous__: float # saved state for previous value at iterator

# initialize engine
def init(base: float = 0, ratio: float = 0):
    global __base__, __iterator__, __ratio__, __current__, __previous__
    __base__ = base
    __iterator__ = 0
    __ratio__ = ratio
    __current__ = __base__
    
# flush memory
def flush():
    global __base__, __iterator__, __ratio__, __current__, __previous__
    del __base__, __iterator__, __ratio__, __current__, __previous__
    
# reset to iterator 0
def reset():
    global __base__, __iterator__, __ratio__, __current__, __previous__
    __iterator__ = 0
    __current__ = GeometricSequence(__base__, __iterator__, __ratio__)
    del __previous__

# use a normal iteration from base library
def normal(base: float, iterator: float, ratio: float):
    return GeometricSequence(base, iterator, ratio)

# iterate forward once
def next():
    global __iterator__, __ratio__, __current__, __previous__
    __previous__ = __current__
    __current__ = GeometricSequence(__base__, __iterator__, __ratio__)
    __iterator__ += 1
    return __current__

# iterate backward once
def back():
    global __iterator__, __ratio__, __current__, __previous__
    __previous__ = __current__
    __current__ = GeometricSequence(__base__, __iterator__, __ratio__)
    __iterator__ -= 1
    return __current__

# iterate at present
def now():
    global __current__
    return __current__

# iterate to a certain iteration state
def jump(iterator: float):
    global __base__, __iterator__, __ratio__, __current__, __previous__
    __iterator__ = iterator
    __current__ = GeometricSequence(__base__, __iterator__, __ratio__)
    __previous__ = GeometricSequence(__base__, __iterator__ - 1, __ratio__)
    return __current__

# shift to certain iterator state
def seek(iterator: float):
    global __base__, __iterator__, __ratio__, __current__, __previous__
    __iterator__ = iterator
    __current__ = GeometricSequence(__base__, __iterator__, __ratio__)
    __previous__ = GeometricSequence(__base__, __iterator__ - 1, __ratio__)
    
# instantly use geometric sequence
def use(base: float, iterator: float, ratio: float):
    global __base__, __iterator__, __ratio__, __current__, __previous__
    __base__ = base
    __iterator__ = iterator
    __ratio__ = ratio
    __current__ = GeometricSequence(__base__, __iterator__, __ratio__)
    __previous__ = GeometricSequence(__base__, __iterator__ - 1, __ratio__)
    return __current__
