import asyncio
from azure.identity.aio import DefaultAzureCredential
from openai import AsyncOpenAI

endpoint = "https://ai-102-foundry.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4-nano"
scope = "https://ai.azure.com/.default"

async def main():
    async with DefaultAzureCredential() as credential:
        async def get_token():
            token = await credential.get_token(scope)
            return token.token

        async with AsyncOpenAI(
            base_url=endpoint,
            api_key=get_token,
        ) as client:
            async def ask(prompt):
                response = await client.responses.create(
                    model=deployment_name,
                    input=prompt,
                )
                return response.output_text

            prompts = [
                "Explain quantum computing briefly.",
                "Summarize the benefits of async I/O.",
                "Give a one-sentence definition of machine learning.",
            ]
            results = await asyncio.gather(*(ask(prompt) for prompt in prompts))

            for prompt, output in zip(prompts, results):
                print(f"Q: {prompt}\nA: {output}\n")

asyncio.run(main())