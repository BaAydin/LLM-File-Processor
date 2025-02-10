import os
import ollama

def read_file(file_path):
    """Liest den Inhalt einer Datei und gibt ihn als String zurück."""
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def write_to_new_file(file_path, content):
    """Schreibt den gegebenen Inhalt in eine neue Datei."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Fehler beim Erstellen der Datei: {e}")

def generate_prompt(user_input, file_content, task_description):
    """Erstellt einen generischen Prompt für das LLM."""
    return f"""
    [KONTEXT]
    {file_content}
    
    [AUFGABE]
    {task_description}
    
    [EINGABE]
    {user_input}
    
    Antworte entsprechend der Aufgabe basierend auf dem gegebenen Kontext.
    """

def process_with_llm(model, user_input, file_path, task_description, output_file_path):
    """Verarbeitet eine Datei mit einem LLM basierend auf einer Aufgabe und speichert das Ergebnis in einer neuen Datei."""
    file_content = read_file(file_path)
    prompt = generate_prompt(user_input, file_content, task_description)
    
    response = ollama.generate(model=model, prompt=prompt)
    result_text = response.get("response", "")
    
    # Speichern des Outputs in einer neuen Datei
    write_to_new_file(output_file_path, result_text)
    return result_text

# Beispielaufruf
if __name__ == "__main__":
    MODEL_NAME = "llama3.2"
    FILE_PATH = "./Data/input.txt"
    OUTPUT_FILE_PATH = "./Data/output.txt" 
    TASK_DESCRIPTION = "Sortieren."
    
    user_input = "Von größter Zahl bis zur kleinsten."
    output = process_with_llm(MODEL_NAME, user_input, FILE_PATH, TASK_DESCRIPTION, OUTPUT_FILE_PATH)
    print("LLM Output:\n", output)
