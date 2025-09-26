class GF:
    def __init__(self, p, value):
        if p <= 1:
            raise ValueError("p must be a prime > 1")
        self.p = p
        self.value = value % p  # always keep inside [0, p-1]

    def __add__(self, other):
        self._check_same_field(other)
        return GF(self.p, (self.value + other.value) % self.p)

    def __sub__(self, other):
        self._check_same_field(other)
        return GF(self.p, (self.value - other.value) % self.p)

    def __mul__(self, other):
        self._check_same_field(other)
        return GF(self.p, (self.value * other.value) % self.p)

    def __truediv__(self, other):
        self._check_same_field(other)
        if other.value == 0:
            raise ZeroDivisionError("cannot divide by zero in a field")
        inv = pow(other.value, -1, self.p)  # multiplicative inverse mod p
        return GF(self.p, (self.value * inv) % self.p)

    def __eq__(self, other):
        return isinstance(other, GF) and self.p == other.p and self.value == other.value

    def __repr__(self):
        return f"GF({self.p}, {self.value})"

    def _check_same_field(self, other):
        if not isinstance(other, GF) or self.p != other.p:
            raise ValueError("Elements must be from the same finite field")


# --- Verification ---
def check_distributivity(p):
    for a in range(p):
        for b in range(p):
            for c in range(p):
                A, B, C = GF(p, a), GF(p, b), GF(p, c)
                if not (A * (B + C) == (A * B) + (A * C)):
                    return False
    return True


def check_addition_group(p):
    elements = [GF(p, x) for x in range(p)]
    zero = GF(p, 0)

    # closure
    for a in elements:
        for b in elements:
            if (a + b) not in elements:
                return False

    # associativity
    for a in elements:
        for b in elements:
            for c in elements:
                if (a + (b + c)) != ((a + b) + c):
                    return False

    # commutativity
    for a in elements:
        for b in elements:
            if a + b != b + a:
                return False

    # identity
    for a in elements:
        if not (a + zero == a and zero + a == a):
            return False

    # inverses
    for a in elements:
        if not any(a + b == zero for b in elements):
            return False

    return True


def check_multiplication_group(p):
    elements = [GF(p, x) for x in range(1, p)]  # exclude 0
    one = GF(p, 1)
    # closure
    for a in elements:
        for b in elements:
            if (a * b) not in elements:
                return False

    # associativity
    for a in elements:
        for b in elements:
            for c in elements:
                if (a * (b * c)) != ((a * b) * c):
                    return False

    # commutativity
    for a in elements:
        for b in elements:
            if a * b != b * a:
                return False
            
    # identity
    for a in elements:
        if not (a * one == a and one * a == a):
            return False
    # inverses
    for a in elements:
        if not any(a * b == one for b in elements):
            return False
    return True


# --- Demo ---
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