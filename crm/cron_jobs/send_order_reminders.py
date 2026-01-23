from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import timedelta
from django.utils import timezone  # if using timezone aware datetimes
import logging

# 1. Calculate start date
seven_days_ago = timezone.now() - timedelta(days=7)

# 2. Set up transport and client
transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=True,
    retries=3,
)
client = Client(transport=transport, fetch_schema_from_transport=True)

# 3. Define query with variable
query = gql("""
query getRecentOrders($startDate: DateTime!) {
  allOrders(orderDateGte: $startDate) {
    edges {
      node {
        id
        customer {
          email
        }
      }
    }
  }
}
""")

variables = {"startDate": seven_days_ago.isoformat()}

# 4. Execute query
result = client.execute(query, variable_values=variables)

# 5. Loop and log
with open("/tmp/order_reminders_log.txt", "a") as f:
    for edge in result["allOrders"]["edges"]:
        order_id = edge["node"]["id"]
        email = edge["node"]["customer"]["email"]
        f.write(f"{timezone.now()}: Order {order_id}, Customer {email}\n")

print("Order reminders processed!")
