## CRM Reports with Celery

### Setup
1. Install Redis
2. pip install -r requirements.txt
3. python manage.py migrate

### Run services
- redis-server
- celery -A crm worker -l info
- celery -A crm beat -l info

### Logs
Check /tmp/crm_report_log.txt
