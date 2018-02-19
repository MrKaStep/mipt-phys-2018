#!/usr/bin/python3
from math import *

n = 10
t = [43.565, 43.559, 43.502, 43.532, 43.585, 43.590, 43.585]
t2 = [43.693, 43.600]
tav = sum(t) / len(t)
sigmat = sqrt(sum(map(lambda x : (x - tav)**2, t)) / len(t))
T = tav / n
# print(T)
# print(sigmat)

N = sigmat / (0.005 * T)

N = 5

# print(N)

tau > 200

z_0 = 2149 # +- 20
R = 114.6 # +- 0.5
r = 30.2 # +- 0.3
m_empty = 1066.8 # +- 0.5

g = 9.8 # +- 0.1

k = g*r*R / (4 * pi**2 * z_0)
print(k)

t_empty = 21.774

m_brick = 1075.1 # +- 0.1
t_brick = 18.778
T_brick = t_brick / N

I_brick = k * m_brick * T_brick ** 2
print(I_brick)

m_ring = 821.1 # +- 0.1
t_ring = 21.129
T_ring = t_ring / N

I_ring = k * m_ring * T_ring ** 2
# print(I_ring)

t_hat = 19.568
T_hat = t_hat / N
m_hat = 580.6 # +- 0.1

t_disk = [15.500, 15.694, 15.719, 15.789, 15.930, 16.228, 16.521, 16.835, 17.227, 17.663, 18.087, 18.672, 19.203, 19.643, 20.419, 21.006, 21.582]

t_brick_ring = 19.117
