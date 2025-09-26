h = 0.00001

def df(f, x):
    return (f(x+h)-f(x))/h

def integral(f, a, b):
    x = a
    area = 0
    while x < b:
        area += f(x)*h
        x += h
    return area

def theorem1(f, x):
    r = df(lambda x:integral(f, 0, x), x)
    print('r =', r, 'f(x) =', f(x))
    print('abs(r-f(x))<0.01 = ', abs(r-f(x))<0.01)
    assert abs(r-f(x))<0.01

def f(x):
    return x**4

print('df(f,3)=', df(f,3))
print('integral(f, 0, 3)=', integral(f, 0, 3))
theorem1(f, 3)