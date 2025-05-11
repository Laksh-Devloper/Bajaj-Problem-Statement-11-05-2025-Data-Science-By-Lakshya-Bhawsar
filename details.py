import requests

url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

data = {
    "name": "Lakshya Bhawsar",
    "regNo": "908",  
    "email": "lakshyabhawsar231094@acropolis.in"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    response_data = response.json()
    webhook_url = response_data.get("webhook")
    access_token = response_data.get("accessToken")
    print(f"Webhook URL: {webhook_url}")
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}")
