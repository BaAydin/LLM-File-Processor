import ollama

response = ollama.list()

res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user", 
            "content": "How many R's does the word strawberry have?",
        },
    ],
    stream=True,
)
for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)
