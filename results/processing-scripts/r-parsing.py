import re
import csv
import os
import sys

# Initialize lists and set for storing modified and unique rows
modified_rows = []
unique_rows = []
seen = set()

def parse_files_in_directory(directory,output_file):
    """
    Function to parse files in a directory and extract relevant information.
    Args:
        directory (str): Directory path containing files to parse.
        output_file (str): Path to the output CSV file.
    """
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        # Check if filename contains "results"
        if "results" in filename:
            filepath = os.path.join(directory, filename)
            # Check if filepath is a file
            if os.path.isfile(filepath):
                # Extract filesystem and run number using regex
                filesystem_regex = re.match(r'^(.+?)-run(\d).*$', filename).group(1)
                run_number_regex = re.match(r'^(.+?)-run(\d).*$', filename).group(2)
                with open(filepath, 'r') as file:
                    # Read CSV file
                    reader = csv.reader(file)
                    rows = list(reader)
                    for row in rows:
                        if row == rows[0]:  # Skip header row
                            continue
                        else:
                            # Append filesystem and run number to each row
                            new_row = [filesystem_regex, run_number_regex] + row
                            modified_rows.append(new_row)

    # Define header row
    header_row = ['filesystem', 'run_number', 'task', 'user', 'system', 'elapsed', 'parallelism']
    unique_rows.insert(0, header_row)

    # Remove duplicate rows while preserving order
    for row in modified_rows:
        row_tuple = tuple(row)
        if row_tuple is not None:
            if tuple(row) not in seen:
                unique_rows.append(row)
                seen.add(row_tuple)

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

    # Parse files in the directory
    parse_files_in_directory(directory_path, output_file)

    # Write unique rows to the output file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(unique_rows)
