# NOTES

## [Homework 1](https://github.com/ChristFarrell/_cm/blob/main/Homework/Homework%2001%20190925/Calculus.py)

This task determine of derivative definition and the fundamental theorem of calculus.<br>
The first part, we asked to solve the derivative approximation. By using h = 0.00001, at x=3, for f(x) = $x^{4}$, the result is 108.0005..., which is very close with the exact answer that is 108.<br>

The second part, we asked to solve the integral approximation, with upper limit of integration is 3 and lower limit of integration is 0. The result for integral approximation of $x^{4}$ is 48.5959..., which is very close with the exact answer that is 48.6.<br>

The last part, we asked to checking fundamental theorem of calculus. With using of x = 3, we can found that the r = 81.00..., which is very close with the exact answer that is f(3) = 81.<br>

At the end, every calculation that python do was correct and always very close with the exact answer for the question.

## [Homework 2](https://github.com/ChristFarrell/_cm/blob/main/Homework/Homework%2002%20190925/Algebra.py)

This equation is a quadratic equation $ax² + bx + c = 0$, which is the variable of a, b, and c cannot be equal as 0. To find the solution of x, we can do it by the rules.<br>
<br>
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$<br>

At the end we using some of the example of x and get the result.
```python
print(root2(1, -5, 6)) # x = 3 & 2
print(root2(1, 4, 3))  # x = -1 & -3  
print(root2(1, 1, 1))  # x = -0.5 + 0.86j & -0.5 - 0.86j
```

## [Homework 3](https://github.com/ChristFarrell/_cm/blob/main/Homework/Homework%2003%20190925/AlgebraAdvance.py)

This question is a cubic equation $ax³ + bx² + c + d = 0$. By this equation, we can sure that all of variable cannot be equal as 0.<br>

The first step, we using normalization of formula, which make variable a will be 1.
```python
b /= a; c /= a; d /= a
```

The second step, we make depressed cubic, that will make result to remove x² term. We using formula $x = t - \frac{b}{3}$. This will makeBy the end, the formula will simplified as $t³ + pt + q = 0$.<br>

The third step, we use discriminant. It will decide whether Δ > 0 ; Δ = 0 ; Δ < 0.<br>
If Δ > 0 = one real root, two complex.<br>
If Δ = 0 = multiple real roots (at least two equal).<br>
If Δ < 0 = three distinct real roots.<br>

The fourth step, we using Cardano’s cube roots from the depressed equation. The solution will be t = u + v.
```python
u = (-q/2 + cmath.sqrt(Δ))**(1/3)
v = (-q/2 - cmath.sqrt(Δ))**(1/3)
```

At the end, it will be calculate the variable of t1, t2, t3. We also shift back the answer to gives the actual solutions of the equation.
```python
return [t1 - b/3, t2 - b/3, t3 - b/3]
```

Here some of result the calculation of cubic equation.
```python
print(solve_cubic(1, -6, 11, -6)) # x = 3, 2, 1
print(solve_cubic(1, -9, 26, -24)) # x = 4, 3, 2
```

## [Homework 4](https://github.com/ChristFarrell/_cm/blob/main/Homework/Homework%2004%20190925/CaseOfAlgebra.py)

This question is asked to solve the equation with the power of x > 5. As we know from the Galois theorem, we cannot solve the equation with the power of x > 5, but by approaching through matrix eigenvalues, coded python can find the value of the equation x whose power is more than 5.<br>

The first part, we just only simplified the equation and remove some not important numbers, so it can more easily to solve the equation.<br>

The second part we use the same way with normalization of formula, which make variable a will be 1.
```python
c = [ci / c[-1] for ci in c]   # make leading coeff = 1
```

The third part, we using some special formula that actually contradicts Galois theorem but can solving the number of x. On the matrix, we have eigenvalue number on there. Eigenvalue is a characteristic scalar value that represents the scale factor by which a vector changes when multiplied by a matrix. Through this proof, it is concluded that the eigenvalues ​​are equal to the roots of the polynomial equation.<br>

We can use example of equation $x⁶ - 21x⁵ + 175x⁴ - 735x³ + 1624x² - 1764x + 720$. The result of matrix will be like this.
```
| 0   0   0   0   0  -720 |
| 1   0   0   0   0  1764 |
| 0   1   0   0   0 -1624 |
| 0   0   1   0   0   735 |
| 0   0   0   1   0  -175 |
| 0   0   0   0   1    21 |
```

```python
# companion matrix
    companion = np.zeros((n, n))
    companion[1:, :-1] = np.eye(n-1)
    companion[:, -1] = -np.array(c[:-1])

# eigenvalue = akar polinomial
    roots = np.linalg.eigvals(companion)
    return roots
```

Here some of result the calculation of equation.
```python
coeffs = [-24, 26, -9, 1] 
print(root(coeffs)) # x = 2, 3, 4

coeffs = [720, -1764, 1624, -735, 175, -21, 1] 
print(root(coeffs)) # x = 1, 2, 3, 4, 5, 6
```

## [Homework 5](https://github.com/ChristFarrell/_cm/blob/main/Homework/Homework%2005%20260925/GaloisField.py)

A finite field (Galois field) is a finite set (its number of elements is finite). This process is equipped with addition and multiplication operations, which satisfy all the axioms of the field. The numbers that finite field uses is a prime number (2, 3, 5, 7, 9, 11, etc).

The code that I used was a bit simple because the proof is also only through true and false.
The code start from checking the p or modulus number.
```python
def __init__(self, p, value):
        if p <= 1:
            raise ValueError("p must be a prime > 1")
        self.p = p
        self.value = value % p  # always keep inside [0, p-1]
```
A finite field only exists if its modulus is a prime number p > 1. If p = 0, 1, or a negative number, the field is invalid. All element values ​​must be changed to always be within the range [0, p-1]. For example if FiniteField(5, 7) → 7 % 5 = 2, so the value is 2.

After checking, there will be operation of mathematics.
```python
def __add__(self, other):
        self._check_same_field(other)
        return GF(self.p, (self.value + other.value) % self.p)
```
For the multiplication, we using (__add__). For the subtraction, we using (__sub__). For the multiplication, we using (__mul__) The operation itself it's still same, using (+, -, x). After finish the operation, it will continue to look for the modulus.

For the division, we use different rule.
```python 
def __truediv__(self, other):
    self._check_same_field(other)
    if other.value == 0:
        raise ZeroDivisionError("cannot divide by zero in a field")
    inv = pow(other.value, -1, self.p)  # multiplicative inverse mod p
    return GF(self.p, (self.value * inv) % self.p)
```
The rules itself is b/a or $b \cdot a^{-1}$. For example if we take a = GF(5, 2) and b = GF(5, 3), so the a is 2 and we need find the operation of $2 * x = 1 (mod 5)$. The eligible number only 6 (2 * 3), which means we will take 3. At the result itself will be $3 * 3 = 9 = 4 (mod 5).$

For the (def __eq__), we will check for both of a and b, if both of them in the same field. For example if a=(5, 2), then the b=(5, 3). Both field was same in 5.

For the (def __repr__) and (def _check_same_field), the GF number will be printed and will be checked again as both must to be always in same field.

After we finish the operation of mathemathics, we will continue to do the simple proofing of our operation. The proofing including 3 categories: Distributivity, Addition forms a group, and Multiplication forms a group.

For the distributivity, we using rules of $A * ( B + C ) = ( A * B ) + ( A * C )$
```python
def check_distributivity(p):
    for a in range(p):
        for b in range(p):
            for c in range(p):
                A, B, C = GF(p, a), GF(p, b), GF(p, c)
                if not (A * (B + C) == (A * B) + (A * C)):
                    return False
    return True
```
We can check it by testing using the mod = 5. Check with a=2, b=3, c=4:<br>
Left: $2 * (3+4) = 2 * 7 ≡ 2 * 2 = 4 (mod 5).$<br>
Right: $2 * 3 + 2 * 4 = 6 + 8 ≡ 1 + 3 = 4 (mod 5).$

At the end, the distributivity is fullfill.

For the Addition from a group and Multiplication from a group, we using same of 5 operations.
```python
def check_addition_group(p):
    elements = [GF(p, x) for x in range(p)]
    zero = GF(p, 0)

    # closure
    for a in elements:
        for b in elements:
            if (a + b) not in elements:
                return False

~(and another 4)

def check_multiplication_group(p):
    elements = [GF(p, x) for x in range(1, p)]  # exclude 0
    one = GF(p, 1)

    # closure
    for a in elements:
        for b in elements:
            if (a * b) not in elements:
                return False

~(and another 4)
```
On this section, there will be 5 section to be checked as addition group. Closure, Associativity, Commutativity, Identity, and Inverse. If all of the section is true, it means both of Addition and Multiplication of group are fullfill.

At the end, the result will be printed:
```python
if __name__ == "__main__":
    a = GF(5, 2)
    b = GF(5, 3)
    print("a =", a)
    print("b =", b)
    print("a+b =", a+b) # GF(5, 0)  (2+3=5 ≡ 0 mod 5)
    print("a*b =", a*b) # GF(5, 1)  (2*3=6 ≡ 1 mod 5)
    print("b-a =", b-a) # GF(5, 1)  (3-2=1 mod 5)
    print("b/a =", b/a) # GF(5, 4)  (3 * inverse of 2 mod 5 = 3*3=9 ≡ 4 mod 5)

    print("Distributivity in GF(5):", check_distributivity(5))
    print("Addition forms a group in GF(5):", check_addition_group(5))
    print("Multiplication (without 0) forms a group in GF(5):", check_multiplication_group(5))
```