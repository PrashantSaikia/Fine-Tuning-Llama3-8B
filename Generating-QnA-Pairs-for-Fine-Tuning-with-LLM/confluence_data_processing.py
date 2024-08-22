import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_parquet("processed_dataset_2024.parquet")

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator="\n", strip=True)

df['content'] = df['content'].apply(extract_text_from_html)

df.to_parquet('processed_dataset_2024.parquet')