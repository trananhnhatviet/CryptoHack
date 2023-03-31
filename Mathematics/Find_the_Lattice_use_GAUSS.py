import numpy as np
from Crypto.Util.number import getPrime, inverse, bytes_to_long,long_to_bytes



def dot(u, v):
    return np.sum([ux*vx for ux, vx in zip(u, v)])



def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m


def gauss(v1, v2):
    while True:
        if dot(v1, v1) > dot(v2, v2):
            v1, v2 = v2, v1
        m = dot(v1, v2) // dot(v1, v1)
        if m == 0:
            return v1, v2
        v2 = [v2x-m*v1x for v1x, v2x in zip(v1, v2)]


q, h = (7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257,
        2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800)
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

u = [1,h]
v = [0,q]

a,b = gauss(u,v)
f = a[0]
g = a[1]
print(long_to_bytes(decrypt(q,h,f,g,e)))



