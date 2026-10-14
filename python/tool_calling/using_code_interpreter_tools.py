# Code interpreter tool can do the following:
# Dynamic Python Execution: The model writes and runs Python code in a sandboxed environment
# File Handling: Upload, process, and download files (CSV, JSON, images, and so on)
# Data Analysis: Perform calculations, statistical analysis, and data transformations on the fly
# Real-time Feedback: The model sees code execution results and can iterate or fix errors
# Complex Problem Solving: Tackle math problems, simulations, and logic puzzles through executable code

# code_interpreter process is like this: - 
# 1. You send a request: Include code_interpreter in your tools array.
# 2. Model analyzes the task: The model determines if code execution is needed.
# 3. Model generates code: The model writes Python code to accomplish the task.
# 4. Code runs: The code runs in a sandboxed environment with access to common libraries (for example, pandas, numpy, and math).
# 5. Results returned: The model receives the output and incorporates it into its response.
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from python.foundry_config import MODEL_DEPLOYMENT, create_openai_client

client = create_openai_client()

# Get response using the code_interpreter tool
response = client.responses.create(
    model=MODEL_DEPLOYMENT,
    instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
    input="What is the square root of 16?",
    tools=[{"type": "code_interpreter",
            "container": {"type": "auto"}}]
)
print(response.output_text)

# Model uses Python to do this using code above: -
#
# import math
#
# Calculate the square root of 16
# square_root = math.sqrt(16)
# square_root

# BEST PRACTICE -
# Be specific: Describe the data format and expected output clearly. Many models internally use the name python tool to identify the code_interpreter tool - so use this language in your instructions.
# Provide context: Include relevant domain knowledge in your prompts
# Validate results: Always review AI-generated code for correctness before using in production
# Monitor costs: Code execution adds tokens; complex operations may use more resources
# Leverage libraries: Common packages like pandas, numpy, and matplotlib are pre-installed
# Error handling: The model can see errors and will attempt to fix them automatically

# LIMITATIONS ARE:
# Be specific: Describe the data format and expected output clearly. Many models internally use the name python tool to identify the code_interpreter tool - so use this language in your instructions.
# Provide context: Include relevant domain knowledge in your prompts
# Validate results: Always review AI-generated code for correctness before using in production
# Monitor costs: Code execution adds tokens; complex operations may use more resources
# Leverage libraries: Common packages like pandas, numpy, and matplotlib are pre-installed
# Error handling: The model can see errors and will attempt to fix them automatically