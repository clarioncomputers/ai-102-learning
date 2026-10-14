# Copilot Instructions

## Setup and validation

- Create or activate a local virtual environment, then install dependencies with:
  ```powershell
  python -m pip install -r requirements.txt
  ```
- This repository has no configured automated test suite, test runner, linter, or formatter. Validate an individual example by running it as a module from the repository root:
  ```powershell
  python -m python.chat_chatcompletions.run_model
  python -m python.chat_chatcompletions.foundry-code-example
  python -m python.chat_chatcompletions.chat_loop
  python -m python.tool_calling.using_code_interpreter_tools
  ```
- The samples use `DefaultAzureCredential`. Before running them, authenticate with an Azure identity available to that credential chain (for example, `az login` or supported VS Code/Azure CLI credentials) and ensure it can access the configured Azure AI Foundry project.
- Shared Azure AI Foundry configuration is in `python\foundry_config.py`. Override its defaults without editing source by setting `OPENAI_ENDPOINT` and `MODEL_DEPLOYMENT` in the shell that starts a sample:
  ```powershell
  $env:OPENAI_ENDPOINT = "https://<your-project>.services.ai.azure.com/openai/v1"
  $env:MODEL_DEPLOYMENT = "<your-deployment>"
  ```

## Architecture

- `python\` is a package of runnable learning samples. Its `foundry_config.py` module centralizes the Azure AI Foundry OpenAI-compatible `/openai/v1` endpoint, deployment, and passwordless client construction for every sample. Samples support both `python -m python.<category>.<module>` from the repository root and direct execution by VS Code.
- `run_model.py` demonstrates a multi-turn Responses API conversation by passing each prior response's `id` as `previous_response_id`.
- `chat_loop.py` is the interactive equivalent: it retains the preceding response object in `last_response_id` and exits only when the user enters `quit`.
- `foundry-code-example.py` is the minimal single-response example. `using_code_interpreter_tools.py` demonstrates Responses API code-interpreter usage.
- Dependencies are pinned in `requirements.txt`; `INSTRUCTIONS.md` is the generated Azure AI Foundry setup and local-run guide.

## Conventions

- Keep samples on the Responses API (`client.responses.create`) and create clients with `foundry_config.create_openai_client()`; it obtains Azure AI tokens using `get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")`. Do not introduce API keys for the existing Foundry examples.
- Keep endpoint and deployment configuration in `foundry_config.py`; use its `OPENAI_ENDPOINT` and `MODEL_DEPLOYMENT` environment variables for per-shell overrides.
- Preserve conversation state with `previous_response_id`; for interactive code, pass `None` on the first request and the immediately prior response's `id` afterward.
