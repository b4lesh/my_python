def num_pi(x):
    from math import pi
    return f"{pi:.{x}f}"


x = int(input('x: '))
print(num_pi(x))
