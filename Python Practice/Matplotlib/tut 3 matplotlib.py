import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
max_t = [50, 51, 52, 48, 47, 49, 46]
min_t = [43, 42, 40, 44, 33, 35, 37]
avg_t = [45, 48, 48, 46, 40, 42, 41]

plt.plot(days, max_t,"+-.", label='Max Temperature', color='#066800')
plt.plot(days, min_t,"x--", label='Min Temperature', color='#E61800')
plt.plot(days, avg_t,"*-", label='Avg Temperature', color='#F9C74A')

plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Temperature Variation')
plt.legend(loc="best",shadow=True,borderpad=0.5,handletextpad=0.5)

annotations = [
    ('PEAK', (4, 44), (5.1, 50)),
    ('Bottom', (5, 32.7), (6.1, 50))
]

for text, xy, xytext in annotations:
    plt.annotate(text, xy=xy, xytext=xytext,
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.grid()
plt.xlim(0.5,7.9)
plt.ylim(32,53)
plt.show()

