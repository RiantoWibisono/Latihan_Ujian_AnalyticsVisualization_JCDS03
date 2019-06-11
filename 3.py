from pymongo import MongoClient
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


x = MongoClient('mongodb://localhost:27017/')
db = x['Kampus']
col1 = db['Dosen']
col2 = db['Mahasiswa']

dataDosen = []
dataMahasiswa = []

for x in col1.find():
    dataDosen.append(x)
for x in col2.find():
    dataMahasiswa.append(x)


dfDataD = pd.DataFrame(
    dataDosen,
    columns = ['asal', 'nama', 'status', 'usia']
)
dfDataM = pd.DataFrame(
    dataMahasiswa,
    columns = ['asal', 'nama', 'status', 'usia']
)

print(dfDataD)
print()
print(dfDataM)


x1 = np.array(dfDataD['nama'])
x2 = np.array(dfDataM['nama'])
y1 = np.array(dfDataD['usia'])
y2 = np.array(dfDataM['usia'])
plt.bar(x1, y1, color='blue', alpha = .7)
plt.bar(x2, y2, color='orange', alpha = .7)

plt.title('Usia Warga Kampus')
plt.legend(['Dosen', 'Mahasiswa'])
plt.grid(True)

plt.show()

print()