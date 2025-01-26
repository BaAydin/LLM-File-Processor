import ollama
import os

model = "llama3.2"

# Paths to input and output files
input_file = "./Data/Tolkien_Werke.txt"
output_file = "./Data/Tolkien-Werke_eingeordnet.txt"

#Check if input file exists
if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")
    exit(1)
    
# Read the input file
with open(input_file, "r") as f:
    items =f.read().strip()
    
# Prompt task for the model
prompt = f"""

Sortiere die Tolkien_Werke nach dem veröffentlichungsdatum

Hier sind die Werke: {items}

"""

#Send the prompt and get a response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print(generated_text)
    
    #Write to the output file
    with open(output_file, "w") as f:
        f.write(generated_text.strip())
        
    print(f"saved to '{output_file}'.")
except Exception as e:
    print("An error occured:", str(e))