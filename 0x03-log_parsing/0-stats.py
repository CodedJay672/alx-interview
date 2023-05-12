#!/usr/bin/python3
""" script that reads stdin line by line
    and computes metrics"""

import sys


def print_metrics(ip_addresses, status_codes, file_sizes):
    """ function that prints metrics """

    total_file_size = sum(file_sizes)
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes):
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            print(f"{status_code}: {status_codes[status_code]}")


ip_addresses = []
status_codes = {}
file_sizes = []
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        if line_count % 10 == 0:
            print_metrics(ip_addresses, status_codes, file_sizes)
        try:
            ip_address, _, _, _, status_code, file_size = line.split()
            ip_addresses.append(ip_address)
            status_codes[
                    int(status_code)
                    ] = status_codes.get(
                            int(status_code), 0
                            ) + 1
            file_sizes.append(int(file_size))
        except ValueError:
            pass
except KeyboardInterrupt:
    print_metrics(ip_addresses, status_codes, file_sizes)
