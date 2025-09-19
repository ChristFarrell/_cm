import cmath

def root2(a, b, c):
    D = b**2 - 4*a*c
    
    r1 = (-b + cmath.sqrt(D)) / (2*a)
    r2 = (-b - cmath.sqrt(D)) / (2*a)
    
    return r1, r2

print(root2(1, -3, 2))
print(root2(1, 2, 1))    
print(root2(1, 1, 1))    
