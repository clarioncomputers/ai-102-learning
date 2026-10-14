#
# The function tool (function calling) lets a model decide when to call named tools you expose in your application. The model doesn't run your business logic directly. Instead, it returns a structured function call, your code runs the function, and then you pass the function output back to the model.
# 
# This pattern is ideal for connecting model reasoning to real-world systems like APIs, databases, business workflows, and utility functions.
#
# Key features include:
#
# Structured tool calls - The model emits explicit function-call requests
# Developer-controlled execution - Your application decides how and where functions run
# Reliable integration pattern - Call APIs, internal services, or helper utilities safely
# Multi-turn orchestration - Return tool output and let the model continue reasoning
# Grounded responses - Answers can include live, system-generated data


# Key features include:

# Structured tool calls - The model emits explicit function-call requests
# Developer-controlled execution - Your application decides how and where functions run
# Reliable integration pattern - Call APIs, internal services, or helper utilities safely
# Multi-turn orchestration - Return tool output and let the model continue reasoning
# Grounded responses - Answers can include live, system-generated data


from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from openai import OpenAI
from openai.types import Model
from python.foundry_config import MODEL_DEPLOYMENT, create_openai_client

import time

# Function to get the current time
def get_time():
    return f"The time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"


# Main function
def main():
    client = create_openai_client()

    function_tools = [
        {
            "type": "function",
            "name": "get_time",
            "description": "Get the current time"
        }
    ]

    # Initialize messages with a system prompt
    messages = [
        {"role": "developer", "content": "You are an AI assistant that provides information."},
    ]

    # Loop until the user types 'quit'
    while True:
        prompt = input("\nEnter a prompt (or type 'quit' to exit)\n")
        if prompt.lower() == "quit":
            break

        # Append the user prompt to the messages
        messages.append({"role": "user", "content": prompt})

        # Get initial response
        response = client.responses.create(
            model=MODEL_DEPLOYMENT,
            input=messages,
            tools=function_tools
        )

        # Append model output to the messages
        messages += response.output

        # Was there a function call?
        for item in response.output:
            if item.type == "function_call" and item.name == "get_time":
                current_time = get_time()
                messages.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": current_time
                })

                # Get a follow up response using the tool output
                response = client.responses.create(
                    model=MODEL_DEPLOYMENT,
                    instructions="Answer only with the tool output.",
                    input=messages,
                    tools=function_tools
                )

        print(response.output_text)


# Run the main function when the script starts
if __name__ == '__main__':
    main()



# How the function tool works
# The general process for using the function tool is:

# 1. You define tools - Provide one or more function definitions in the tools array.
# 2. Model evaluates the prompt - It determines whether a function call is needed.
# 3. Model emits a function call - The response includes the function name and call metadata.
# 4. Your app runs logic - Run the matching function in your code.
# 5. You return function output - Send a function_call_output item with the result.
# 6. Model completes the answer - It incorporates tool results into the final response.

# Best practices
# Keep tools focused - Small, single-purpose functions are easier to control and test
# Validate function inputs - Never trust tool arguments blindly in production systems
# Handle errors safely - Return clear error outputs the model can reason about
# Log tool usage - Track calls, latency, and failure rates for debugging and governance
# Limit sensitive operations - Require explicit authorization for high-impact actions

# Limitations to know about
# The model requests function calls, but your application must run them
# Incorrect or unexpected tool arguments can occur and should be validated
# Tool latency can increase end-to-end response time
# Function calling improves reliability, but final outputs still need review for critical decisions
# Used well, the function tool turns a model from a text generator into an orchestrator that can interact with real systems in a controlled, auditable way.