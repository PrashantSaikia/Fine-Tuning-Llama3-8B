import time
import pandas as pd
from generate_qna import generate_question_and_answer

df = pd.read_parquet("processed_dataset_2024.parquet")

import time
import pandas as pd
from random import uniform
import botocore.exceptions

# Read the parquet file
df = pd.read_parquet("processed_dataset_2024.parquet")

# Initialize an empty list to store Q&A pairs
qa_data = []

# Function to generate question and answer with retries
def generate_with_retries(content, retries=3, delay=uniform(1, 2)):
    for attempt in range(retries):
        try:
            question, answer = generate_question_and_answer(content)
            return question, answer
        except (botocore.exceptions.ReadTimeoutError, botocore.exceptions.ConnectTimeoutError) as e:
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    print("Max retries reached. Skipping this content.")
    return None, None

# Iterate over each content in the dataframe
for i in range(len(df)):
    # Start the timer
    t = time.time()

    # Generate question and answer with retries
    question, answer = generate_with_retries(df.content[i])

    if question is not None and answer is not None:
        # Append the generated Q&A to the list
        qa_data.append({"Context": df.content[i], "Question": question, "Answer": answer})

    # Every 10th iteration, or at the end of the loop, save the data and clear the list
    if i % 10 == 0 or i == len(df) - 1:
        # Convert the list to a DataFrame
        qa_df = pd.DataFrame(qa_data)

        # Append the data to the CSV file
        qa_df.to_csv("Fine Tuning Dataset.csv", mode='a', header=(i == 0), index=False)

        # Clear the list after appending to CSV
        qa_data = []

        # Print progress
        print(f'Finished processing doc {i+1}')
        print(f"Time taken to generate QnA pairs from document {i-9} to {i+1}: {time.time()-t}s\n")
