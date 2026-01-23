from celery import shared_task
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime
import requests

@shared_task
def generate_crm_report():
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True,
        retries=3,
    )

    client = Client(
        transport=transport,
        fetch_schema_from_transport=False,
    )

    query = gql("""
        query {
            crmReport {
                totalCustomers
                totalOrders
                totalRevenue
            }
        }
    """)

    result = client.execute(query)["crmReport"]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(
            f"{timestamp} - Report: "
            f"{result['totalCustomers']} customers, "
            f"{result['totalOrders']} orders, "
            f"{result['totalRevenue']} revenue\n"
        )
