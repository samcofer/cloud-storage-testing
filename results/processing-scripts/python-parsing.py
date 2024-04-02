import re
import csv
import os
import sys

def parse_files_in_directory(directory,output_file):

    pattern = r'BEGIN - Running in .+\nVENV CREATE: Run duration = (\d+) milliseconds\nPIP UPDATE: Run duration = (\d+) milliseconds\nPYTORCH INSTALL: Run duration = (\d+) milliseconds\nCLEANUP: Run duration = (\d+) milliseconds\nEND'   # Replace 'pattern3' with your third regex pattern
    data = []
    values = []
    headers = ['filesystem', 'run-number(ms)', 'venv-creation(ms)','pip-update(ms)', 'pytorch-install(ms)','cleanup(ms)']

    for filename in os.listdir(directory):
        if "run" in filename:
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                filesystem_regex = re.match(r'^(.+?)-run(\d).*$', filename).group(1)
                run_number_regex = re.match(r'^(.+?)-run(\d).*$', filename).group(2)
                with open(filepath, 'r') as file:
                    lines = file.read()
                    for match in re.finditer(pattern, lines):
                        data.append([filesystem_regex] + [run_number_regex] + [match.group(1)] + [match.group(2)] + [match.group(3)] + [match.group(4)])

    with open(f'{output_file}', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py directory_path output_file")
        sys.exit(1)

    directory_path = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.isdir(directory_path):
        print("Error: Directory not found.")
        sys.exit(1)

    parse_files_in_directory(directory_path,output_file)
