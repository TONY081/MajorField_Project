import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/tonyk/Desktop/case stud/case_studies_project/cleaned_merged_dataset.csv')

# Group by release year and count movies
movies_per_year = df.groupby('release_year')['title'].count()

# Plot the trend
plt.plot(movies_per_year.index, movies_per_year.values, marker='o')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.title('Trend in Movie Release Over the Years')
plt.grid(True)
plt.show()
