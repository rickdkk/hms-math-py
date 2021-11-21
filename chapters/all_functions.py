import numpy as np
import sympy as smp
from IPython.core.display import display


# Chapter 2
def display_and_diff(func, *, symbols=None, n: int = 1, simplify: bool = False):
    """Convenience function that takes an equation and displays the equation and it's derivative"""
    print("The following equation is given:")
    display(func)

    derivatives = []
    for _ in range(n):
        func = smp.diff(func, symbols) if symbols is not None else smp.diff(func)
        print("The derivative of this equation is equal to:")
        display(func)

        if simplify:
            func = func.simplify()
            print("Simplified, this is equal to:")
            display(func)
        derivatives.append(func)
    return func if n == 1 else derivatives


# Chapter 3
def display_and_integrate(func, *, symbols=None, unpack: bool = False):
    """Convenience function that takes an equation and displays it and its integrals"""
    print("The equation given is:")
    display(func)
    if symbols is not None and not unpack:
        integral = smp.integrate(func, symbols)
    elif symbols is not None and unpack:
        integral = smp.integrate(func, *symbols)
    else:
        integral = smp.integrate(func)

    print("Its integral is equal to:")
    display(integral)
    return integral


# Chapter 5
def cartesian_to_polar(x_coord, y_coord, z_coord=None, degrees=False):
    """Converts cartesian (x, y, z) coords to polar coordinates (r, θ, ϕ) or (x, y) to (r, ϕ)"""
    if two_dimensional := z_coord is None:
        z_coord = np.zeros_like(x_coord)

    r = np.sqrt(x_coord ** 2 + y_coord ** 2 + z_coord ** 2)
    theta = np.arctan2(z_coord, np.sqrt(x_coord ** 2 + y_coord ** 2))
    phi = np.arctan2(y_coord, x_coord)

    if degrees:
        theta = np.degrees(theta)
        phi = np.degrees(phi)
    return (r, phi) if two_dimensional else (r, theta, phi)


def polar_to_cartesian(r, angle1, angle2=None, degrees=False):
    """Converts polar coordinates (r, θ, ϕ) to cartesian coordinates (x, y, z) or (r, ϕ) to (x, y)"""
    if two_dimensional := angle2 is None:
        angle2 = np.zeros_like(r)
        angle1, angle2 = angle2, angle1  # swap θ and ϕ

    if degrees:
        angle1 = np.radians(angle1)
        angle2 = np.radians(angle2)

    x_coord = r * np.cos(angle1) * np.cos(angle2)
    y_coord = r * np.cos(angle1) * np.sin(angle2)
    z_coord = r * np.sin(angle1)
    return (x_coord, y_coord) if two_dimensional else (x_coord, y_coord, z_coord)


def cartesian_to_cilinder(x_coord, y_coord, z_coord, degrees=False):
    """Converts cartesian (x, y, z) coords to cilinder coordinates (r, θ, z)"""
    r = np.sqrt(x_coord**2 + y_coord**2)
    phi = np.arctan2(y_coord, x_coord)
    phi = np.degrees(phi) if degrees else phi
    return r, phi, z_coord.copy()


def cilinder_to_cartesian(r, phi, z_coord, degrees=False):
    """Converts cilinder coordinates (r, θ, z) coords to cartesian (x, y, z)"""
    phi = np.radians(phi) if degrees else phi
    x_coord = r * np.cos(phi)
    y_coord = r * np.sin(phi)
    return x_coord, y_coord, z_coord.copy()
