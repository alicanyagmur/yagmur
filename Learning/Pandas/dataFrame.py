import  pandas as pd


data = ([10,20,30,40,50])
df = pd.DataFrame(data)

print(df)

print("**************************************")

data2 = [["Ali", 31, "Ankara"],["Nina",30,"Skopje"],["Alina",1,"Ankara"]]
df2 = pd.DataFrame(data2)
print(df2)


print("**************************************")

data3 = [["Ali", 31, "Ankara"],["Nina",30,"Skopje"],["Alina",1,"Ankara"]]
df3 = pd.DataFrame(data3, columns=["İsim", "Yaş", "Şehir"]) # colomns isim verebiliriz. indexlere de verebiliriz.
print(df3)

print("**************************************")
#dataframe ile çalışmak için illa liste olmasına gerek yok
# sözlük olarak yapalım

data4 = {"isim":["Ahmet", "Nejla", "Mahoni"],
         "Yaş" : [31,30,1],
         "Şehir": ["Ankara", "Skopje", "Ankara"]}
df4 = pd.DataFrame(data4,index=[1,2,3]) # Sutun ve Satırlar biribirine eşit olmak zorunda yoksa hata verir.
print(df4)
print("***********")
print(df4["isim"])# bana sadece isimleri verir.

print("**************************************")
# bazende bazı kolonları istemeye biliriz bunun içinde del komutunu kullanırız.
del df4["Şehir"] # bunu böyle yazmak yerine pop kullanabiliriz.
print(df4)
print("**************************************")
df3.pop("Yaş")
print(df3)

data5 = {"isim":["Ali", "Nina", "Alina"],
         "Yaş" : [31,30,1],
         "Şehir": ["Ankara", "Skopje", "Ankara"]}
df5 = pd.DataFrame(data5) # colomns isim verebiliriz. indexlere de verebiliriz.
print(df5)
print("**************************************")
#veriye ulaşmak için location verebiliriz bunuda loc ile verebiliriz.
print(df5.loc[2])
print("***********")
print(df5.iloc[2])

print("**************************************")
# bütün verileri birleştirmek istersek
df6 = df5.append(df4)
print(df6)

print("**************************************")
# verileri incelemek istersek ilkten 5 tanesini verir
print(df6.head())
print("**************************************")
# verileri incelemek istersek sondan 5 tanesini verir
print(df6.tail())