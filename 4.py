import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df1 = pd.read_csv('./balita/BCG.csv', na_values = 'n.a')
df2 = pd.read_csv('./balita/campak.csv', na_values = 'n.a')
df3 = pd.read_csv('./balita/DPT.csv', na_values = 'n.a')
df4 = pd.read_csv('./balita/polio.csv', na_values = 'n.a')

df1 = df1.interpolate()
df2 = df2.interpolate()
df3 = df3.interpolate()
df4 = df4.interpolate()


# fig 1
plt.figure('Persentasi balita terimunisasi 1995-2017 ')

plt.subplot(221)
plt.bar(df1['Tahun'], df1['% Balita yang pernah mendapat imunisasi BCG'], color='r')
plt.title('BCG')
plt.xticks(df1['Tahun'], rotation = 90)

plt.subplot(222)
plt.bar(df2['Tahun'], df2['% Balita yang pernah mendapat imunisasi Campak'], color='g')
plt.title('Campak')
plt.xticks(df2['Tahun'], rotation = 90)

plt.subplot(223)
plt.bar(df3['Tahun'], df3['% Balita yang pernah mendapat imunisasi DPT'], color='y')
plt.title('DPT')
plt.xticks(df3['Tahun'], rotation = 90)

plt.subplot(224)
plt.bar(df4['Tahun'], df4['% Balita yang pernah mendapat imunisasi Polio'], color='b')
plt.title('Polio')
plt.xticks(df4['Tahun'], rotation = 90)

plt.tight_layout()

# fig 2
plt.figure('Persentasi balita tak terimunisasi 1995-2017 ')

plt.subplot(221)
plt.bar(df1['Tahun'], (100-df1['% Balita yang pernah mendapat imunisasi BCG']), color='r')
plt.title('BCG')
plt.xticks(df1['Tahun'], rotation = 90)

plt.subplot(222)
plt.bar(df2['Tahun'], (100-df2['% Balita yang pernah mendapat imunisasi Campak']), color='g')
plt.title('Campak')
plt.xticks(df2['Tahun'], rotation = 90)

plt.subplot(223)
plt.bar(df3['Tahun'], (100-df3['% Balita yang pernah mendapat imunisasi DPT']), color='y')
plt.title('DPT')
plt.xticks(df3['Tahun'], rotation = 90)

plt.subplot(224)
plt.bar(df4['Tahun'], (100-df4['% Balita yang pernah mendapat imunisasi Polio']), color='b')
plt.title('Polio')
plt.xticks(df4['Tahun'], rotation = 90)

plt.tight_layout()

plt.show()


