import re
import pandas as pd

def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Regular expressions to match each field in the text
    authors_pattern = r"%A (.*?)\n"   # Authors
    title_pattern = r"%T (.*?)\n"     # Title
    abstract_pattern = r"%X (.*?)\n"  # Abstract
    year_pattern = r"%D (.*?)\n"      # Year Published
    doi_pattern = r"%R (.*?)\n"       # DOI

    # Extract the fields using the patterns
    titles = re.findall(title_pattern, data)
    authors = re.findall(authors_pattern, data)
    abstracts = re.findall(abstract_pattern, data)
    years = re.findall(year_pattern, data)
    dois = re.findall(doi_pattern, data)

    # Make sure all lists are the same length by padding shorter lists with empty strings or None
    max_length = max(len(titles), len(authors), len(abstracts), len(years), len(dois))

    # Padding each list to make sure they all have the same length
    titles += [''] * (max_length - len(titles))
    authors += [''] * (max_length - len(authors))
    abstracts += [''] * (max_length - len(abstracts))
    years += [''] * (max_length - len(years))
    dois += [''] * (max_length - len(dois))

    # Combine the extracted data into a dictionary
    parsed_data = {
        "Title": titles,
        "Authors": authors,
        "Abstract": abstracts,
        "Year Published": years,
        "DOI": dois
    }

    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(parsed_data)
    
    return df
# Testing the function
file_path = "/Users/estherk/Box/HCI584_estherk/HCI684_SrAPP/docs/exportlist.txt" 
articles_df = parse_file(file_path)
print(articles_df.head())  # Print the first few rows to verify
