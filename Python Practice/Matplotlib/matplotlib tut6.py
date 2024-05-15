import matplotlib.pyplot as plt

exp_vals = [1400, 600, 300, 410, 250]
exp_labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]
explode = [0, 0, 0, 0.1, 0.2]  # Explode the "Car" and "Other Utilities" slices
autopct_format = '%1.1f%%'  # Format for autopct labels

plt.pie(exp_vals, labels=exp_labels, shadow=True, autopct=autopct_format, radius=1, explode=explode, counterclock=False)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.title("Monthly Expenses")

plt.show()
