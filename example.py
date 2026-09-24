import ollama

print("AI Chat Bot")
print("Type exit to stop\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Stopped")
        break
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user",
              "content": question
            }
        ]
    )

    print("Bot:", response["message"]["content"])