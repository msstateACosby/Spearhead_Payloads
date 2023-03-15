#Tuple Math Lib
"""
'tuple_lib'
============================

Tuple aka vector math library, provides basic vector functions and common use operations
 * Author:

============================
"""
### Tuple by-element functions
def add(tuple1: tuple, tuple2: tuple) -> tuple:
    """Add second tuple to first tuple by element"""
    return (tuple1[0]+tuple2[0],tuple1[1]+tuple2[1],tuple1[2]+tuple2[2])

def sub(tuple1: tuple, tuple2: tuple) -> tuple:
    """Subtract second tuple from first tuple by element"""
    return (tuple1[0]-tuple2[0],tuple1[1]-tuple2[1],tuple1[2]-tuple2[2])

def mult(tuple1: tuple, tuple2: tuple) -> tuple:
    """Multiply first and second tuple by element"""
    return (tuple1[0]*tuple2[0],tuple1[1]*tuple2[1],tuple1[2]*tuple2[2])

def div(tuple1: tuple, tuple2: tuple) -> tuple:
    """Divide first tuple by second tuple by element"""
    return (0 if tuple1[0]==0 or tuple2[0]==0 else tuple1[0]/tuple2[0],0 if tuple1[1]==0 or tuple2[1]==0 else tuple1[1]/tuple2[1],0 if tuple1[2]==0 or tuple2[2]==0 else tuple1[2]/tuple2[2])

### Scalar on tuple functions
def addScalar(scalar: float | int, tuple1: tuple) -> tuple:
    """Add scalar to each element of tuple"""
    return (tuple1[0]+scalar,tuple1[1]+scalar,tuple1[2]+scalar)

def subScalar(scalar: float | int, tuple1: tuple) -> tuple:
    """Subtract scalar from each element of tuple"""
    return (tuple1[0]-scalar,tuple1[1]-scalar,tuple1[2]-scalar)

def multScalar(scalar: float | int, tuple1: tuple) -> tuple:
    """Multiply tuple elements by scalar"""
    return (tuple1[0]*scalar,tuple1[1]*scalar,tuple1[2]*scalar)

def divScalar(scalar: float | int, tuple1: tuple) -> tuple:
    """Divide tuple elements by scalar"""
    return (0 if tuple1[0] == 0 else tuple1[0]/scalar,0 if tuple1[1] == 0 else tuple1[1]/scalar,0 if tuple1[2] == 0 else tuple1[2]/scalar)

### Common operation functions
def mag(tuple1: tuple) -> float:
    """Magnitude of a tuple"""
    return (tuple1[0]**2 + tuple1[1]**2 + tuple1[2]**2)**0.5

def unit(tuple1: tuple) -> tuple:
    """Unit vector"""
    return divScalar(mag(tuple1),tuple1)

def dot(tuple1: tuple, tuple2: tuple) -> float:
    """Dot product of tuples 1 and 2"""
    return (tuple1[0]*tuple2[0]) + (tuple1[1]*tuple2[1]) + (tuple1[2]*tuple2[2])

def cross(tuple1: tuple, tuple2: tuple) -> tuple:
    """Cross product of tuple1 X tuple2, tuple1 is first item"""
    return (((tuple1[1]*tuple2[2]) - (tuple1[2]*tuple2[1])), -((tuple1[0]*tuple2[2])-(tuple1[2]*tuple2[0])), ((tuple1[0]*tuple2[1])-(tuple1[1]*tuple2[0])))

def projScalar(tuple1: tuple, tuple2: tuple) -> float:
    """Scalar of the projection of tuple1 on tuple2"""
    dotp = dot(tuple1,tuple2)
    magp = mag(tuple2)
    return (0 if dotp==0 or magp==0 else dotp/magp)

def proj(tuple1: tuple, tuple2:tuple) -> tuple:
    """Tuple of the projection of tuple1 on tuple2"""
    dotp = dot(tuple1,tuple2)
    magp = mag(tuple2)
    scalar = dotp/(magp**2)
    return multScalar(scalar, tuple2)