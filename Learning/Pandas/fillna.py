import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv'
data = pd.read_csv(url)

print(data.isnull().sum())
print("**************************************")

print(data.shape)
print("**************************************")

print(data['Shape Reported'].value_counts(dropna=False)) # boş olanları drop etmiyor ve tamamen çalışıyor değerlere göre veriyor
# örneğin rengi belirtilmemiş  NaN = 2644 tane var  Light = 2803 tane var

print("**************************************")
data = pd.read_csv(url)

data['Shape Reported'].fillna(value='Belirsiz', inplace=True) # Null olan datayı belirsiz olarak yazdırdık yani NaN artık Belirsiz. inplace ilede bellekte olan değeri değiştiriyor.
print(data['Shape Reported'].value_counts(dropna=False))