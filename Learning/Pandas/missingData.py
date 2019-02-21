import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv'
data = pd.read_csv(url)

print(data)
print("**************************************")
print(data.columns)
print("**************************************")
print(data[["City","State", "Colors Reported"]].head())
print("**************************************")

print(data.isnull().head()) # boşmu diye soruyoruz.
print("**************************************")
print(data.notnull().head()) # veri var mı diye soruyor.
print("**************************************")
print(data.isnull().sum())
print("**************************************")
print(data[data.City.isnull()]) # city boş olanları listeledik.