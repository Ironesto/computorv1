#!/usr/bin/env python3
import cmath
import sys
import re
import math

def main():
    if len(sys.argv) > 1:
        equation = sys.argv[1]
    else:
        equation = input("Introduce una ecuación: ")

    left, right = equation.split("=")
    left_poly = parse_side(left)
    right_poly = parse_side(right)

    reduced = subtract_poly(left_poly, right_poly)

    print("Reduced form:")
    for power in sorted(reduced):
        coef = reduced[power]
        print(str(coef) + " * X^" + str(power))
    degree = get_polynomial_degree(reduced)
    print(f"Polynomial degree: {degree}")

    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    elif degree == 0:
        solve_degree_zero(reduced)
    elif degree == 1:
        solve_degree_one(reduced)
    elif degree == 2:
        solve_degree_two(reduced)


def parse_side(side):
    side = side.replace(" ", "")
    if side[0] not in "+-":
        side = "+" + side

    terms = re.findall(r'([+-])([\d\.]+)\*X\^(\d+)', side)

    poly = {}

    for sign, coef, power in terms:
        coef = int(coef)
        power = int(power)
        if sign == '-':
            coef = -coef
        if power in poly:
            poly[power] += coef
        else:
            poly[power] = coef

    return poly

def subtract_poly(left, right):
    result = left.copy()
    for power, coef in right.items():
        if power in result:
            result[power] -= coef
        else:
            result[power] = -coef
    return result

def get_polynomial_degree(poly):
    non_zero_degrees = [deg for deg, coef in poly.items() if coef != 0]
    return max(non_zero_degrees, default=0)

def solve_degree_zero(poly):
    c = poly.get(0, 0)
    if c == 0:
        print("Any real number is a solution.")
    else:
        print("No solution.")

def solve_degree_one(poly):
    a = poly.get(1, 0)
    b = poly.get(0, 0)
    if a == 0:
        print("No solution.")
    else:
        solution = -b / a
        print("The solution is:")
        print(solution)

def solve_degree_two(poly):
    a = poly.get(2, 0)
    b = poly.get(1, 0)
    c = poly.get(0, 0)
    discriminant = b ** 2 - 4 * a * c # esto es Δ = b² - 4ac

    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        sqrt_d = math.sqrt(discriminant)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        print(x1)
        print(x2)
    elif discriminant == 0:
        print("Discriminant is zero, the solution is:")
        x = -b / (2 * a)
        print(x)
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        sqrt_d = cmath.sqrt(discriminant)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        print(x1)
        print(x2)

if __name__ == "__main__":
    main()
