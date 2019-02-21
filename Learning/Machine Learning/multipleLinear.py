import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("insurance.csv")

print(data.columns)


expenses = data.expenses.values.reshape(-1,1) # Y eksenini oluşturmuş olduk

ageBmis = data[['age','bmi']].values  # X eksenini oluşturmuş olduk.

regression = LinearRegression()

regression.fit(ageBmis,expenses)

print(regression.predict(np.array([20,20]))) # 20 yaşında olan ve bmi sahip kişi için tahminleme yapması gerekiyor.
# yani 20 yaşında ve 2 bmi sahip birinin ortalama harcaması 5068 olarak hesaplamaktadır.

print(regression.predict(np.array([20,21])))
print(regression.predict(np.array([20,22])))
print(regression.predict(np.array([20,23])))

print(regression.predict(np.array([[30,20],[30,21],[30,22],[30,23]])))
