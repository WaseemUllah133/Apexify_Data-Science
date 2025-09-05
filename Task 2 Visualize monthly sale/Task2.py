import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales.csv')

plt.plot(data['Month'], data['Sales'], marker='o')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
