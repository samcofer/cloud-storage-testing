import re       # Import the regular expression module
import csv      # Import the CSV module
import os       # Import the OS module
import sys      # Import the SYS module

def parse_files_in_directory(directory, output_file):
    """
    Function to parse files in a directory and extract relevant information.
    Args:
        directory (str): Directory path containing files to parse.
        output_file (str): Path to the output CSV file.
    """

    # Define regex patterns to match desired content in the files
    patterns = [
        r'(\d+(?:\.\d+)?(?:\sk)?)\srequests completed in ((?:\d+(?:\.\d+)?)\s(?:ms|s)), (\d+(?:\.\d+)?(?:\s(?:GiB|MiB|KiB)))? (?:read|written), (\d+(?:\.\d+)?(?:\sk)?) iops, (\d+(?:\.\d+)?(?:\s(?:GiB|MiB|KiB))/s)',  # Pattern 1
        r'generated (\d+(?:\.\d+)?(?:\sk)?)\srequests in ((?:\d+(?:\.\d+)?)\s(?:s)), ((?:\d+(?:\.\d+)?(?:\s(?:GiB|MiB|KiB)))?), (\d+(?:\.\d+)?(?:\sk)?) iops, (\d+(?:\.\d+)?(?:\s(?:GiB|MiB|KiB))/s)',  # Pattern 2
        r'^min/avg/max/mdev = (\d+\.\d+\s(?:[a-zA-Z]{2}))\s/\s(\d+\.\d+\s(?:[a-zA-Z]{2}))\s/\s(\d+\.\d+\s(?:[a-zA-Z]{2}))\s/\s(\d+\.\d+\s(?:[a-zA-Z]{2}))'  # Pattern 3
    ]

    # Initialize lists for storing extracted data
    data = []
    values = []

    # Define headers for the CSV file
    headers = ['filesystem', 'cloud', 'test-name', 'requests-count', 'requests-time', 'requests-ops-volume', 'requests-iops', 'requests-throughput',
               'generated-count', 'generated-time', 'generated-ops-volume', 'generated-iops', 'generated-throughput',
               'min', 'avg', 'max', 'mdev']

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if "run" in filename:  # Check if filename contains "run"
            filepath = os.path.join(directory, filename)  # Construct full filepath
            path_list = os.path.abspath(filepath).split("/")

            if "azure" in path_list:
                cloud="AZURE"
            elif "aws" in path_list:
                cloud="AWS"
            elif "gcp" in path_list:
                cloud="GCP"
            else:
                cloud=""
            if os.path.isfile(filepath):  # Check if filepath is a file
                # Extract filesystem and io-test-name using regex
                filesystem_regex = re.match(r'^(.+?)-run-(ioping.*)$', filename).group(1)
                iotest_regex = re.match(r'^(.+?)-run-(ioping.*)$', filename).group(2)
                with open(filepath, 'r') as file:
                    lines = file.readlines()  # Read lines from the file
                    # Iterate through each line in the file
                    for line in lines:
                        # Iterate through regex patterns
                        for pattern in patterns:
                            match = re.match(pattern, line)  # Match pattern against line
                            if match:  # If pattern matches
                                values.extend(match.groups())  # Extend values with matched groups
                # Append extracted data to the data list
                data.append([filesystem_regex] + [cloud] + [iotest_regex] + [f'{values[i]}' for i in range(0, len(values))])
                values = []  # Reset values list for the next iteration

    # Write the extracted data to the output CSV file
    with open(f'{output_file}', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)  # Write headers to the CSV file
        for row in data:
            writer.writerow(row)  # Write each row of data to the CSV file

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py directory_path output_file")
        sys.exit(1)

    directory_path = sys.argv[1]  # Get directory path from command line argument
    output_file = sys.argv[2]      # Get output file path from command line argument

    # Check if directory exists
    if not os.path.isdir(directory_path):
        print("Error: Directory not found.")
        sys.exit(1)

    # Call the function to parse files in the directory and write to the output file
    parse_files_in_directory(directory_path, output_file)
    print("ioping Testing CSV file generated successfully.")
