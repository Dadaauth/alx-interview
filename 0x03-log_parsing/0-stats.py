#!/usr/bin/python3
"""A module documentation"""

import sys
import signal

line_count = 0
total_file_size = 0


def check_line_format(line):
    """Check the format of the line and return the details of the line"""
    ip_address = line.split(" -", 1)
    timestamp = ip_address[1].strip()
    timestamp = timestamp.split('[')
    timestamp = timestamp[1].split(']')
    request = timestamp[1]
    request = request.strip()
    request = request.split(" ")
    protocol = request[0]
    path = request[1]
    http_ver = request[2]
    status_code = request[3]
    file_size = request[4]
    protocol = protocol.strip("\"")
    http_ver = http_ver.strip("\"")
    timestamp = timestamp[0]
    ip_address = ip_address[0]
    return (ip_address, timestamp, protocol,
            path, http_ver, status_code, file_size)


def print_codes(status_codes):
    """Print the status codes and their count"""
    for st_code in status_codes:
        if st_code["count"] > 0:
            print(f"{st_code["code"]}: {st_code["count"]}")


status_codes = [
    {"code": 200, "count": 0},
    {"code": 301, "count": 0},
    {"code": 400, "count": 0},
    {"code": 401, "count": 0},
    {"code": 403, "count": 0},
    {"code": 404, "count": 0},
    {"code": 405, "count": 0},
    {"code": 500, "count": 0},
]


def sigint_handler(signum, frame):
    """Signal handler for SIGINT signal"""
    print("Signal handler with signal", signum)
    print_updates()


signal.signal(signal.SIGINT, sigint_handler)


def print_updates():
    """Print the updates of the status codes and the total file size"""
    print(f"File size: {total_file_size}")
    print_codes(status_codes)
    for st_code in status_codes:
        st_code["count"] = 0


for line in sys.stdin:
    details = check_line_format(line)
    total_file_size += int(details[-1])
    status_code = int(details[-2])
    for st_code in status_codes:
        if st_code["code"] == status_code:
            st_code["count"] += 1
            break
    if line_count == 10:
        print_updates()
        line_count = 0
    line_count += 1
