import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films.columns)
print("**************************************")
films = films.drop("content_rating", axis=1) #axis=1 kolon  axis=0 satır
films = films.drop("actors_list", axis=1)

print(films)

print("**************************************")
films = films.drop(2,axis=0)
print(films)



print("**************************************")
rowsToDrop = [0,1,20,354,24,85] # listedeki rowları siler  2 yi yukarda sildiğimiz için tekrar silersek hata verir.
films = films.drop(rowsToDrop,axis=0)
print(films)

print("**************************************")
print(films.mean())