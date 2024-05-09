import pandas as pd
import os
import sys

def manipulate_ms(field):


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

def manipulate_s(field):


    if 'ms' in str(field):
        # Manipulate the value for milliseconds
        value = round(float(field.replace(' ms', '')) / 1000,3)
        return value
    elif ' s' in str(field):
        # Manipulate the value for microseconds
        value = round(float(field.replace(' s', '')),0)
        return value
    else:
        return field

def manipulate_k(field):


    if ' k' in str(field):
        # Manipulate the value for thousands count
        value = round(float(field.replace(' k', '')) * 1000,3)
        print(value)
        return value
    else:
        value = float(field)
        print(value)
        return value

def manipulate_vol(field):


    if 'MiB' in str(field):
        # Manipulate the value for milliseconds
        value = round(float(field.replace(' MiB', '')) / 1024,3)
        return value
    elif 'GiB' in str(field):
        # Manipulate the value for microseconds
        value = float(field.replace(' GiB', ''))
        return value
    elif 'KiB' in str(field):
        # Manipulate the value for microseconds
        value = float(field.replace(' KiB', ''))
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
    
    

    # Standardize on ms
    columns = ['min','max','avg','mdev']
    for col in columns:
        merged_df[col] = merged_df[col].apply(manipulate_ms)
        merged_df.astype({col: 'float'}).dtypes
    
    # Standardize on seconds
    columns = ['requests-time', 'generated-time']
    for col in columns:
        merged_df[col] = merged_df[col].apply(manipulate_s)
        merged_df.astype({col: 'float'}).dtypes

   
    # Standardize count on single digits, not k
    columns = ['requests-count', 'generated-count']
    for col in columns:
        merged_df[col] = merged_df[col].apply(manipulate_k)
        # testdf['testcol'] = testdf['testcol'].astype(str)


    # Standardize on GiB
    columns = ['requests-ops-volume', 'generated-ops-volume']
    for col in columns:
        merged_df[col] = merged_df[col].apply(manipulate_vol)
        merged_df.astype({col: 'float'}).dtypes

    
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
