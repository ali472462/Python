import matplotlib.pyplot as pl
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[45,78,95,84,32,51,55]

#plt.plot(x,y,'H-.')
plt.plot(x,y, linestyle="-.", marker='^', markersize=9, color='Red',alpha=1, drawstyle='steps-mid',dash_joinstyle='round',fillstyle='left')
plt.show()