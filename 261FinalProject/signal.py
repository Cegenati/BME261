import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("walking.csv")
df1.columns = ['Time', 'ACX', 'ACY', 'ACZ']

plt.plot (df1.Time, df1.ACX)
plt.plot (df1.Time,df1.ACY)
plt.plot (df1.Time,df1.ACZ)
plt.show()
