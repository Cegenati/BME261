import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("waling.csv")
df.columns = ["Time", "AcX", "AcY","AcZ"]

plt.plot(df.Time, df.AcX)
plt.plot(df.Time, df.AcY)
plt.plot(df.Time, df.AcZ)
plt.show()
