import sympy as sy
import numpy as np

def fun_1( your_id):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate(sy.exp(-2*x**3), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,6,1,2,4,7,8,9,2,4], 
                   [1,2,5,9,7,1,2,2,9,7],
                   [5,9,7,8,4,1,2,5,2,6],
                   [8,5,7,4,6,9,2,1,3,0],
                   [5,1,0,2,4,7,8,5,9,2],
                   [7,4,1,3,1,2,5,4,6,9],
                   [1,3,5,4,9,7,5,4,2,6],
                   [1,5,7,1,2,3,6,4,5,8],
                   [5,2,5,4,6,9,7,8,3,3],
                   [5,4,5,4,6,0,1,7,9,6]
                   ])
    b = np.array([9,8,2,1,5,6,9,4,5,8])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1303350
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
