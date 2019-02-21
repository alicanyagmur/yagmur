import numpy as np

a = np.floor(10*np.random.random((2,3)))
b = np.floor(10*np.random.random((2,3)))

print(a)
print(b)

c= np.vstack((a,b))  # 2 diziyi alt altta getirerek dizdi.
print(c)

d = np.hstack((a,b)) # 2 dizideki satırları birleştirir.
print(d)