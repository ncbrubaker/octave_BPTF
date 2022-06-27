function [add sub mult div fac] = compute(x, y)
    add = x + y
    sub = x - y
    mult = x * y
    div = x / y
    fac = factorial(x) + factorial(y)