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

## [Homework 6](https://github.com/ChristFarrell/_cm/blob/main/Homework/Homework%2006%20031025/Geometry.py)

This is the geometry python to do some test for the point, line, and circle. There are 4 test on this code: test for intersection of two lines, test for intersection of two circles, test for intersection of a line and a circle, and test for perpendicular line through a point outside the line.<br>

At first, we use point to represent poin of 2D (x,y) with using of dataclass.
```python
class Point:
    x: float
    y: float
    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"
```

Second, we use line to store the equation of ax + by = c
```python
class Line:
    # store line in ax + by = c
    def __init__(self, a: float, b: float, c: float):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def __repr__(self):
        return f"{self.a:.2f} x + {self.b:.2f} y = {self.c:.2f}"
```

Third, we use circle to receive the coefficients a,b,c from the general equation $x² + y² + ax + by + c = 0$, then convert it to center-radius form.
```python
class Circle:
    # equation: x^2 + y^2 + ax + by + c = 0
    def __init__(self, a: float, b: float, c: float):
        self.h = -a/2
        self.k = -b/2
        self.r2 = (a*a + b*b)/4 - c
        self.r = math.sqrt(self.r2) if self.r2 >= 0 else float("nan")
        self.a, self.b, self.c = float(a), float(b), float(c)

    def __repr__(self):
        return f"Circle(Center={Point(self.h, self.k)}, Radius={self.r:.4f})"
```
For the information:
- self.h and self.k are the main coordinat. We using the rule (h, k) = (-a/2 , -b/2).
- self.r2 = r², where the square radius of r² is (a² + b²)/4 - c.
- self r we use sqrt for the result of self.r2<br>

For example for the circle: If we have (0, 0, -25), it nmeans the main coordinat is (-0.0, -0.0), r2 = (0+0)/4 - (-25) = 25, which the radius is 5.<br>

Next, we start to do the fuctions to answer every part of questions and test. We start it with intersect of two lines.
```python
def intersect_two_lines(L1: Line, L2: Line):
    a1,b1,c1 = L1.a,L1.b,L1.c
    a2,b2,c2 = L2.a,L2.b,L2.c
    D = a1*b2 - a2*b1
    if abs(D) < EPS:
        # Lines are parallel or coincident
        if abs(a1*c2 - a2*c1) < EPS and abs(b1*c2 - b2*c1) < EPS:
            return "Coincident (infinite intersections)"
        else:
            return "Parallel (no intersection)"
    # Unique intersection
    x = (c1*b2 - c2*b1)/D
    y = (a1*c2 - a2*c1)/D
    return Point(x,y)
```
For the first question, the print answer will print 3 possibility of lines. First is coincident (infinite intersections), second is parallel (no intersection), and the last is unique intersection. On this part, it is work by receiving the equation of $ax + by = c$. Then the coefficient for a, b, and c will be taken and bring to the formula of determinant.<br>

The determinant rules is $D = a1 ∗ b2 - a2 ∗ b1$<br>
If D ≠ 0 it means  the lines intersect at one point.<br>
If D = 0 it means the lines are parallel or coincident.<br>

For D = 0, we use Cramer rules to find the unique intersection point. We can find it by using:
```python
x = (c1*b2 - c2*b1)/D
y = (a1*c2 - a2*c1)/D
```

If the result is parallel or coincident, we need test it by have<br> 
$a1 ∗ ​c2 ​− a2 ∗​ c1 ​= 0 and b1 ∗ ​c2 ​− b2 ∗ ​c1 ​= 0$.<br>

If both answer same, we can sure that the both equation will have coincident (infinite intersections), otherwise the equation will have parallel (no intersection). Examples of figures can be seen below.<br>

For the second part, we will find the intersection of two circles
```python
def intersect_two_circles(C1, C2):
    dx,dy = C2.h-C1.h, C2.k-C1.k
    d = math.hypot(dx,dy)
    if d > C1.r+C2.r or d < abs(C1.r-C2.r) or d < EPS:
        return "No intersection"
    
    a = (C1.r**2 - C2.r**2 + d*d) / (2*d)
    h = math.sqrt(max(0,C1.r**2 - a*a))

    xm = C1.h + a*dx/d
    ym = C1.k + a*dy/d

    rx, ry = -dy*(h/d), dx*(h/d)

    if abs(h) < EPS:
        return [Point(xm,ym)]
    return [Point(xm+rx, ym+ry), Point(xm-rx, ym-ry)]
```
This section begins by calculating the distance between the center of circle C1 and circle C2. Next, the condition of the circle is checked.<br>
d > r1 + r2     = centers too far, the circles do not meet.<br>
d < |r1 - r2|   = one circle is inside the other but does not touch.<br>
d < EPS         = the formula fails<br>

Next, we search for the projection points, until we find the midpoint. (xm, ym) is the point in the middle between 2 points where the circle intersects. (ym, ry) is the orthogonal vector. At the end, it will print 2 different of point. Examples of figures can be seen below.<br>

For the third part, we will find the intersection of a line and a circle.
```python
def intersect_line_circle(L, C):
    a,b,c = L.a,L.b,L.c
    # foot of center to line

    t = (a*C.h+b*C.k+c)/(a*a+b*b)
    x0 = C.h - a*t
    y0 = C.k - b*t

    d = math.hypot(x0-C.h, y0-C.k)
    if d > C.r+EPS: 
        return "No intersection"
```
This section begins by finding the projection point of the center of the circle onto the line (x0, y0). Next, using the formula d, we will determine the distance between the center (h, k) and the perpendicular point (x0, y0). If d > r, then there is no intersection. If d = 0, then the line touches the circle at one point.<br>

```python
if abs(d-C.r) < EPS: 
        return [Point(x0,y0)]
    h = math.sqrt(C.r**2 - d**2)
    vx,vy = -b, a
    l = math.hypot(vx,vy)
    vx,vy = vx/l, vy/l
    return [Point(x0+vx*h, y0+vy*h), Point(x0-vx*h, y0-vy*h)]
```
But, if d < r, This will give two points of intersection, so a shift of the projection point (x0, y0) is carried out to determine the two points of intersection of the circle-line. Examples of figures can be seen below.<br>

For the last part, we will find perpendicular line.
```python
def get_perpendicular_line(L, P):
    a,b,c = L.a,L.b,L.c
    # perpendicular line: -b x + a y + c2 = 0
    a2,b2 = -b,a
    c2 = -(a2*P.x+b2*P.y)
    Q = intersect_two_lines(L, Line(a2,b2,c2))
    return {"perpendicular_line":Line(a2,b2,c2), "foot_of_perpendicular":Q}
```
From the equation of ax + by = c, we will take the (a,b) variable. Since we want to find a perpendicular line, we have to rotate it 90°, so it turns from (a,b) to (-b,a). At the end, the perpendicular equation will be -bx + ay + c = 0.<br>

Next, we will get provide the number of P = (x,y). Later we will substitute the x and y to perpendicular equation, so we will get the result for variable c. The equation itself will be same for -bc + ay + c = 0. At the end, we have two different equation. First equation of line and the perpendicular equatiuon.<br>

By finding that, we can finish the equation using of elimination methods to finding the result for foot of perpendicular (Q), by finding the number of x and y. Examples of figures can be seen below.<br>

At the last part, we will start to do the calculation of geometry. First we will try to find the intersection of two lines. We can see the example in below.
```python
if __name__ == "__main__":
    L_a = Line(2, 3, 6)
    L_b = Line(4, -3, 6)
    print("1. 兩直線交點測試:")
    print(f"   {L_a} 和 {L_b}: {intersect_two_lines(L_a, L_b)}")

    L_c = Line(1, 1, 1)
    L_d = Line(2, 2, 5)
    print(f"   {L_c} 和 {L_d}: {intersect_two_lines(L_c, L_d)}")
```
For example the equation of $2x + 3y = 6 & 4x - 3y = 6$<br>
D = 2 * (-3) - 4 * 3 = -18 (use Cramer rule to find the unique point)<br>
```python
x point
x = (c1*b2 - c2*b1) / D
x = (6*(-3) - 6*3) / -18
x = 2

y point
y = (a1*c2 - a2*c1) / D
y = (2*6 - 4*6) / -18
y = 2/3 ≈ 0.67

# So the point (2 , 0.67)
```

For equation of $x + y = 1 and 2x + 2y = 5$<br>
D = 1 * 2 - 2 * 1 = 0 (Checking lines)<br>
```python
a1c2 - a2c1 = 1 * 5 - 2 * 1 = 3
b1c2 - b2c1 = 1 * 5 - 2 * 1 = 3

# So it is Infinite intersections (lines are coincident)
```

Second, we will find the intersection of two circles.
```python
C_g = Circle(-2, 0, -8) 
C_h = Circle(2, 0, -8)
    print("2. 兩個圓交點測試:")
    print(f"   {C_g} 和 {C_h}: {intersect_two_circles(C_g, C_h)}\n")
```
From there we can know 2 equation for x^2 + y^2 - 2x - 8 = 0 and x^2 + y^2 + 2x - 8 = 0. Both circles are centered at (1,0) and (-1,0) with radius 3. If we completed the equation, by using equation 1 = equation 2, we will find the point of x, which is 0. The 0 will be substitute to euqation and there will be 2 different points for y (-2.83 and 2.83). At the end, here the result.
```python
 # Circle(Center=Point(1.00, 0.00), Radius=3.0000) 和 Circle(Center=Point(-1.00, 0.00), Radius=3.0000): [Point(0.00, -2.83), Point(0.00, 2.83)]
```

Third, we will find the intersection of a line.
```python
C_i = Circle(0, 0, -25) 
L_l = Line(1, 0, 10)
    print(f"   {L_l} 和 {C_i} (不相交): {intersect_line_circle(L_l, C_i)}\n")
```
From there, we can know that<br>
a = 1, b = 0, c = -10 (a*x + b*y + c = 0)<br>
h = 0, k = 0, r = 5<br>

From the t = (a*C.h+b*C.k+c)/(a*a+b*b), we can know the t = -10, so x0 = 10 and y0 = 0 (x0, y0) = (10, 0). We remember that from the equation of circle, the r will be 5. Since of that, we found that d = 10 and r = 5. So d > r. At the end, here the result.
```python
 # 1.00 x + 0.00 y = 10.00 和 Circle(Center=Point(0.00, 0.00), Radius=5.0000) (不相交): No intersection
```

Last, we will find the perpendicular line through a point outside the line.
```python
L_m = Line(2, 3, 6)
P_n = Point(5, 4)
    result = get_perpendicular_line(L_m, P_n)
```
From there, we know the a = 2, b = 3, c = 6, P.x = 5, P.y = 4. Then we use rule c2 = -(a2*P.x+b2*P.y) =−((−3)(5)+(2)(4)) = 7.<br>

Because it is perpendicular, (a,b) becomes (-b,a), which the result of equation is -3x + 2y = 7. Lastly, we just need find the Q.<br>

For equation of $2x + 3y = 6 & -3x + 2y = 7$<br>
D = 2 * 2 - (-3)(3) = 13<br>
```python
x point
x = (c1*b2 - c2*b1) / D
x = (6*2 - 7*3) / 13
x = -9/13 ≈ -0.69

y point
y = (a1*c2 - a2*c1) / D
y = (2*7 - (-3)*6) / 13
y = 32/13 ≈ 2.46

# So the point (-0.69, 2.46)
```

At the end, here the result.
```python
# 原直線 L: 2.00 x + 3.00 y = 6.00 (Starting line)
# 線外點 P: Point(5.00, 4.00) (Outer point)
# 垂直線 L_perp: -3.00 x + 2.00 y = 7.00 (Perpendicular line)
# 垂足 Q (交點): Point(-0.69, 2.46) (Legs perpendicular)
```

All from input test number, already used by the code of Teacher.