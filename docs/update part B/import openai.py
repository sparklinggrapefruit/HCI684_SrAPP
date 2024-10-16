

import os
from openai import OpenAI # pip install openai
from keys import open_ai_api_key # you must enter your OpenAI API key in a file called keys.py

client = OpenAI(
    api_key=open_ai_api_key
)


import pandas as pd
from tkinter import filedialog, Tk

def upload_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("Text files", "*.txt"),))
    if file_path:
        # Assuming each article is separated by a new line and each field by a comma.
        # Customize based on the format of your text file.
        df = pd.read_csv(file_path, delimiter=',', names=['Title', 'Authors', 'Abstract', 'Year', 'DOI'])
        print(df.head())  
        return df
    else:
        print("No file selected.")
        return None

# Testing file upload
if __name__ == "__main__":
    articles_df = upload_file()

##it works!
##"exportlist" file uploaded.

##Extracting data from the file.

