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
print(pd.concat([data1Df,data2Df],axis=1))

print("**************************************")
print(pd.concat([data1Df[['id','ad','soyad']],data2Df[['id','ad','soyad']]],axis=1))
