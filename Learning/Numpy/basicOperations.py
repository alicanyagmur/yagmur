import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

print(a)
print(b)

c = a-b
print(c) # satır ve sutunlara göre çıkartıyor yani 20den0 30dan1 40dan2 50den3 çıkartmış oldu.
print(a*b) # elementwise product denir yani her bir element çarpımını verir 20*0  30*1 40*2 50*3 sonucunu verdi
print(a@b) # matrix çarpımını verir.
print(a.dot(b))  # matrix çarpımını verir.

d = b**3
print(d)

e = 10*np.sin(a)
print(e<7)



f = np.ones((2,4))
print(f)
g = np.zeros((2,4))
print(g)
h = np.random.random((2,4))
print(h)

i = np.sum(b)
print(i)
print(b.sum())
j = np.min(b)
print(j)
k = np.max(b)
print(k)
l = np.sqrt(b)
print(l)