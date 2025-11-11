from openai import OpenAI
import os
from dotenv import load_dotenv

def read_file(filename:str)->str:
    try:
        return open(filename, "r").read()
    except FileNotFoundError:
        raise Exception(f"The incorrect input path is{filename}")

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Add it to your shell or .env file.")
    client = OpenAI(api_key=api_key)
    filename ="notes.txt"
    system_prompt = "Process these notes and convert them to LaTeX and add any relevant equations that seem necessary only provide latex in output nothing else:"
    contents = read_file(filename)
    response = client.responses.create(
        model ="gpt-4o",
        instructions = system_prompt,
        input = contents
    )
    output_path = "notes_to_latex"
    with open(output_path, "w") as f:
        f.write(response.output_text)
    print(f"Wrote LaTeX to {output_path}")

if __name__ == "__main__":
    main()