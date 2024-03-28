import re

# Sample text
text = """
--- /elastic-san-same-zone-run (ext4 /dev/dm-6) ioping statistics ---
7.10 k requests completed in 29.9 s, 1.73 GiB read, 237 iops, 59.5 MiB/s
generated 7.10 k requests in 30.0 s, 1.73 GiB, 236 iops, 59.2 MiB/s
min/avg/max/mdev = 2.59 ms / 4.20 ms / 25.6 ms / 1.01 ms
"""

# Regular expressions to extract data
completed_regex = r'(\d+(?:\.\d+)?\s*(?:[kM])?)\s*requests completed in (\d+\.\d+)\s*(m?s), (\d+(?:\.\d+)?)\s*(?:MiB)?\s*(?:read|written), (\d+)\s*iops, (\d+(?:\.\d+)?)\s*(?:MiB)?/s'
generated_regex = r'generated (\d+(?:\.\d+)?\s*(?:[kM])?)\s*requests in (\d+\.\d+)\s*s, (\d+(?:\.\d+)?)\s*(?:MiB)?, (\d+)\s*iops, (\d+(?:\.\d+)?)\s*(?:MiB)?/s'
min_avg_max_mdev_regex = r'min/avg/max/mdev = (\d+\.\d+)\s*(m?s) / (\d+\.\d+)\s*(m?s) / (\d+\.\d+)\s*(m?s) / (\d+\.\d+)\s*(u?s)'

# Extracting data using regular expressions
completed_match = re.search(completed_regex, text)
generated_match = re.search(generated_regex, text)
min_avg_max_mdev_match = re.search(min_avg_max_mdev_regex, text)

# Echoing important data
if completed_match:
    print("Completed requests:")
    print("Number of requests:", completed_match.group(1))
    print("Time taken:", completed_match.group(2), completed_match.group(3))
    print("Data:", completed_match.group(4), "MiB")
    print("IOPS:", completed_match.group(5))
    print("Data transfer rate:", completed_match.group(6), "MiB/s")

if generated_match:
    print("\nGenerated requests:")
    print("Number of requests:", generated_match.group(1))
    print("Time taken:", generated_match.group(2), "s")
    print("Data:", generated_match.group(3), "MiB")
    print("IOPS:", generated_match.group(4))
    print("Data transfer rate:", generated_match.group(5), "MiB/s")

if min_avg_max_mdev_match:
    print("\nMinimum/Average/Maximum/Deviation:")
    print("Minimum:", min_avg_max_mdev_match.group(1), min_avg_max_mdev_match.group(2))
    print("Average:", min_avg_max_mdev_match.group(3), min_avg_max_mdev_match.group(4))
    print("Maximum:", min_avg_max_mdev_match.group(5), min_avg_max_mdev_match.group(6))
    print("Deviation:", min_avg_max_mdev_match.group(7), min_avg_max_mdev_match.group(8))
