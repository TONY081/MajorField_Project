import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('C:/Users/tonyk/Desktop/case stud/case_studies_project/cleaned_merged_dataset.csv')

# Replace empty values with NaN
df.replace('', pd.NA, inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv('cleaned_file.csv', index=False)
