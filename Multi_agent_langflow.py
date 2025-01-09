from dotenv import load_dotenv
import requests
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "095ad790-6809-4b6b-80d6-116c572c64cd"
FLOW_ID = "78b09d89-9887-42aa-8435-dfa2d6369ec0"
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")
ENDPOINT = "MultiAI_endpoint"

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()