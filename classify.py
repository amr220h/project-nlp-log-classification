from processer_regex import classify_with_regex
from processer_bert import classify_with_bert
from processer_llm import classify_with_llm

def classify(log_messages_with_source):
    labels = []
    for source, log_message in log_messages_with_source:
        label = classify_log_message(source, log_message)
        labels.append((source, label))
    return labels


def classify_log_message(source, log_message):
    label = None
    if source == 'LegacyCRM':
        label = classify_with_bert(log_message)
        if label is None:
            label = classify_with_llm(log_message)
    if label is None:
        label = classify_with_regex(log_message)
    if label is None:
        return "Unknown"
    else:
        return label
if __name__ == "__main__":
    # Example usage
    log_messages_with_source = [
        ("LegacyCRM", "User User123 logged in at 2023-10-01 12:00:00"),
        ("LegacyCRM", "Backup started at 2023-10-01 12:05:00"),
        ("LegacyCRM", "Backup completed successfully at 2023-10-01 12:10:00"),
        ("OtherSystem", "System updated to version 1.2.3"),
        ("OtherSystem", "File report.pdf uploaded successfully by user User123"),
        ("OtherSystem", "Disk cleanup completed successfully at 2023-10-01 12:15:00"),
        ("OtherSystem", "System reboot initiated by user User123"),
        ("OtherSystem", "asmdsaskaasdasasasdasn"),
        ("OtherSystem", "Account with ID 789 updated by admin"),
        ("OtherSystem", "Account with ID 101 deleted by admin")
    ]

    for source, message in log_messages_with_source:
        print(f"Source: {source} | Log Message: {message} | Classification: {classify_log_message(source, message)}")
    print(f"Log Message: {message} | Classification: {classify_log_message(source, message)}")