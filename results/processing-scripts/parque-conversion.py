import pandas as pd
import os
import sys

def manipulate(field):


    if 'ms' in str(field):
        # Manipulate the value for milliseconds
        value = float(field.replace('ms', ''))
        return value
    elif 'us' in str(field):
        # Manipulate the value for microseconds
        value = round(float(field.replace('us', '')) / 1000,3)
        return value
    else:
        return field

def merge_csv_to_parquet(csv_dir, output_parquet):
    # List to store dataframes of CSV files
    dfs = []

    # Read each CSV file and append its dataframe to the list
    for filename in os.listdir(csv_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(csv_dir, filename)
            df = pd.read_csv(filepath)
            dfs.append(df)

    # Merge dataframes on the "filesystem" column
    merged_df = pd.concat(dfs, ignore_index=True)
    
    columns = ['min','max','avg','mdev']

    for col in columns:
        merged_df[col] = merged_df[col].apply(manipulate)

    # Aggregate python columns

    # Filter out rows where 'test-name' is not "PIP venv Pytorch Install"
    filtered_rows = merged_df[merged_df['test-name'] != 'PIP venv Pytorch Install']

    # Group by multiple columns and calculate the mean for the desired rows
    grouped_rows = merged_df[merged_df['test-name'] == 'PIP venv Pytorch Install'].groupby(['filesystem', 'cloud', 'test-name']).mean().round(0).reset_index()

    merged_df = pd.concat([filtered_rows, grouped_rows], ignore_index=True)

    merged_df = merged_df.drop(columns='run-number')

    # Write merged data to a Parquet file
    merged_df.to_parquet(output_parquet, index=False)

    print("Parquet file created successfully.")

if __name__ == "__main__":
 # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py directory_path output_file")
        sys.exit(1)

    directory_path = sys.argv[1]
    output_file = sys.argv[2]

    # Check if directory exists
    if not os.path.isdir(directory_path):
        print("Error: Directory not found.")
        sys.exit(1)

    merge_csv_to_parquet(directory_path, output_file)
