import re
import csv
import os
import sys

def parse_files_in_directory(directory,output_file):

    patterns = [
        r'(\d+(?:\.\d+)?(?:\sk)?)\srequests completed in ((?:\d+(?:\.\d+)?)\s(?:ms|s)), (\d+(?:\.\d+)?(?:\s(?:GiB|MiB|KiB)))? (?:read|written), (\d+(?:\.\d+)?(?:\sk)?) iops, (\d+(?:\.\d+)?(?:\s(?:GiB|MiB|KiB))/s)',   # Replace 'pattern3' with your third regex pattern
        r'generated (\d+(?:\.\d+)?(?:\sk)?)\srequests in ((?:\d+(?:\.\d+)?)\s(?:s)), ((?:\d+(?:\.\d+)?(?:\s(?:GiB|MiB|KiB)))?), (\d+(?:\.\d+)?(?:\sk)?) iops, (\d+(?:\.\d+)?(?:\s(?:GiB|MiB|KiB))/s)',
        r'^min/avg/max/mdev = (\d+\.\d+\s(?:[a-zA-Z]{2}))\s/\s(\d+\.\d+\s(?:[a-zA-Z]{2}))\s/\s(\d+\.\d+\s(?:[a-zA-Z]{2}))\s/\s(\d+\.\d+\s(?:[a-zA-Z]{2}))'  # Replace 'pattern2' with your second regex pattern
    ]
    data = []
    values = []
    headers = ['filesystem', 'io-test-name','requests-count', 'requests-time','requests-ops-volume','requests-iops', 'requests-throughput',
               'generated-count','generated-time','generated-ops-volume', 'generated-iops', 'generated-throughput',
               'min', 'avg', 'max', 'mdev']

    for filename in os.listdir(directory):
        if "run" in filename:
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                filesystem_regex = re.match(r'^(.+?)-run-(ioping.*)$', filename).group(1)
                iotest_regex = re.match(r'^(.+?)-run-(ioping.*)$', filename).group(2)
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        for pattern in patterns:
                            match = re.match(pattern, line)
                            if match:
                                values.extend(match.groups())
                data.append([filesystem_regex] + [iotest_regex] + [f'{values[i]}' for i in range(0, len(values))])
                values = []

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
