from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://ai-102-foundry.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4-nano"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

stream = client.responses.create(
    model=deployment_name,
    input="Write a short story about a robot learning to paint.",
    stream=True
)

for event in stream:
    print(event, end="", flush=True)