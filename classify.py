from processer_regex import classify_with_regex
from processer_bert import classify_with_bert
from processer_llm import classify_with_llm

def classify_log_messages(source, log_message):
    label = None

    if source == 'LegacyCRM':
        label = classify_with_bert(log_message)
        if label is None:
            label = classify_with_llm(log_message)

    if label is None:
        label = classify_with_regex(log_message)

    if label is None:
        label = classify_with_bert(log_message)

    return label if label is not None else "Unknown"


def classify(log_messages_with_source):
    labels = []
    for source, message in log_messages_with_source:
        label = classify_log_messages(source, message)
        labels.append((source, label))
    return labels


if __name__ == "__main__":
    log_messages = [
        ("LegacyCRM", "User User123 logged in at 2023-10-01 12:00:00"),
        ("LegacyCRM", "Backup started at 2023-10-01 12:05:00"),
        ("OtherSystem", "Backup completed successfully at 2023-10-01 12:10:00"),
        ("OtherSystem", "System updated to version 1.2.3"),
        ("OtherSystem", "File report.pdf uploaded successfully by user User123"),
        ("OtherSystem", "Disk cleanup completed successfully at 2023-10-01 12:15:00"),
        ("OtherSystem", "System reboot initiated by user User123"),
        ("LegacyCRM", "asmdsaskaasdasasasdasn"),
        ("OtherSystem", "Account with ID 789 updated by admin"),
        ("OtherSystem", "Account with ID 101 deleted by admin"),
    ]

    for source, message in log_messages:
        print(f"Source: {source} | Log Message: {message} | Classification: {classify_log_messages(source, message)}")
