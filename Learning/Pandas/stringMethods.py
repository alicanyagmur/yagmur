import pandas as pd

data = pd.read_table("orders.tsv")
print(data)
print("**************************************")
print(data.columns)
print("**************************************")
print(data.item_name)
print("**************************************")
print(data.item_name.str.upper()) #str operasyonlarını bu şekilde kullanılır.
print("**************************************")
#datayı değiştirmek istiyorsakta
data.item_name = data.item_name.str.upper()
print(data.item_name)
print("**************************************")
print(data.item_name.str.contains('Chicken'))
print("**************************************")
print(data.item_name.str.contains('Chicken'.upper()))
print("**************************************")
data.choice_description = data.choice_description.str.replace('[','')
data.choice_description = data.choice_description.str.replace(']','')
print(data.columns)
print(data[['item_name','choice_description']])