from math import floor
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
def pascals_triangle(n):
    triangle=[]
    fact_n=factorial(n)
    for r in range(n+1):
        entry=fact_n / (factorial((n-r))*factorial(r))
        triangle.append(floor(entry))
    return triangle

print(pascals_triangle(7))
