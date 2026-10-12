import asyncio
from openai import AsyncOpenAI
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://ai-102-foundry.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4-nano"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

async def ask(prompt):
    response = await client.responses.create(
        model=deployment_name,
        input=prompt
    )
    return response.output_text

async def main():
    # Issue three requests concurrently instead of one after another
    prompts = [
        "Explain quantum computing briefly.",
        "Summarize the benefits of async I/O.",
        "Give a one-sentence definition of machine learning."
    ]
    results = await asyncio.gather(*(ask(p) for p in prompts))
    for prompt, output in zip(prompts, results):
        print(f"Q: {prompt}\nA: {output}\n")

asyncio.run(main())