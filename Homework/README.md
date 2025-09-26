# NOTES

## [Homework 1]()



## [Homework 2]()



## [Homework 3]()



## [Homework 4]()



## [Homework 5]()

A finite field (Galois field) is a finite set (its number of elements is finite). This process is equipped with addition and multiplication operations, which satisfy all the axioms of the field. The numbers that finite field uses is a prime number (2,3,5,7,9,11,etc).

The code that I used was a bit simple because the proof is also only through true and false.
```python
def __init__(self, p, value):
        if p <= 1:
            raise ValueError("p must be a prime > 1")
        self.p = p
        self.value = value % p  # always keep inside [0, p-1]

