
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from python.foundry_config import MODEL_DEPLOYMENT, create_openai_client

client = create_openai_client()

# Track responses
last_response_id = None

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Get a response
    response = client.responses.create(
                model=MODEL_DEPLOYMENT,
                instructions="You are a helpful AI assistant that explains technology concepts clearly.",
                input=input_text,
                previous_response_id=last_response_id.id if last_response_id else None
    )
    assistant_text = response.output_text
    print("\nAssistant:", assistant_text)
    last_response_id = response
