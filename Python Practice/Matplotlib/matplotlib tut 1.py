import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[45,78,95,84,32,51,55]

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Weather")
plt.plot(x,y,color='red',linestyle='dotted',linewidth=9 )
plt.show()