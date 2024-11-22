# modules used 
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns


# Loading and Reading the dataset
youtube_data = pd.read_csv(r"C:\Users\DELL\Desktop\Work\Internship projects\DATA\Intern Launch\Task 1 YouTube Streamer Analysis-20240816T041247Z-001\Task 1 YouTube Streamer Analysis\youtubers_df.csv")

# Displaying first few rows
print(youtube_data.head())

# Basic Information about the dataset
print(youtube_data.info())

# Statistics Summary
print(youtube_data.describe())

#Checking and Sorting Missing Values
print(youtube_data.isnull().sum)

# Printing the column names
print(youtube_data.columns)

# Get the number of missing data points per column
missing_values_count = youtube_data.isnull().sum()

# Print the number of missing data points for the first ten columns
print("Missing values in the first ten columns:")
print(missing_values_count[0:10])

# Calculate the total number of cells and missing values with the percentage
total_cells = np.prod(youtube_data.shape)
print(total_cells)

total_missing = missing_values_count.sum()
print(total_missing)

percent_missing = (total_missing / total_cells) * 100
print(f"Percentage of missing values: {percent_missing:.2f}%")

# Drop rows with missing values
data = youtube_data.dropna()
print(data.head())
columns_with_na_dropped = data.dropna(axis=1)
print(columns_with_na_dropped.head())
print(f"Percentage of missing values: {percent_missing:.2f}%")

# just how much data did we lose?
print("Columns in original dataset: %d \n" % data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])


# Incase there is formatting issues in the column names
# Remove any leading/trailing spaces
youtube_data.columns = youtube_data.columns.str.strip()

#Checking for missing columns
required_columns = ['Subscribers', 'Visits', 'Likes', 'Comments']
for column in required_columns:
    if column not in youtube_data.columns:
        print(f"Column {column} is missing")
        
#Correcting the typo in the column name
youtube_data = youtube_data.rename(columns={'Suscribers': 'Subscribers'})
columns_with_na_dropped = columns_with_na_dropped.rename(columns={'Suscribers': 'Subscribers'})
# Verify the renaming
print("After renaming:", youtube_data.columns)

# Graphical Representation
# Plot for detecting outliers
sns.boxplot(data=columns_with_na_dropped[['Subscribers', 'Visits', 'Likes', 'Comments']])
plt.show()

# Trend Analysis
#Analyzing the frequency of each category

# Count the number of streamers in each category
category_counts = columns_with_na_dropped['Categories'].value_counts()
print(category_counts)

# Plot the most popular categories
sns.barplot(x=category_counts.index, y=category_counts.values)
plt.xticks(rotation=90)
plt.show()
'''
# Correlation analysis
correlation_matrix = columns_with_na_dropped[['Subscribers', 'Likes', 'Comments']].corr()

# Heatmap for Visualizing Correlation
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Streamers Content Distribution
# By Country
# Count the number of streamers by country
country_counts = columns_with_na_dropped['Country'].value_counts()

# Plot the distribution of streamers by country
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.xticks(rotation=90)
plt.show()

'''
'''
# Regional Preferences
regional_preferences = youtube_data.groupby([])

'''
