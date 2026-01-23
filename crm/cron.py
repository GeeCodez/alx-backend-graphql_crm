from datetime import datetime
import requests

def log_crm_heartbeat():
    """Log a heartbeat message indicating the CRM system is active."""
    timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("tmp/crm_heartbeat.log", "a") as log_file:
        log_file.write(f"{timestamp} CRM is alive\n")

    try:
        response= requests.post(
            'http://localhost:8000/graphql/',
            json={'query': '{ hello }'},
            timeout=5
        )
        if response.status_code == 200:
            print(f"{timestamp} CRM heartbeat check successful.")
        else:
            print(f"{timestamp} CRM endpoint returned {response.status_code}.")
    except Exception as e:
        print(f"{timestamp} Error pinging GraphQL: {e}")