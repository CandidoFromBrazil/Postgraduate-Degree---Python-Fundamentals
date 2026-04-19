from collections import Counter

# 1. Setup - Point to your log file
log_file_path = 'access.log'
failed_ips = []

# 2. Process - Loop through every line in the log
with open(log_file_path, 'r') as file:
    for line in file:
        # Check if the line contains a 401 error (Unauthorized)
        if ' 401 ' in line:
            # Grab the IP address (usually the first word in the line)
            ip = line.split()[0]
            failed_ips.append(ip)

# 3. Report - Count them and print if they hit a limit
counts = Counter(failed_ips)

print("--- Potential Brute Force Attacks ---")
for ip, count in counts.items():
    if count > 5:  # Only show IPs with more than 5 failures
        print(f"IP: {ip} | Failed Attempts: {count}")