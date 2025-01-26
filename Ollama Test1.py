import ollama

response = ollama.list()

res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user", 
            "content": "emoriable World War 2 dates and what happened there in very short?",
        },
    ],
    stream=True,
)
for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)


# #Create a new model with modelfile
# modelfile =""""
# FROM llama3.2
# SYSTEM You are going to answer very concise with as few words as needed
# PARAMETER temperature 0.1
# """

# ollama.create(model="Concise", modelfile=modelfile)

# res = ollama.generate(model="Concise", prompt="memoriable World War 2 dates and what happened there")
# print(res["response"])