import time
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = 'AIzaSyD6Fgx2K-_rM1P1IYfTUBKLuUi6Ew6Nf5w'  # Replace with your actual API key

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
        model = genai.GenerativeModel('gemini-pro')

        start_time = time.time()
        response = model.generate_content("What is the meaning of life?")
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Time taken: {elapsed_time} seconds")

        display(to_markdown(response.text))
        display(response.candidates)
