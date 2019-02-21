import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv'
data = pd.read_csv(url)

print(data.isnull().sum())
print("**************************************")

print(data.shape)
print("**************************************")

data = data.dropna() # default olarak  (how = "any") gelir. yani herhangibir değeri yoksa uçur demek
data = data.dropna(how="any") # herhangi bir veri yoksa uçurur.
# ama birde bütün satırın null olmasını istersenk any yerine all yazmamız gerekir.
print(data.shape)

data = pd.read_csv(url)
print("**************************************")
# hem City hem Colors reported kolonların boş olmasını istersek.
data = data.dropna(subset=['City','Colors Reported'],how="any") # all demek hem city de hem colors da null olanları uçur demek any dersek ikisinden birinin yol olması yeterli
print(data.shape)