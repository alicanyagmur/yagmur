import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films.query('star_rating>=9.0'))
print("**************************************")
print(films.query('star_rating>=9.0 & star_rating<=9.2'))