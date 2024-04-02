import re  # Import the regular expression module
import csv  # Import the CSV module
import os   # Import the OS module
import sys  # Import the SYS module

def parse_files_in_directory(directory, output_file):
    """
    Function to parse files in a directory and extract relevant information.
    Args:
        directory (str): Directory path containing files to parse.
        output_file (str): Path to the output CSV file.
    """

    # Define the regex pattern to match the desired content in the files
    pattern = r'BEGIN - Running in .+\nVENV CREATE: Run duration = (\d+) milliseconds\nPIP UPDATE: Run duration = (\d+) milliseconds\nPYTORCH INSTALL: Run duration = (\d+) milliseconds\nCLEANUP: Run duration = (\d+) milliseconds\nEND'

    # Initialize a list to store the extracted data
    data = []

    # Define headers for the CSV file
    headers = ['filesystem', 'run-number', 'venv-creation(ms)', 'pip-update(ms)', 'pytorch-install(ms)', 'cleanup(ms)']

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if "run" in filename:  # Check if filename contains "run"
            filepath = os.path.join(directory, filename)  # Construct full filepath
            if os.path.isfile(filepath):  # Check if filepath is a file
                # Extract filesystem and run number using regex
                filesystem_regex = re.match(r'^(.+?)-run(\d).*$', filename).group(1)
                run_number_regex = re.match(r'^(.+?)-run(\d).*$', filename).group(2)
                with open(filepath, 'r') as file:
                    lines = file.read()  # Read contents of the file
                    # Iterate through matches of the regex pattern in the file
                    for match in re.finditer(pattern, lines):
                        # Append extracted data to the list
                        data.append([filesystem_regex] + [run_number_regex] + [match.group(1)] + [match.group(2)] + [match.group(3)] + [match.group(4)])

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
