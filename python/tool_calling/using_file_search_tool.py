# Key features include:
# Document-grounded answers - Responses are based on your uploaded files
# Semantic retrieval - Finds relevant passages by meaning, not only exact keyword matches
# Vector store integration - Search across one or more indexed document collections
# Citations and transparency - Include matched results for debugging and traceability
# Better enterprise relevance - Use organization-specific knowledge in model outputs



from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from openai import OpenAI
from openai.types import Model
from python.foundry_config import MODEL_DEPLOYMENT, create_openai_client

client = create_openai_client()

from openai import OpenAI

# Create vector store and upload a file
vector_store = client.vector_stores.create(name="policy-docs")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("MAICPP-Benefits-Guide.pdf", "rb")
)

# Get response using the file_search tool
response = client.responses.create(
    model=MODEL_DEPLOYMENT,
    instructions="You are an AI assistant that provides information from HR policy documents.",
    input="What's the benefits for Partner Launch Benefits?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    }],
    include=["file_search_call.results"]
)
print(response.output_text)

# How the file_search tool works
#   The general process for using the file_search tool is:
# 1.    You prepare files - Upload documents to a vector store.
# 2.    You send a request - Include file_search in the tools array with vector store IDs.
# 3.    Model performs retrieval - It searches indexed chunks for relevant content.
# 4.    Results are injected - Matching passages are provided to the model.
# 5.    Response is generated - The model answers using retrieved document context.

#    Best practices
#    Use high-quality source files - Clean, current documents improve retrieval accuracy
#    Write focused prompts - Ask specific questions to reduce ambiguous matches
#    Scope vector stores carefully - Separate domains (HR, legal, finance) when helpful
#    Include retrieval results in development - Use response includes for troubleshooting
#    Review answers for critical workflows - Keep human validation in high-stakes scenarios

#    Limitations to know about
#    Answer quality depends on document quality, coverage, and chunk relevance
#    Very large or mixed-domain stores can return less focused context
#    Updated source files may require re-indexing before new content is searchable
#    Retrieval improves grounding but doesn't replace human review for sensitive decisions
#    Used well, file_search turns a general-purpose model into a domain-aware assistant that can answer from the documents your team actually uses.