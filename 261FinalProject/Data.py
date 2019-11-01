import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from sklearn import neighbors
from scipy import signal


df1 = pd.read_csv("S01R01.txt", sep = " ")
df2 = pd.read_csv("S01R02.txt", sep = " ")
df3 = pd.read_csv("S02R01.txt", sep = " ")
df4 = pd.read_csv("S02R02.txt", sep = " ")
df5 = pd.read_csv("S03R01.txt", sep = " ")
df6 = pd.read_csv("S03R02.txt", sep = " ")
df7 = pd.read_csv("S03R03.txt", sep = " ")
df8 = pd.read_csv("S04R01.txt", sep = " ")
df9 = pd.read_csv("S05R01.txt", sep = " ")
df10 = pd.read_csv("S05R02.txt", sep = " ")
df11 = pd.read_csv("S06R01.txt", sep = " ")
df12 = pd.read_csv("S06R02.txt", sep = " ")
df13 = pd.read_csv("S07R01.txt", sep = " ")
df14 = pd.read_csv("S07R02.txt", sep = " ")
df15 = pd.read_csv("S08R01.txt", sep = " ")
df16 = pd.read_csv("S09R01.txt", sep = " ")
df17 = pd.read_csv("S10R01.txt", sep = " ")
df1.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df2.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df3.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df4.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df5.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df6.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df7.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df8.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df9.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df10.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df11.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df12.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df13.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df14.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df15.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df16.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']
df17.columns = ['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Thigh1', 'Thigh2', 'Thigh3', 'Trunk1', 'Trunk2', 'Trunk3', 'Freeze']

frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17]
dfbad = pd.concat(frames)

df = dfbad[['Time', 'Ankle1', 'Ankle2', 'Ankle3', 'Freeze']]

signal1 = sp.signal.medfilt(df1.Ankle1,21)
sub1df1 = df1[df1.Freeze == 1]
sub2df1 = df1[df1.Freeze == 2]

b, a = signal.butter(5,0.05)
y = signal.filtfilt(b,a,df1.Ankle1)

plt.subplot(2,1,1)
plt.plot(df1.Time, df1.Ankle1)
plt.scatter(sub1df1.Time,sub1df1.Ankle1, c= 'orange')
plt.scatter(sub2df1.Time,sub2df1.Ankle1, c='purple')

plt.subplot (2,1,2)
plt.plot(df1.Time, y)
#plt.scatter(sub1df1.Time,sub1df1.Ankle1, c= 'orange')
#plt.scatter(sub2df1.Time,sub2df1.Ankle1, c='purple')
plt.show()












#x = df.Freeze

# df1 = df1[df1.Freeze != 0 ]
# sub1df1 = df1[df1.Freeze == 1]
# sub2df1 = df1[df1.Freeze == 2]
#
# #f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True, sharey=False)
# #ax1.plot(df1.Time,df1.Ankle1)
# #ax2.plot(df1.Time,df1.Ankle2)
# #ax3.plot(df1.Time,df1.Ankle3)
# #ax4.plot(df1.Time,df1.Freeze)
#
#
# x = df1.Time
# y = df1.Ankle1
# signal = sp.signal.medfilt(y,3)
# plt.plot (x,y)
# plt.show()
# plt.plot(x,signal)
# plt.show()
#
#
# # plt.subplot(2,1,1)
# # plt.plot(df1.Time,der)
# #
# # plt.subplot(2,1,2)
# # plt.scatter(sub1df1.Time,sub1df1.Ankle1, c= 'orange')
# # plt.scatter(sub2df1.Time,sub2df1.Ankle1, c='purple')
# # plt.show()