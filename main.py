import numpy as np

'''
Newton-Raphson
'''
newton_values = np.array([-1.6])
iterations = [] # Keeps track of iterations for Newton-Raphson and Bisection

# Function f(x)
def f(x):
    return x * np.sin(3 * x) - np.exp(x)

# Derivative function
def df(x):
    return np.sin(3 * x) + 3 * x * np.cos(3 * x) - np.exp(x)

for i in range(1000):
    y = f(newton_values[i])
    dfx = df(newton_values[i])
    newton_values = np.append(newton_values, newton_values[i] - (y / dfx))
    if abs(y) < 1e-6:
        iterations.append(i+1)
        break

'''
Bisection
'''
xl = -0.7; xr = -0.4
midpoints = [] # Keeps track of midpoints for bisection method
for i in range(0, 100):
    xc = (xl + xr)/2
    midpoints.append(xc)
    y = f(xc)
    if (y > 0):
        xl = xc
    else:
        xr = xc
    if abs(y) < 1e-6:
        iterations.append(i+1)
        break