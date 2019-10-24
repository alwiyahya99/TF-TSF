import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_excel('Sales_Data.xlsx')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#melihat variable dari dataset
print('melihat variable dari dataset')
print(dataset.keys(), '\n')

#melihat shape dari dataset
print('isi shape dari dataset')
print(dataset.shape, '\n')

#melihat dataset
dataku = pd.DataFrame(dataset)
print(dataku.head())

#split dataset
X_train, X_test, Y_train, Y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=0)
#fitting metode simple regresi linear
regressor = LinearRegression()
print(regressor.fit(X_train, Y_train))

#melakukan prediksi untuk hasil test set
Y_pred = regressor.predict(X_test)

#visualisasi data
plt.scatter(dataku.BiayaPromo, dataku.NilaiPenjualan)
plt.xlabel("Biaya Promosi")
plt.ylabel("Nilai Penjualan")
plt.title("Grafik nilai penjualan vs biaya promosi")
plt.show()

#visualisasi hasil machine learning
#ukuran plot
plt.figure(figsize=(10,8))
#biru adalah data observasi
plt.scatter(X_train, Y_train, color='blue')
#garis merah adalah hasil prediksi dari machine learning
plt.plot(X_train, regressor.predict(X_train), color='red')
#memberi judul dan label
plt.title('Biaya promosi terhadap penjualan (training set)')
plt.xlabel('Biaya promosi')
plt.ylabel('penjualan')
plt.show()