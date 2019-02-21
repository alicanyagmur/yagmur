import numpy as np

a = np.floor(10*np.random.random((3,4))) # floor float olan veriyinin ondalık kısmını atar.

print(a)
print(a.shape) # dizi yapısını bize gösterir.

print(a.ravel()) # ürettiği dizinin listesini bize verir. sadece gösterirken düzleştirdi a'yı değiştirmedi.

a = a.ravel()
print(a)

print(a.shape) # tek boyut olduğunu ve 12 elemanlı olduğunu gösteriyor.

print(a.reshape(2,6))
a = a.reshape(2,6)
print(a.T) #transfors etti. yani yapıyı 90 derece yana çevirerek listelenmiş gösteriyor.

print(a.reshape(2,-1)) # buradaki -1'in anlamı bana 2 satır oluştur eleman sayısını otomatik belirler ama tam bölünmesi gerekiyor. Tam bölünmezse hata verir.