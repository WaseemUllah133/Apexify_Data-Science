import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("survey.csv")

# Count the number of responses for each satisfaction level
satisfaction_counts = df["Satisfaction"].value_counts()

# Display the counts in console
print("Satisfaction Counts:")
print(satisfaction_counts)

# Create a bar plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x=satisfaction_counts.index, y=satisfaction_counts.values, palette="muted")

# Customize the plot
plt.xlabel("Satisfaction Level")
plt.ylabel("Number of People")
plt.title("Survey Results: User Satisfaction Levels")
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
