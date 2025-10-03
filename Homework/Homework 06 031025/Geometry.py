import math
from dataclasses import dataclass

EPS = 1e-9

@dataclass
class Point:
    x: float
    y: float
    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"

class Line:
    # store line in ax + by = c
    def __init__(self, a: float, b: float, c: float):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def __repr__(self):
        return f"{self.a:.2f} x + {self.b:.2f} y = {self.c:.2f}"

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

# ---------- functions ----------
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

def intersect_line_circle(L, C):
    a,b,c = L.a,L.b,L.c
    # foot of center to line

    t = (a*C.h+b*C.k+c)/(a*a+b*b)
    x0 = C.h - a*t
    y0 = C.k - b*t

    d = math.hypot(x0-C.h, y0-C.k)
    if d > C.r+EPS: 
        return "No intersection"
    
    if abs(d-C.r) < EPS: 
        return [Point(x0,y0)]
    h = math.sqrt(C.r**2 - d**2)
    vx,vy = -b, a
    l = math.hypot(vx,vy)
    vx,vy = vx/l, vy/l
    return [Point(x0+vx*h, y0+vy*h), Point(x0-vx*h, y0-vy*h)]

def get_perpendicular_line(L, P):
    a,b,c = L.a,L.b,L.c
    # perpendicular line: -b x + a y + c2 = 0
    a2,b2 = -b,a
    c2 = -(a2*P.x+b2*P.y)
    Q = intersect_two_lines(L, Line(a2,b2,c2))
    return {"perpendicular_line":Line(a2,b2,c2), "foot_of_perpendicular":Q}

# ---------- main tests ----------
if __name__ == "__main__":
    L_a = Line(2, 3, 6)
    L_b = Line(4, -3, 6)
    print("1. 兩直線交點測試:")
    print(f"   {L_a} 和 {L_b}: {intersect_two_lines(L_a, L_b)}")

    L_c = Line(1, 1, 1)
    L_d = Line(2, 2, 5)
    print(f"   {L_c} 和 {L_d}: {intersect_two_lines(L_c, L_d)}")

    L_e = Line(1, 1, 1)
    L_f = Line(2, 2, 2)
    print(f"   {L_e} 和 {L_f}: {intersect_two_lines(L_e, L_f)}\n")

 
    C_g = Circle(-2, 0, -8) 
    C_h = Circle(2, 0, -8)
    print("2. 兩個圓交點測試:")
    print(f"   {C_g} 和 {C_h}: {intersect_two_circles(C_g, C_h)}\n")

 
    C_i = Circle(0, 0, -25) 
    L_j = Line(2, -1, 5)
    print("3. 直線與圓交點測試:")
    print(f"   {L_j} 和 {C_i}: {intersect_line_circle(L_j, C_i)}")

    L_k = Line(1, 0, 5) 
    print(f"   {L_k} 和 {C_i} (切線): {intersect_line_circle(L_k, C_i)}")

    L_l = Line(1, 0, 10)
    print(f"   {L_l} 和 {C_i} (不相交): {intersect_line_circle(L_l, C_i)}\n")


    L_m = Line(2, 3, 6)
    P_n = Point(5, 4)
    result = get_perpendicular_line(L_m, P_n)

    print("4. 過線外一點作垂直線測試:")
    print(f"   原直線 L: {L_m}")
    print(f"   線外點 P: {P_n}")
    print(f"   垂直線 L_perp: {result['perpendicular_line']}")
    print(f"   垂足 Q (交點): {result['foot_of_perpendicular']}")

