from sentence_transformers import SentenceTransformer
import joblib
import numpy as np

# Load the sentence transformer model
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the saved classifier
classifier = joblib.load('models/log_classifier_model.pkl')

def classify_with_bert(log_message):
    # Encode the log message
    embedding = transformer_model.encode([log_message])  # shape: (1, 384)

    # Predict the class
    prediction = classifier.predict(embedding)

    return prediction[0]

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
        "Account with ID 103 deleted by admin"
    ]

    for message in log_messages:
        print(f"{message} -> {classify_with_bert(message)}")