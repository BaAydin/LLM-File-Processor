# LLM-File-Processor

Ein **Python-Skript** zur Verarbeitung von Textdateien mit einem lokalen LLM (z. B. Ollama). Das Skript liest den Inhalt einer Datei, generiert einen promptbasierten Text für das LLM und speichert die Antwort in einer neuen Datei.

## Funktionen

- **read_file**: Liest den Inhalt einer Datei und gibt ihn als String zurück.
- **write_to_new_file**: Schreibt den gegebenen Inhalt in eine neue Datei.
- **generate_prompt**: Erstellt einen generischen Prompt für das LLM unter Berücksichtigung des Dateiinhalts und der Aufgabe.
- **process_with_llm**: Verarbeitet eine Datei mit einem LLM basierend auf einer Aufgabe und speichert das Ergebnis in einer neuen Datei.

## Installation

1. Stelle sicher, dass **Python 3.x** installiert ist.
2. **Ollama** muss im Hintergrund laufen. Du kannst es über die Ollama-Website herunterladen und installieren: [Ollama Download](https://ollama.com/).

3. Installiere das Ollama-Paket:
   ```bash
   pip install ollama

