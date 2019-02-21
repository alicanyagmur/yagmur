# dizinin indexinci değerine gitme
import numpy as np

sayilar = np.array([0,5,10,15,20,25,30])

print(sayilar[3])
print(sayilar[0:3])
#şuana kadar tek dimension tek boyutlu olanlarda çalıştık

sayilar2 = np.array([[0,5,10],[15,20,25]])

print(sayilar2[0])
print(sayilar2[0][1])
print(sayilar2[0,1])
print(sayilar2[:,1]) # tüm satırların 1. indexini verir
print(sayilar2[:,0:2]) # tüm satılardan 0 dan 2. indexe kadar ama 2 dahil değil
print(sayilar[::-1]) # array'ı tersten dizer
print(sayilar2[-1,:]) # en son satırdaki bütün sutunların verilerini aldık
print(sayilar2[:,-1]) # tüm satırların son sutununu verir