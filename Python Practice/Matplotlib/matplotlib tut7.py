import matplotlib.pyplot as plt
import numpy as np
exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]
# Create a figure with a transparent background
fig = plt.figure(facecolor='none')
plt.pie(exp_vals,labels=exp_labels,radius=2, autopct='%0.1f%%', explode=[0,0.1,0.1,0,0],shadow=True)

# Changed title color to "blue"
plt.title("Monthly Expenses", color="blue")

plt.savefig("../files/piechart.pdf", bbox_inches="tight", pad_inches=1, transparent=True)

# Changed the color of the tick labels to "green"
plt.tick_params(axis='both', colors='green')

plt.show()

#//////////////      Exercise        ///////////////

company=['GOOGL','AMZN','MSFT','FB']

revenue=[90,136,89,27]

xpos = np.arange(len(company))

plt.xticks(xpos, company)
plt.xlabel("Companies")
plt.ylabel("Revenue")
plt.title("US Tech Stocks")

bar_width = 0.4  # Width of each bar
bar_spacing = 0.2  # Spacing between groups of bars

plt.bar(xpos - bar_spacing, revenue, width=bar_width, label="Revenue")
plt.legend()


plt.savefig("../files/piechart1.pdf", bbox_inches="tight", pad_inches=1, transparent=True)

plt.show()
