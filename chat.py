
import ollama

print("Local AI Chatbot")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        continue

    try:
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        print("\nAI:", response["message"]["content"])

    except Exception as e:
        print("Error:", e)