import numpy as np

a = np.arange(10)
print(a)

b = a

print(a[2])
print(b[2])

b[0]=0
print(a)
print(b)
# A'nın referansını aldığı için b de değişiklik yaparsak a'da değişiklik yapmış oluyoruz.

c = a.copy()
c[0]= 1000
print(c)
print(a)

# aynı data ile farklı matrixlerde çalışmak istersek view kullanmamız gerekiyor. datalar aynı boyutlar farklı
d = a.view()
print("********")
print(a)
print(d)
d[0] = 250
print(a)
print(d)
# örneğin d yi shape etmek istiyorum

d.shape = 2,5
print(a)
print(d)