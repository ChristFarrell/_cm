import sympy as sp

# Define variables
x, y, z = sp.symbols('x y z', real=True)

# Define vector field F (F = (x^2 y, y^2 z, z^2 x))
F = sp.Matrix([
    x**2 * y,
    y**2 * z,
    z**2 * x
])

# Gradient of a scalar field (f = x^2 y + y z^2)
f = x**2 * y + y * z**2

grad_f = sp.Matrix([
    sp.diff(f, x),
    sp.diff(f, y),
    sp.diff(f, z)
])

# Divergence of vector field F
div_F = sp.diff(F[0], x) + sp.diff(F[1], y) + sp.diff(F[2], z)

# Curl of vector field F
curl_F = sp.Matrix([
    sp.diff(F[2], y) - sp.diff(F[1], z),
    sp.diff(F[0], z) - sp.diff(F[2], x),
    sp.diff(F[1], x) - sp.diff(F[0], y),
])

# Evaluate all at point (1,2,3)
pt = {x:1, y:2, z:3}

grad_val = grad_f.subs(pt)
div_val  = div_F.subs(pt)
curl_val = curl_F.subs(pt)

print("Gradient ∇f =", grad_f)
print("Gradient at (1,2,3) =", grad_val)

print("\nDivergence ∇·F =", div_F)
print("Divergence at (1,2,3) =", div_val)

print("\nCurl ∇ x F =", curl_F)
print("Curl at (1,2,3) =", curl_val)
