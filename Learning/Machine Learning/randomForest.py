import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("positions.csv")

level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values

regression = RandomForestRegressor(n_estimators=10, random_state=10) # n_esti... kaç tane decition Tree oluşturacaksak onu yazıyoruz.
# her seferinde farklı sonuçlar çıkıyor
#random_state= 10 dediğimizde gelen sonuçların hepsi aynı geliyor.
regression.fit(level,salary)
print(regression.predict(8.3))

#plt.scatter(level,salary,color="red")
#plt.plot(level,regression.predict(level),color="green")
#plt.show()
