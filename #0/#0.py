#Vladyslav Beshta

K= 1 #порядковий номер третьої літери імені
N= 1 #порядковий номер останньої літери прізвища/порядковий номер у групі
M = ((2%9)*10) #помножений на 10 залишок від ділення порядкового номеру першої літери прізвища на 9

import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import math
import numpy as np

#1
data = pd.read_csv('Top_100_Tennis_Players-2007_Men.csv', index_col=0)

#2
pd.set_option('display.expand_frame_repr', False)
display(data.head(K+N))

#3(a)
country_counter = len(data[data.Country == 'Spain '])
print(country_counter, 'tennis players from Spain.')

#3(b)
strM = str(M) + "%"
strM10 = str(M+10) + "%"
print("From",strM,"to", strM10)

percent = data['Winning Percentage']
sortByWinning = data.sort_values(by=['Winning Percentage'])

moreM = sortByWinning[sortByWinning['Winning Percentage'] >= strM]
betweenMWin = moreM[moreM['Winning Percentage'] <= strM10]
money = betweenMWin['Career Earnings'].values

result = 0
for i in range(0, len(money)):
    result += int(money[i][1:])
print('Average value of money;',round(result/len(money),2))

#4
countries = data['Country'].drop_duplicates().values

average_points = []
average_wins = []

for i in range(0, len(countries)):
    points = data['Pts'].values[data.Country == countries[i]]
    average_points.append(math.ceil(sum(points)/len(points)))
    wins = data['Singles Record (Career)'].str.extract(r'(\d+)').astype('float').values[data.Country == countries[i]]
    average_wins.append(np.nansum(wins) / len(wins))

y_pos = np.arange(len(countries))

width = 0.35
fig, ax = plt.subplots()
ax.barh(y_pos, average_points, width, color='red', label='Cередній рейтинг гравців по крїнах')
ax.barh(y_pos + width, average_wins, width, color='green', label='Середній рейтинг перемог гравців по країнах')
ax.set(yticks=y_pos + width, yticklabels=countries, ylim=[2*width - 1, len(y_pos)])
ax.legend()
plt.show()