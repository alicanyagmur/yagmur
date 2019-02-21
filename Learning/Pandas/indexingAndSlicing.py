import pandas as pd

notlar = pd.read_csv("grades.csv")

notlar.columns = ["İsim", "Soyisim", "SSN", "Test1", "Test2", "Test3", "Test4", "Final", "Sonuc"]

print(notlar)
print("**************************************")
print(notlar.loc[1])
print("**************************************")
print(notlar.loc[:,"İsim"])
print("**************************************")
print(notlar.loc[:5,"İsim"])
print("**************************************")
print(notlar.loc[:5,"İsim":"Test4"])
#Pandasta indexleme ve slicing yaparken girilen değerler dahil olur yukardaki 5e kadar değil de 5 dahil olur.
#Eğer belli bir stunu almak istiyorsakta [ ] içinde , ile eklemek gerekir.

print("**************************************")
print(notlar.loc[:5,["İsim","Soyisim","Final","Sonuc"]])


print("**************************************")
print(notlar.loc[:5,:"SSN"]) # en baştan SSN ye kadar getirir

print("**************************************")
print(notlar.loc[::-1,:"SSN"]) # tersten listeleyerek SSN ye kadar verir.