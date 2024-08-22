import boto3, json, os, requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()
# Bedrock credentials
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')

def generate_question_and_answer(text_chunk):
    # Define the question prompt
    question_prompt = (
        f"""<s>[INST]
        You are a Professor writing an exam. Here is the provided context: 
        
        {text_chunk}
        
        You task is to formulate a single question that captures an important 
        fact or insight from the context, e.g. 'Describe the architecture of Midnight', or 
        'What should new employees do immediately after joining IOG as part of their onboarding procedure?, or
        'I recently had a business trip where I took a train to get to the destination, stayed at a hotel, and paid for my meals. 
        How do I submit expense reimbursement forms for it?'
        Restrict the question to the context information provided. 
        
        Simply respond with the question you generate. DO NOT begin your question with, "According to the provided context",
        or "Based on the provided context", etc.
        [/INST]"""
    )

    bedrock=boto3.client(service_name="bedrock-runtime", 
                         region_name="us-west-2",
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key
                        )
    
    payload={
        "prompt": question_prompt, 
        "max_tokens":200,
        "temperature":0.1,
        "top_p":0.15,
        "top_k":20
    }
    body=json.dumps(payload)
    model_id="mistral.mixtral-8x7b-instruct-v0:1"

    response=bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    response_body=json.loads(response.get("body").read())
    
    # Generate a question unconditionally
    question = response_body['outputs'][0]['text'].strip().replace('''""''', '')

    # Generate an answer unconditionally
    answer_prompt = (
        f"""
        Given the context: '{text_chunk}', give a detailed, complete and information packed answer 
        to the question: '{question}'. Use only the context to answer, do not give references. 
        Simply answer the question without editorial comments.
        """
    )
    bedrock=boto3.client(service_name="bedrock-runtime", 
                         region_name="us-west-2",
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key
                        )
    
    payload={
        "prompt": answer_prompt, 
        "max_tokens":4000,
        "temperature":0.1,
        "top_p":0.15,
        "top_k":20
    }
    body=json.dumps(payload)
    model_id="mistral.mixtral-8x7b-instruct-v0:1"

    response=bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    response_body=json.loads(response.get("body").read())
    
    # Generate a answer unconditionally
    answer = response_body['outputs'][0]['text'].strip()

    return question, answer

if __name__=="__main__":
    question, answer = generate_question_and_answer(doc.page_content)
    print(question)
    print('\n')
    print(answer)