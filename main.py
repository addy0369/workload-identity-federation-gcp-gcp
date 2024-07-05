import os
from google.cloud import bigquery

def main(request):
   client = bigquery.Client()

    # Perform a query.
    QUERY = (
      'SELECT * FROM 'playground-piotr-7t2f6.audit_logs_play.cloudaudit_googleapis_com_activity_20240705'
      'LIMIT 100')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    for row in rows:
      print(row.name)
