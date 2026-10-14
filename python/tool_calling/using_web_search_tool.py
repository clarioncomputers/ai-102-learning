# The web_search tool gives a generative AI model access to current, external information at runtime.

#Key features include:
# Live information retrieval - Get recent information not available in static model training data
# Source-grounded responses - Build answers from retrieved web content
# Reduced hallucination risk - Improve reliability by checking external sources
# Automatic query generation - The model decides when and how to search based on user intent
# Seamless user experience - Search and response generation happen in one flow

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from openai import OpenAI
from openai.types import Model
from python.foundry_config import MODEL_DEPLOYMENT, create_openai_client

client = create_openai_client()

# Get response using the web_search tool
response = client.responses.create(
    model=MODEL_DEPLOYMENT,
    instructions="You are an AI assistant. Use web search when current information is required.",
    input="What are three major announcements from Microsoft Build this week?",
    tools=[{"type": "web_search"}]
)

print(response.output_text)



# The general process for using the web_search tool is:
# 1. You send a request - Include a web search tool in the tools array.
# 2. Model evaluates the question - It decides whether fresh web data is needed.
# 3. Search is performed - The model issues one or more search queries.
# 4. Results are reviewed - Relevant pages are selected and summarized.
# 5. Response is generated - The model combines search findings into the final answer.

# Best practices:
# Ask time-aware questions clearly - Include words like "latest", "current", or date ranges when needed
# Set expectations for sources - Prompt for reputable or official sources when accuracy matters
# Request concise outputs - Ask for short summaries with key points to reduce noise
# Verify critical facts - For high-stakes scenarios, independently validate important claims
# Track usage and latency - Web retrieval can increase response time and token usage

# Limitations to know about:
# Results depend on what is publicly available and indexable at query time
# Source quality can vary, so output may still require human review
# Retrieved content may change over time, so repeated runs can produce different answers
# Some environments may apply regional, policy, or network restrictions to web access

# Used well, web_search helps your model move from static knowledge to timely, source-aware answers that are more useful in real-world workflows.