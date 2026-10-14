from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from python.foundry_config import MODEL_DEPLOYMENT, create_openai_client

client = create_openai_client()


response1 = client.responses.create(
    model=MODEL_DEPLOYMENT,
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What is the capital of France?",
)

response2 = client.responses.create(
    model=MODEL_DEPLOYMENT,
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What are the various areas in Paris called?",
    temperature=0.8,  # Higher temperature for more creativity
    previous_response_id=response1.id
)

print(response2.output_text)

# Generate a response using the OpenAI-compatible client
response3 = client.responses.create(
    model=MODEL_DEPLOYMENT,
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What aere their names?",
    previous_response_id=response2.id
)

# Display the response
print(response3.output_text)


#print(f"Response: {response3.output_text}")
#print(f"Response ID: {response3.id}")
#print(f"Status: {response3.status}")
#print(f"answer: {response3.output[0]}")
