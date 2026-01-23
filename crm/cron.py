from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_file = "/tmp/crm_heartbeat_log.txt"

    try:
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=True,
            retries=3,
        )

        client = Client(transport=transport, fetch_schema_from_transport=True)

        query = gql("""
        query {
            hello
        }
        """)

        client.execute(query)

        with open(log_file, "a") as f:
            f.write(f"{timestamp} [INFO] CRM is alive\n")

        print(f"{timestamp} [INFO] CRM heartbeat logged successfully")

    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"{timestamp} [ERROR] Heartbeat failed: {e}\n")

        print(f"{timestamp} [ERROR] Heartbeat failed: {e}")
