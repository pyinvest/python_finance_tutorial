import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


data = pd.read_csv('data.csv')
data = data.groupby('Country/Region').sum()
data = data.iloc[:,2:]


def animate(i):
    date = pd.to_datetime(data.columns[i]).strftime('%Y-%m-%d')
    countries = list(data.iloc[:,i].sort_values()[-5:].index)
    values = list(data.iloc[:,i].sort_values()[-5:])
    plt.cla()
    plt.barh(countries,values)
    plt.title(date)

plt.figure(figsize=(20,15))
ani = FuncAnimation(plt.gcf(),animate,interval=1000,frames=len(data.columns)-1)
plt.show()