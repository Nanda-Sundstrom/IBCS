import math
def f(n):
    return n * (n + 1) // 2
print(f(10))

def solve_quadratic(a, b, c):
    """
    Returns the solutions to the quadratic to the eqation ax^2 + bx + c = 0
    
    Args:
    :param a: coefficient of x^2
    :param b: coefficient of x
    :param c: constant

    Returns:
    List of solutions
    """
    D=b**2 - 4*a*c #discriminant
    if D < 0:
        return[]
    #now we know D >= 0
    if D == 0: #we can also use elif
        return[-b / (2*a)]
    #now we know that D > 0
    else:
        return[(-b + math.sqrt(D)) / (2*a), (-b - math.sqrt(D)) / (2*a)]
    #or return[(-b + m*math.sqrt(D) / (2*a) for m in [1, -1])]

print(solve_quadratic(1, 0, -1)) #a=1, c=-1, x**2 - 1 = 0
help(solve_quadratic)

