def is_triangle(a, b, c):
    """The method should return true if a triangle can be built with the sides of given length 
    and false in any other case.In this case, all triangles must have surface greater than 0 to be accepted."""
    
    return (a > abs(b - c)) and (a < b + c)
