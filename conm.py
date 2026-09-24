import ollama

print("My AI Q&A Bot")
print("Type 'exit' to stop.\n")
messages = []

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break
    messages.append({
        "role": "user",
        "content": question
    })
    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    answer = response["message"]["content"]
    messages.append({
        "role": "assistant",
        "content": answer
    })

    print("Bot:", answer)