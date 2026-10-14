from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from python.foundry_config import MODEL_DEPLOYMENT, create_openai_client

client = create_openai_client()

response = client.responses.create(
    model=MODEL_DEPLOYMENT,
    input="What is the capital of France?",
)

print(f"answer: {response.output[0]}")
