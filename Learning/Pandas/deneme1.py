import pandas as pd

notlar = pd.read_csv("grades.csv")

print(notlar)
print(type(notlar))

print("**************************************")
print(notlar.head())
print("**************************************")
print(notlar.tail())
print("**************************************")

notlar.columns = ["İsim", "Soyisim", "SSN", "Test1", "Test2", "Test3", "Test4", "Final", "Sonuc"]
print(notlar["Final"])
print("**************************************")
print(notlar.iloc[2])
print("**************************************")
print(notlar[1:7])