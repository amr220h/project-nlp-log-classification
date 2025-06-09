from processer_regex import classify_with_regex


def classify_log_messages(log_messages):
  label = classify_with_regex(log_messages)
  if label is None:
    return "Unknown"
  else:
    return label

def classify(log_message):
    labels = []
    for source, log_message in log_message:
        label = classify_log_messages(source,log_message)
        labels.append((source, label))
    return labels

if __name__ == "__main__":
  # Example usage
  log_messages = [
      "User User123 logged in at 2023-10-01 12:00:00",
      "Backup started at 2023-10-01 12:05:00",
      "Backup completed successfully at 2023-10-01 12:10:00",
      "System updated to version 1.2.3",
      "File report.pdf uploaded successfully by user User123",
      "Disk cleanup completed successfully at 2023-10-01 12:15:00",
      "System reboot initiated by user User123",
      "asmdsaskaasdasasasdasn",
      "Account with ID 789 updated by admin",
      "Account with ID 101 deleted by admin"
  ]

  for message in log_messages:
    print(f"Log Message: {message} | Classification: {classify_log_messages(message)}")