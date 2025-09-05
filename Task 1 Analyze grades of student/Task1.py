import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv('grades.csv')

# Step 2: Calculate the average score for each student
df['Average'] = df[['Math', 'English', 'Science']].mean(axis=1)

# Step 3: Find the student with the highest average
top_student = df.loc[df['Average'].idxmax()]

# Step 4: Print the full DataFrame and top student
print("Student Grades with Averages:\n")
print(df)

print("\nTop Student:")
print(f"{top_student['Name']} with an average score of {top_student['Average']:.2f}")
