def f(x):
    return x**3 - 4*x - 9


def bisection(a, b, tol=0.001, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs. Please choose a and b such that they bracket a root.")
    

    iterations = 0
    while (b - a) >= tol and iterations < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0:
            a = b = c
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1

    root_approx = (a + b) / 2.0
    return root_approx, iterations, b - a


a = 2
b = 3

try:
    root, iterations, width = bisection(a, b)
    print(f'Root approximation: {root:.6f}')
    print(f'Number of iterations: {iterations}')
    print(f'Final interval width: {width:.6f}')
except ValueError as err:
    print(err)

