# VS Code for the Web - Azure AI Foundry

We've generated a simple development environment for you to play with sample code to create and run the agent that you built in the Azure AI Foundry playground.

The Azure AI Foundry extension provides tools to help you build, test, and deploy AI models and AI Applications directly from VS Code. It offers simplified operations for interacting with your models, agents, and threads without leaving your development environment. Click on the Azure AI Foundry Icon on the left to see more.

Follow the instructions below to get started!

## Open the terminal

python.exe -m pip install --upgrade pip

python -m pip install -r requirements.txt  

For codespaces use:

# azure login
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login --use-device-code

# install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login --use-device-code

# run the python file to see all working okay (bash).
python python/run_model.py


Press ``Ctrl-` `` &nbsp; to open a ter

## Run your model locally

To run the model that you deployed in AI Foundry, and view the output in the terminal run the following command:

```bash
python -m python.chat_chatcompletions.run_model
```



## Continuing on your local desktop

You can keep working locally on VS Code Desktop by clicking "Continue On Desktop..." at the bottom left of this screen. Be sure to take the .env file with you using these steps:

- Right-click the .env file
- Select "Download"
- Move the file from your Downloads folder to the local git repo directory
- For Windows, you will need to rename the file back to .env using right-click "Rename..."
