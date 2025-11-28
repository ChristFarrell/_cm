import sympy as sp

x, y, z = sp.symbols('x y z', real=True)

# ==========================
# 2. LAPLACIAN FUNCTION
#    ∇²f = f_xx + f_yy + f_zz
# ==========================
def laplacian(f):
    return sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)

# ==========================
# 3. DEFINE A SURFACE (SCALAR FIELD)
#    Example:
#    f(x,y,z) = x^2 + y^2 + z^2
# ==========================
f = x**2 + y**2 + z**2

# Compute the Laplacian symbolically
lap_f = laplacian(f)

# ==========================
# 4. EVALUATE AT A POINT
# ==========================
point = {x: 1, y: 2, z: 3}
lap_value = lap_f.subs(point)

print("Scalar field f =", f)
print("Laplacian ∇²f =", lap_f)
print("Laplacian at point (1,2,3) =", lap_value)

# ==========================
# 5. INTERPRETATION
#    ∇²f > 0  → concave up (凹)
#    ∇²f < 0  → concave down (凸)
#    ∇²f = 0  → flat (平)
# ==========================
if lap_value > 0:
    print("Shape at the point: CONCAVE (凹)")
elif lap_value < 0:
    print("Shape at the point: CONVEX (凸)")
else:
    print("Shape at the point: FLAT (平)")
