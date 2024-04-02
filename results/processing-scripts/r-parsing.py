import re
import csv
import os
import sys


modified_rows = []
unique_rows = []
seen = set()


def parse_files_in_directory(directory,output_file):

    for filename in os.listdir(directory):
        if "results" in filename:
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                filesystem_regex = re.match(r'^(.+?)-run(\d).*$', filename).group(1)
                run_number_regex = re.match(r'^(.+?)-run(\d).*$', filename).group(2)
                with open(filepath, 'r') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    for row in rows:
                        new_row = [filesystem_regex, run_number_regex] + row
                        modified_rows.append(new_row)
                    # Remove duplicate rows while preserving order

    for row in modified_rows:
        row_tuple = tuple(row)
        if row_tuple is not None:
            if tuple(row) not in seen:
                unique_rows.append(row)
                seen.add(row_tuple)




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

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(unique_rows)
