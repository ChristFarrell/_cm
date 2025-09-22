import cmath

def root3(a, b, c, d):
    if a == 0:
        raise ValueError("a cannot be 0")
    # normalisasi ke bentuk x^3 + px + q
    b_, c_, d_ = b/a, c/a, d/a
    p = c_ - b_**2/3
    q = 2*b_**3/27 - b_*c_/3 + d_
    Δ = (q/2)**2 + (p/3)**3
    
    u = (-q/2 + cmath.sqrt(Δ))**(1/3)
    v = (-q/2 - cmath.sqrt(Δ))**(1/3)
    x1 = u+v - b_/3
    ω = -0.5 + 0.5j*cmath.sqrt(3)
    x2 = u*ω + v*ω.conjugate() - b_/3
    x3 = u*ω.conjugate() + v*ω - b_/3
    return (x1, x2, x3)

print(root3(1, -6, 11, -6))
