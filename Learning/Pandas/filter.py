import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films)
print("**************************************")
print(films.columns)
print("**************************************")
print(films.head())

print("**************************************")
print(films['title'])
print("**************************************")
print(films['title'].head())
print("**************************************")
print(films.title.tail())

print("**************************************")
print(films[['title','star_rating']].head())


print("**************************************")
print(films[:9][['title','star_rating']].head())

print("**************************************")
print(films[films['star_rating']>=8.5])

print("**************************************")
print(films[films['star_rating']>=8.5][['title','star_rating']])

print("**************************************")
print(films[
          (films['star_rating']>=8.5) &
          (films['star_rating']<=9)
      ][['title','star_rating']])
