import os       # Import the OS module
import csv      # Import the CSV module
import sys      # Import the SYS module

def parse_directory(directory):
    """
    Function to parse files in a directory and extract relevant information.
    Args:
        directory (str): Directory path to parse.
    Returns:
        dict_values: Values of the file pairs with their attributes.
    """

    # Dictionary to store file pairs with their attributes
    file_pairs = {}
    cloud = ""
    # Traverse the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            basename = os.path.basename(filepath)

            path_list = os.path.abspath(filepath).split("/")

            if "azure" in path_list:
                cloud="AZURE"
            elif "aws" in path_list:
                cloud="AWS"
            elif "gcp" in path_list:
                cloud="GCP"
            else:
                cloud=""

            # Read the content of the file
            with open(filepath, 'r') as file:
                content = file.read()


            # Find the index of "-run"
            index = basename.find("-run")
            if index == -1:
                continue  # If "-run" is not found, skip the file

            # Extract the prefix
            prefix = basename[:index]

            # Check if prefix already exists
            if prefix in file_pairs:
                file_pairs[prefix]['cloud'] = cloud
                file_pairs[prefix]['test-name'] = 'acl-and-lock-testing'
                # Check if file contains extended ACL support
                extended_acl_support = int("Extended ACLs are supported" in content)
                file_pairs[prefix]['extended-acl-support'] = max(file_pairs[prefix]['extended-acl-support'], extended_acl_support)
                # Check if file contains link-based file locks
                link_based_locks = int("Your filesystem appears to support link-based locks" in content)
                file_pairs[prefix]['linkbased-file-locks'] = max(file_pairs[prefix]['linkbased-file-locks'], link_based_locks)


            else:
                # Create a new entry
                file_pairs[prefix] = {
                    'cloud': cloud,
                    'filesystem': prefix,
                    'test-name': 'acl-and-lock-testing',
                    'extended-acl-support': int("Extended ACLs are supported" in content),
                    'linkbased-file-locks': int("Your filesystem appears to support link-based locks" in content)
                }

    return file_pairs.values()

def write_to_csv(data, output_file):
    """
    Function to write data to a CSV file.
    Args:
        data (dict_values): Values of the file pairs with their attributes.
        output_file (str): Path to the output CSV file.
    """

    # Define the header of the CSV file
    header = ['filesystem','cloud','test-name', 'extended-acl-support', 'linkbased-file-locks']

    # Write data to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script_name.py directory_path output_csv_file")
        sys.exit(1)

    directory_path = sys.argv[1]  # Get directory path from command line argument
    output_file = sys.argv[2]     # Get output file path from command line argument

    # Check if directory exists
    if not os.path.isdir(directory_path):
        print("Error: The provided directory path is invalid.")
        sys.exit(1)

    # Parse directory and write data to CSV
    file_pairs = parse_directory(directory_path)
    write_to_csv(file_pairs, output_file)
    print("App Testing CSV file generated successfully.")
