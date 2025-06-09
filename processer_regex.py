import re

def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out).*": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.*": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.*": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action",
        r"Account with ID .* updated by .*": "User Action",
        r"Account with ID .* deleted by .*": "User Action",



    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label

    return "Other"

print('-------------------------------------')
if __name__ == "__main__":
    # Example usage
    log_messages = [
        "User User123 logged in at 10:00 AM",
        "Backup started at 11:00 AM",
        "Backup completed successfully at 11:30 AM",
        "System updated to version 1.2.3",
        "File report.pdf uploaded successfully by user User456",
        "Disk cleanup completed successfully at 12:00 PM",
        "System reboot initiated by user User789",
        "Account with ID 101 created by admin",
        "Account with ID 102 updated by admin",
        "Account with ID 103 deleted by admin",
        'hi my name is amr khaled my age is 19'
    ]

    for message in log_messages:
        print(f"{message} -> {classify_with_regex(message)}")