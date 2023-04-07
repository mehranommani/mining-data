from pydriller import Repository
import datetime

# set the path to the local repository
repo_path = "https://github.com/apache/commons-bcel"

# set the output file path
output_file = "re_bcel.csv"

# set the committer date cutoff
dt1 = datetime.datetime(2022, 12, 31)

# create an empty list to store the extracted data
rows = []

# iterate over the commits in the repository
for commit in Repository(repo_path, only_modifications_with_file_types=['.java'], only_in_branch='master', to=dt1).traverse_commits():

    # create an empty list to store the extracted file data
    file_data = []

    # iterate over the modified files in the commit
    for modified_file in commit.modified_files:

        # only extract data for modified .java files
        if modified_file.filename.endswith(".java"):

            # extract the required data from the commit and the modified file
            commit_data = [
                commit.hash,
                commit.author.name,
                commit.author.email,
                commit.committer_date.strftime('%y/%m/%d'),
                commit.msg,
                len(commit.modified_files)
            ]

            file_data.append([
                modified_file.new_path,
                modified_file.complexity,
                modified_file.nloc
            ])

    # add the extracted data to the rows list
    for file_row in file_data:
        rows.append(commit_data + file_row)

# create a pandas DataFrame from the rows list
import pandas as pd
columns = ["commit_hash", "author_name", "author_email", "committer_date", "commit_msg", "num_files_changed", "path", "complexity", "nloc"]
df = pd.DataFrame(rows, columns=columns)

# save the DataFrame to a CSV file
df.to_csv(output_file, index=False)

# print a message to confirm that the data was saved
print(f"Data saved to {output_file}")
