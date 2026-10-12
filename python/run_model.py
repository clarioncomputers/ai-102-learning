from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://ai-102-foundry.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4-nano"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

response1 = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What is the capital of France?",
)

response2 = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What are the various areas in Paris called?",
    temperature=0.8,  # Higher temperature for more creativity
    previous_response_id=response1.id
)

print(response2.output_text)

# Generate a response using the OpenAI-compatible client
response3 = client.responses.create(
    model=deployment_name,
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

