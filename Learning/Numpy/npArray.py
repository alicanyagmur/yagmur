import numpy as np

#a = np.arange(1,10)

#a = np.array(1,3,5,6,8,9) # bu bir fonksiyon olduğu için 6 tane parametre olarak gönderiliyor gibi

a = np.array([1,3,5,7,9,11]) # bu şekilde [ ] tek bir parametre göndermiş gibi olduk.

print(a)
print(a.dtype) #numpy hepsini aynı anda çalışır yani float olursa bütün hepsi floattır.
print(a.ndim)


b = np.array([[1,3],[5,7],[9,11]]) # bize 3 satır 2 sutundan oluşan 2 boyutlu bir array hazırladı.
print(b)
print(b.ndim)


# b deki arrayi  b = b.reshape(3,2) olarak