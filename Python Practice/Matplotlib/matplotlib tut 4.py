
"""
company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
revenue = [90, 136, 89, 27]
profit = [40, 2, 34, 12]

xpos = np.arange(len(company))

plt.xticks(xpos, company)
plt.xlabel("Companies")
plt.ylabel("Amount")
plt.title("US Tech Stocks")

bar_width = 0.4  # Width of each bar
bar_spacing = 0.2  # Spacing between groups of bars

plt.bar(xpos - bar_spacing, revenue, width=bar_width, label="Revenue")
plt.bar(xpos + bar_spacing, profit, width=bar_width, label="Profit")
plt.legend()

plt.show()


plt.yticks(xpos, company)
plt.title("US Tech Stocks")

bar_height = 0.4  # Width of each bar
bar_spacing = 0.2  # Spacing between groups of bars

plt.barh(xpos - bar_spacing, revenue, height=bar_height, label="Revenue")
plt.barh(xpos + bar_spacing, profit, height=bar_height,  label="Profit")
plt.legend()

plt.show()
"""

#///////////////////          ChaGpt Give Me Project             ////////////////

import matplotlib.pyplot as plt
import numpy as np
import FuncAnimation
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))
categories = ['Rent', 'Utilities', 'Groceries', 'Transportation', 'Entertainment', 'Healthcare']
expenses = [1200, 150, 250, 200, 100, 80]

plt.figure(figsize=(10, 6))  # Adjust the figure size for better visualization

xpos=np.arange(len(categories))

plt.xticks(xpos,categories)
plt.xlabel('Categories')
plt.ylabel('Monthly Expense ($)')
plt.title('Monthly Expenses by Category')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better readability

for i, expense in enumerate(expenses):
    plt.text(i, expense + 5, f"${expense}", ha='center', va='bottom', fontsize=10)

plt.bar(xpos,expenses,label="expence",color="skyblue")
plt.legend()

plt.tight_layout()

plt.show()

# Clear the previous bars and texts
ax.cla()

# Set the xticks and labels again
ax.set_xticks(xpos)
ax.set_xticklabels(categories)

# Plot the new bars and texts
ax.bar(xpos, new_expenses, color='skyblue', label='Expense')
for i, expense in enumerate(new_expenses):
    ax.text(i, expense + 5, f"${expense}", ha='center', va='bottom', fontsize=10)

# Set the axes labels and title again
ax.set_xlabel('Categories')
ax.set_ylabel('Monthly Expense ($)')
ax.set_title('Monthly Expenses by Category')

# Add the legend and gridlines again
ax.legend()
ax.grid(True, axis='y', linestyle='--', alpha=0.7)



import numpy as np
import matplotlib.pyplot as plt

# Step 1: Data Collection (Fictional Monthly Expenses)
categories = ['Rent', 'Utilities', 'Groceries', 'Transportation', 'Entertainment', 'Healthcare']
expenses = [1200, 150, 250, 200, 100, 80]
savings = 1000  # Example value for savings

# Step 3: Plot Creation
plt.figure(figsize=(12, 6))

# Using a NumPy array for x positions
xpos = np.arange(len(categories))

# Plot expenses
plt.subplot(1, 2, 1)
plt.bar(xpos, expenses, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Monthly Expense ($)')
plt.title('Monthly Expenses by Category')
plt.xticks(xpos, categories, rotation=45, ha='right')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend(['Expenses'])

# Data Labels for expenses
for i, expense in enumerate(expenses):
    plt.text(i, expense + 5, f"${expense}", ha='center', va='bottom', fontsize=10)

# Plot savings
plt.subplot(1, 2, 2)
plt.bar(['Savings'], [savings], color='green')
plt.xlabel('Categories')
plt.ylabel('Amount ($)')
plt.title('Monthly Savings')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend(['Savings'])

# Data Labels for savings
plt.text(0, savings + 5, f"${savings}", ha='center', va='bottom', fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

# Analysis
most_expensive_category = categories[np.argmax(expenses)]
total_expenses = np.sum(expenses)

print(f"The most expensive category is {most_expensive_category} with ${max(expenses)}")
print(f"Total monthly expenses: ${total_expenses}")
print(f"Monthly savings: ${savings}")

