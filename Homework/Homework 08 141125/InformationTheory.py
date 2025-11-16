import math
import numpy as np

def probability_10000():
    p = 0.5
    n = 10000
    return p**n # probability of 10000

def log_p_pow_n(p=0.5, n=10000):
    return n * math.log(p) # ln (natural log)

def entropy(p):
    return -sum(pi * math.log(pi, 2) for pi in p)

def cross_entropy(p, q):
    return -sum(p[i] * math.log(q[i], 2) for i in range(len(p)))

def kl_divergence(p, q):
    return sum(p[i] * math.log(p[i] / q[i], 2) for i in range(len(p)))

def mutual_information(p_xy):
    p_xy = np.array(p_xy)
    p_x = np.sum(p_xy, axis=1, keepdims=True)   # marginal p(x)
    p_y = np.sum(p_xy, axis=0, keepdims=True)   # marginal p(y)
    
    mask = p_xy > 0
    
    return np.sum(p_xy[mask] * np.log2(p_xy[mask] / (p_x * p_y)[mask])) #entro

def verify_cross_entropy_property(p, q):
    H_pp = cross_entropy(p, p)
    H_pq = cross_entropy(p, q)
    return H_pp, H_pq, (H_pp < H_pq) #verify

def hamming74_encode(d):
    """Input: 4 bit [d1,d2,d3,d4], Output: 7 bit Hamming code"""
    d1, d2, d3, d4 = d
    
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    
    return [p1, p2, d1, p3, d2, d3, d4]

def hamming74_decode(code):
    """Decode + correct 1-bit error"""
    p1, p2, d1, p3, d2, d3, d4 = code
    
    # syndrome bits
    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4
    
    error_pos = s1*1 + s2*2 + s3*4     # position error (1–7)
    
    if error_pos != 0:
        code[error_pos - 1] ^= 1       # fix code
    
    # return 4 bit data asli
    return [code[2], code[4], code[5], code[6]]

if __name__ == "__main__":
    
    print("Number 1")
    print("P(10000 heads) =", probability_10000())
    
    print("\nNumber 2")
    print("log(0.5^10000) =", log_p_pow_n())
    
    print("\nNumber 3")
    p = [1/6, 1/3, 1/3, 1/6]
    q = [1/8, 1/4, 1/4, 3/8]
    print("entropy(p) =", entropy(p))
    print("cross_entropy(p,q) =", cross_entropy(p,q))
    print("KL(p||q) =", kl_divergence(p,q))
    
    p_xy = [[0.25, 0.0],
            [0.0, 0.75]]
    print("Mutual Information =", mutual_information(p_xy))
    
    print("\nNumber 4")
    Hpp, Hpq, result = verify_cross_entropy_property(p, q)
    print("H(p,p) =", Hpp)
    print("H(p,q) =", Hpq)
    print("H(p,p) < H(p,q)?", result)
    
    print("\nNumber 5")
    data = [1,0,1,1]
    encoded = hamming74_encode(data)
    print("Encoded =", encoded)
    
    encoded_with_error = encoded.copy()
    encoded_with_error[3] ^= 1
    print("With error =", encoded_with_error)
    
    decoded = hamming74_decode(encoded_with_error)
    print("Decoded =", decoded)