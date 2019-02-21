import pandas as pd
import numpy as np

data = np.array(["Ali", "Nina" , "Alina"])
s = pd.Series(data) # bana datanın serisini oluşturdu. Pandasın indexleme yaparak listeliyor. Bundan dolayıda pandas indexler sayesinde hızlıdır.
z = pd.Series(data, index=[1,2,3]) # indexi bizde verebiliriz ama eşdeğer sayıda olması zorunlu

print(s)
print(z)

data2 = {"Matematik":10, "Fizik":20, "Beden eğitimi": 100 }
s2 = pd.Series(data2) # burada indexte verebiliriz.
z2 = pd.Series(data2, index=["Fizik","beden", "Matematik"]) # string olduğunda eş değer olması gerekir.
print(s2)
print(z2)
print(z2[0])
print(z2["Matematik"])



s3 = pd.Series(5,index=[1,2,3]) # index sayısı fazla olması sorun çıkartmaz. Aynı veriyi onlarada kopyalar.

print(s3)

