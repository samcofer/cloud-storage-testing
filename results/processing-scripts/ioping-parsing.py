import re
import csv
import os
import sys

def parse_files_in_directory(directory):
    pattern = r'^min/avg/max/mdev = (\d+\.\d+)\s([a-zA-Z]{2})\s/\s(\d+\.\d+)\s([a-zA-Z]{2})\s/\s(\d+\.\d+)\s([a-zA-Z]{2})\s/\s(\d+\.\d+)\s([a-zA-Z]{2})'
    data = []

    headers = ['filesystem', 'min', 'avg', 'max', 'mdev']

    for filename in os.listdir(directory):
        if "run" in filename:
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                filesystem_regex = re.match(r'(.+?)-run', filename).group(1)
                print(filesystem_regex)
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        match = re.match(pattern, line)
                        if match:
                            values = match.groups()
                            data.append([filesystem_regex] + [f'{values[i]} {values[i+1]}' for i in range(0, len(values), 2)])

    with open('parsed_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py directory_path")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Error: Directory not found.")
        sys.exit(1)

    parse_files_in_directory(directory_path)
