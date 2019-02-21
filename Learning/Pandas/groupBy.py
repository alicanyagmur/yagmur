import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films.columns)
print("**************************************")
print(films.star_rating.mean()) # bütün filmlerin ortalamasını verir. 7,88978

print("**************************************")
print(films.star_rating.mean())

print("**************************************")
print(films.groupby('genre').star_rating.mean()) # bütün filmlerin türüne göre ortalamasını getirir.