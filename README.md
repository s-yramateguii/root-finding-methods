# Root Finding Using Newton-Raphson and Bisection Methods

This Python script implements two numerical methods—**Newton-Raphson** and **Bisection**—to approximate the root of $$f(x)=0$$

## Problem Definition
The target function \( f(x) \) is defined as:
<p align="center">
  $$ f(x) = x \sin(3x) - e^x $$
</p>

### Derivative of \( f(x) \)
The derivative \( f'(x) \), required for Newton-Raphson, is:
<p align="center">
  $$ f'(x) = \sin(3x) + 3x \cos(3x) - e^x $$
</p>

## Methods

### 1. Newton-Raphson Method
- Starts with an initial guess $$x_0 = -1.6$$.
- Uses the formula: $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
- Stops iterating when $$|f(x)| < 10^{-6}$$ or after 1000 iterations.

### 2. Bisection Method
- Starts with an interval $$[x_l, x_r] = [-0.7, -0.4]$$.
- Iteratively refines the midpoint \( x_c \) of the interval:
  $$x_c = \frac{x_l + x_r}{2}$$
- Stops when $$|f(x)| < 10^{-6}$$ or after 100 iterations.

## Outputs
- **Newton-Raphson:** 
  - Approximated root stored in `newton_values`.
  - Total iterations to convergence stored in `iterations`.
- **Bisection:** 
  - Approximated midpoints stored in `midpoints`.
  - Total iterations to convergence stored in `iterations`.
