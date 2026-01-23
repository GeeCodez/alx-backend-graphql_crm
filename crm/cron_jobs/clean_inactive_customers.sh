#!/bin/bash

cd /home/gee/alx-backend-graphql_crm/

source venv/bin/activate

#running django shell
python manage.py shell <<END
from crm.models import Customer
from datetime import timedelta
from django.utils import timezone

#calculating one_year_ago
one_year_ago = timezone.now() - timedelta(days=365)

# Get inactive customers
inactive_customers = Customer.objects.filter(order__order_date__lt=one_year_ago).distinct()

# Count and delete
count = inactive_customers.count()
inactive_customers.delete()

# Log deletion
with open("/tmp/customer_cleanup_log.txt", "a") as f:
    f.write(f"{timezone.now()}: Deleted {count} inactive customers\n")
END
