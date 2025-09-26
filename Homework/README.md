# NOTES

## [Homework 1]()



## [Homework 2]()

The equation is a quadratic equation $ax² + bx + c = 0$, which is the variable of a, b, and c cannot be equal as 0. To find the solution of x, we can do it by the rules.<br>
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

## [Homework 3]()



## [Homework 4]()



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
The rules itself is $b/a or b * a^{-1}$. For example if we take a = GF(5, 2) and b = GF(5, 3), so the a is 2 and we need find the operation of $2 * x = 1 (mod 5)$. The eligible number only 6, which means we will take 3. At the result itself will be $3 * 3 = 9 = 4 (mod 5).$

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