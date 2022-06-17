import os
from typing import List
import openai
import argparse
import re

MAX_INPUT_LENGTH = 32

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type = str, required = True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    
    if validate_length(user_input):

        generate_tangents(user_input)
        generate_keywords(user_input)
    

    else: raise ValueError(f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}")

def validate_length(prompt: str):
    return len(prompt) <= MAX_INPUT_LENGTH



def generate_keywords(prompt: str): # list[str]:

# Load your API key from an environment variable or secret management service

    openai.api_key = os.getenv("OPENAI_API_KEY")

    updated_prompt = f"Generate words related to {prompt}: "

    print(updated_prompt)

    response = openai.Completion.create(model="text-davinci-002", prompt=updated_prompt, temperature=.7, max_tokens=64)
    
    #extract output text.
    keywords_text = response["choices"][0]["text"]

    #strip whitespace 
    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|\*|-", keywords_text)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]

    print(f"Keywords: {keywords_array}")

    #prevent cutoff response
    last_char = keywords_text[-1]

    if last_char not in {".", "!", "?"}:
        keywords_text += "..."
       
    return keywords_array


def generate_tangents(prompt: str): # -> str:

# Load your API key from an environment variable or secret management service

    openai.api_key = os.getenv("OPENAI_API_KEY")

    updated_prompt = f"Generate possible paths of further research for {prompt}: "

    print(updated_prompt)

    response = openai.Completion.create(model="text-davinci-002", prompt=updated_prompt, temperature=.6, max_tokens=64)
    
    #extract output text.
    guide_text = response["choices"][0]["text"]

    #strip whitespace 
    guide_text = guide_text.strip()

    #prevent cutoff response
    last_char = guide_text[-1]

    if last_char not in {".", "!", "?"}:
        guide_text += "..."
       

    print(f"Tangents: {guide_text}")   
    return guide_text


if __name__ == "__main__":
    main()