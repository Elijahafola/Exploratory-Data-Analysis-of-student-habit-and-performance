import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
filepath = "C:/Users/afola/Music/LangaugeLearningApp/Extract//student_habits_performance.csv"
df = pd.read_csv(filepath)

# Display the first few rows
print(df.head())

# Get basic information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe())


# Histogram of study hours
plt.figure(figsize=(8,5))
sns.histplot(df["study_hours_per_day"], bins=20, kde=True)
plt.title("Distribution of Study Hours Per Day")
plt.show()

# Correlation heatmap
plt.figure(figsize=(12,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# Scatter plot: Study Hours vs Exam Score
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["study_hours_per_day"], y=df["exam_score"])
plt.title("Study Hours vs Exam Score")
plt.show()

# Bar plot for diet quality distribution
plt.figure(figsize=(6,4))
sns.countplot(x=df["diet_quality"], palette="Set2")
plt.title("Diet Quality Distribution")
plt.show()


