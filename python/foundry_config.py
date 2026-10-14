import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

OPENAI_ENDPOINT = os.getenv(
    "OPENAI_ENDPOINT",
    "https://ai-102-foundry.services.ai.azure.com/openai/v1",
).rstrip("/")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT", "gpt-5.4-nano")


def create_openai_client() -> OpenAI:
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://ai.azure.com/.default",
    )
    return OpenAI(base_url=OPENAI_ENDPOINT, api_key=token_provider)
