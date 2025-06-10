from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq = Groq()
def classify_with_llm(log_message):
    # Define the prompt for the LLM
    prompt = f''''Classify the following log message into one of the following categories:
    User Action, System Notification, Other. Provide only the category name as the output.
    
    Log Message: {log_message}'''

    
prompt = "Classify the following log message: 'User User123 logged in at 10:00 AM'"

chat_completion = groq.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
      
        {
            "role": "user",
            "content": prompt,
        }
    ],
    
)

print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    # Example usage
    print(classify_with_llm("User User123 logged in at 10:00 AM"))

    print(classify_with_llm("Backup started at 11:00 AM"))
    print(classify_with_llm("Backup completed successfully at 11:30 AM"))
    