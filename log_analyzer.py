import re
from collections import Counter

def analyze_logs(log_file):
    with open(log_file, "r") as file:
        logs = file.readlines()

    error_pattern = r"(ERROR|WARNING|CRITICAL)"
    matched = []

    for line in logs:
        match = re.search(error_pattern, line)
        if match:
            matched.append(match.group())

    counts = Counter(matched)

    print("=== Log Analysis Summary ===")
    for level, count in counts.items():
        print(f"{level}: {count} occurrences")

if __name__ == "__main__":
    analyze_logs("system_logs.txt")
