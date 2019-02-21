import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # bizim verilerimze göre linear olmuyor.
from sklearn.preprocessing import PolynomialFeatures # Bizim verilerimize göre polynom özelliği gerekiyor

data = pd.read_csv("positions.csv")

print(data.columns)


level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values.reshape(-1,1)

regression = LinearRegression()
regression.fit(level,salary)



tahmin = regression.predict(8.3)

#plt.scatter(level,salary,color="red")
#plt.plot(level,regression.predict(level),color="blue")
#plt.show()


regressionPoly = PolynomialFeatures(degree=4)
levelPoly = regressionPoly.fit_transform(level)# benim elimde level değerleri var sen bunu görüntü haline getir diyoruz.
regression2 = LinearRegression() #linear regressionu yeni x e göre oluşturuyoruz.
regression2.fit(levelPoly,salary) # yeni levelPoly'ye göre çizginin çizilmesini istiyoruz

tahmin2 = regression2.predict(regressionPoly.fit_transform(8.3)) # polinom karşılığına fit etmemiz gerekiyor.


plt.scatter(level,salary,color="red")
plt.plot(level,regression.predict(level),color="blue") # Burada linear ile düz çizgi çiziyordu
plt.plot(level,regression2.predict(levelPoly),color="green") # burada verilerimize göre çizgi çiziyor.
plt.show()
