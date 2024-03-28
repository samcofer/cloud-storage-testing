import os
import csv
import re
import sys

def parse_files(directory):
    # Initialize variables to store data
    file_data = {}
    file_groups = {}

    # Regular expression to match the filename pattern
    pattern = re.compile(r'^(.*)-run(\d+)\.txt$')

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            match = pattern.match(filename)
            if match:
                prefix = match.group(1)
                run_number = match.group(2)
                if prefix not in file_groups:
                    file_groups[prefix] = []
                file_groups[prefix].append((run_number, filepath))

    # Process file groups and extract data
    for prefix, files in file_groups.items():
        for i in range(0, len(files), 4):
            file_set = files[i:i+4]
            row = {'filesystem': prefix}
            for run_number, filepath in file_set:
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                    # Extract data from the last 3 lines
                    requests_completed = re.search(r'(\d+) requests completed', lines[-3]).group(1)
                    min_avg_max_mdev = re.search(r'min/avg/max/mdev = (.+)', lines[-1]).group(1)
                    # Add fields to the row
                    row[f'requests_completed_{run_number}'] = requests_completed
                    row[f'min_avg_max_mdev_{run_number}'] = min_avg_max_mdev
            file_data[prefix] = row

    # Write data to CSV
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['filesystem']
        for i in range(1, 5):
            fieldnames.append(f'requests_completed_{i}')
            fieldnames.append(f'min_avg_max_mdev_{i}')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in file_data.values():
            writer.writerow(row)

if __name__ == "__main__":

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print("Error: The provided directory path is invalid.")
        sys.exit(1)


    file_pairs = parse_files(directory_path)
