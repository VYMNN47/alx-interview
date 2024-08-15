#!/usr/bin/python3
"""Module for stats function"""
import re
import sys


def stats():
    """reads stdin line by line and computes metrics"""
    file_size = 0
    counter = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                    405: 0, 500: 0}

    try:
        for line in sys.stdin:
            pattern = (
                r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \['
                r'(.*?)\] "GET /projects/260 HTTP/1.1" '
                r'(\d{3}) (\d+)'
            )
            match = re.search(pattern, line)
            if match:
                scode = int(match.group(3))
                fsize = int(match.group(4))
                if scode in status_codes:
                    status_codes[scode] += 1
                file_size += fsize

            counter += 1
            if counter >= 10:
                print_stats(file_size, status_codes)
                counter = 0

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(file_size, status_codes)


def print_stats(file_size, status_codes):
    """Prints the statistics"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    stats()
