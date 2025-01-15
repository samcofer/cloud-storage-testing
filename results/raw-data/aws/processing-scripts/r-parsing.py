import re
import csv
import os
import sys
from collections import defaultdict


# Initialize lists and set for storing modified and unique rows
modified_rows = []
unique_rows = []
seen = set()
elapsed_times = defaultdict(float)
counts = defaultdict(int)

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
            path_list = os.path.abspath(filepath).split("/")

            if "azure" in path_list:
                cloud="AZURE"
            elif "aws" in path_list:
                cloud="AWS"
            elif "gcp" in path_list:
                cloud="GCP"
            else:
                cloud=""
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
                            test_name = row[0]
                            elapsed = float(row[3])
                            parallelism = row[4]
                            if parallelism == "NA":
                                parallelism = ""
                            else:
                                parallelism = ", " + parallelism + " Parallel Ops"
                            # Append filesystem and run number to each row
                            key = (filesystem_regex, cloud, f"{test_name}{parallelism}")
                            elapsed_times[key] += elapsed
                            counts[key] += 1

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

        header_row = ['filesystem','cloud', 'test-name', 'elapsed']

        writer.writerow(header_row)
        for key, elapsed_sum in elapsed_times.items():
            # Calculate average elapsed time
            avg_elapsed = elapsed_sum / counts[key]
            avg_elapsed = round(avg_elapsed,3)
            # Write row to the output file
            writer.writerow([key[0], key[1], key[2], avg_elapsed])
    print("R Testing CSV file generated successfully.")
