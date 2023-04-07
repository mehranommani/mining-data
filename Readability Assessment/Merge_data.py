
import pandas as pd

# Read the two CSV files
df1 = pd.read_csv("integerated.csv")
df2 = pd.read_csv("readability.csv")

# Merge the two dataframes based on the hash code
merged_df = pd.merge(df1, df2, on="commit_hash")

# Drop duplicates
merged_df.drop_duplicates(subset=['commit_hash'], keep='first', inplace=True)

# Write the merged dataframe to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)
