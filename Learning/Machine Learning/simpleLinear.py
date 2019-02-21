import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

regression = LinearRegression()

data = pd.read_csv("hw_25000.csv")
boy = data.Height.values.reshape(-1,1)
kilo = data.Weight.values.reshape(-1,1)

regression.fit(boy,kilo)
print(regression.predict(71)) # boyu 71 inc olan kişinin kilo oranını gösteriyor.

print(data.columns)

x = np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x, regression.predict(x), color="red") # plot çizgi çiziyor ve her x için direrek ve regression.predict(x) (X'in Y'ye karşılığı) veriyor

print("burada yüzde " + str(r2_score(kilo, regression.predict(boy))) + "  oranında hata payı vardır.") #

plt.scatter(data.Height,data.Weight)
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.title("Simple Linear Regression Model")
plt.show()

print(r2_score(kilo, regression.predict(boy)))