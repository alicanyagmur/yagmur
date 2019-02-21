import pandas as pd

data1 = {
            'id' : [1,2,3,4],
            'ad' : ["Ali", "Nina","Alina","Mahoni"],
            'soyad' : ["Yagmur","Voinovska", "Yagmur", "Canovski"]
        }

data2 = {
            'id' : [1,3,4,7],
            'ad' : ["Ahmet", "Nejla","Molly","alena"],
            'soyad' : ["kar","taka", "krid", "ristovska"]
        }

data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)

print(data1Df[['id','ad','soyad']])
print(data2Df[['id','ad','soyad']])

print("**************************************")
print(pd.merge(data1Df,data2Df,on='id',how='inner')) # id alanına göre merge ediyor how inner dersek inner join olarak  merge eder
# yani burada iki kolondo da aynı id ler varsa birbirine inner join ediyor. eşleşmeyen idler gelmez
print("**************************************")
print(pd.merge(data1Df[['id','ad','soyad']],data2Df,on='id',how='inner'))

print("**************************************")
print(pd.merge(data1Df,data2Df,on='id',how='left')) # sagda olup solda olmayanlarıda da getirir. right'da tam tersi