import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [150, 200, 250, 300, 350, 400],
    'Expenses': [100, 150, 200, 220, 270, 320]
}

df = pd.DataFrame(data)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='skyblue', label='Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.legend()
plt.show()

# Create line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b', label='Sales')
plt.plot(df['Month'], df['Expenses'], marker='o', linestyle='--', color='r', label='Expenses')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Monthly Sales and Expenses')
plt.legend()
plt.show()
