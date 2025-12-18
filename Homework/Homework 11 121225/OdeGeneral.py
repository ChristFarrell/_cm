import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    roots = np.roots(coefficients)

    solution_parts = []
    C_index = 1
    used = set()

    for r in roots:
        if tuple(np.round([r.real, r.imag], 10)) in used:
            continue

        # Count (multiplicity)
        multiplicity = 0
        for rr in roots:
            if np.isclose(r, rr):
                multiplicity += 1

        used.add(tuple(np.round([r.real, r.imag], 10)))

        a = r.real    # real
        b = r.imag    # imaginary

        # real
        if np.isclose(b, 0):
            for m in range(multiplicity):
                if m == 0:
                    term = f"C_{C_index} e^({a}x)"
                else:
                    power = f"x^{m}" if m > 1 else "x"
                    term = f"C_{C_index} {power} e^({a}x)"

                solution_parts.append(term)
                C_index += 1

        else: # imaginary
            for m in range(multiplicity):

                # Power for x^m
                if m == 0:
                    power = ""
                else:
                    power = f"x^{m} " if m > 1 else "x "

                # cos term
                term1 = f"C_{C_index} {power}e^({a}x) cos({abs(b)}x)"
                solution_parts.append(term1)
                C_index += 1

                # sin term
                term2 = f"C_{C_index} {power}e^({a}x) sin({abs(b)}x)"
                solution_parts.append(term2)
                C_index += 1

    return " + ".join(solution_parts)

# 範例測試 (1): 實數單根: y'' - 3y' + 2y = 0  特徵方程: lambda^2 - 3lambda + 2 = 0, 根: 1, 2
# 預期解: C_1e^(1x) + C_2e^(2x)
print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

# 範例測試 (2): 實數重根: y'' - 4y' + 4y = 0  特徵方程: lambda^2 - 4lambda + 4 = 0, 根: 2, 2
# 預期解: C_1e^(2x) + C_2xe^(2x)
print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

# 範例測試 (3): 複數共軛根: y'' + 4y = 0  特徵方程: lambda^2 + 4 = 0, 根: 2i, -2i (alpha=0, beta=2)
# 預期解: C_1cos(2x) + C_2sin(2x)
print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

# 範例測試 (4): 複數重根 (二重): (D^2 + 1)^2 y = 0  特徵方程: (lambda^2 + 1)^2 = 0, 根: i, i, -i, -i (alpha=0, beta=1, m=2)
# 預期解: C_1cos(1x) + C_2sin(1x) + C_3xcos(1x) + C_4xsin(1x)
print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

# 範例測試 (5): 高階混和根: y''' - 6y'' + 12y' - 8y = 0  特徵方程: (lambda - 2)^3 = 0, 根: 2, 2, 2
# 預期解: C_1e^(2x) + C_2xe^(2x) + C_3x^2e^(2x)
print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))