from openai import OpenAI
def read_file(filename:str)->str:
    try:
        return open(filename,"r")
    except FileNotFoundError:
        raise Exception(f"The incorrect input path is{filename}")

def main():
   filename ="notes.txt"
   concat_return = "Process these notes and convert them to LaTeX and add any relevant equations that seem necessary:"
   contents = read_file(filename) 
   concat_return = concat_return + contents
   response = client.responses()
