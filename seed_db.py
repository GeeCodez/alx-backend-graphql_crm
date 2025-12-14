import os
import django
from decimal import Decimal

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_backend_graphql.settings")
django.setup()

from crm.models import Customer, Product, Order

# --- Seed Customers ---
customers_data = [
    {"name": "Alice Johnson", "email": "alice@example.com", "phone": "1234567890"},
    {"name": "Bob Smith", "email": "bob@example.com", "phone": "2345678901"},
    {"name": "Charlie Brown", "email": "charlie@example.com", "phone": "3456789012"},
]

customers = []
for data in customers_data:
    customer, created = Customer.objects.get_or_create(**data)
    customers.append(customer)

# --- Seed Products ---
products_data = [
    {"name": "Laptop", "price": Decimal("1200.00")},
    {"name": "Smartphone", "price": Decimal("800.00")},
    {"name": "Headphones", "price": Decimal("150.00")},
]

products = []
for data in products_data:
    product, created = Product.objects.get_or_create(**data)
    products.append(product)

# --- Seed Orders ---
orders_data = [
    {"customer": customers[0], "product": products[0], "quantity": 1},
    {"customer": customers[1], "product": products[1], "quantity": 2},
    {"customer": customers[2], "product": products[2], "quantity": 3},
]

for data in orders_data:
    total_amount = data["quantity"] * data["product"].price
    order = Order(
        customer=data["customer"],
        product=data["product"],
        quantity=data["quantity"],
        total_amount=total_amount  # Ensure NOT NULL constraint is satisfied
    )
    order.save()

print("Database seeding completed successfully!")
