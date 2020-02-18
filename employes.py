import os
import sys
import psycopg2
import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# rds settings
session = boto3.session.Session()
client = session.client(service_name='secretsmanager')
rds_secret_cred = client.get_secret_value(
    SecretId=os.getenv('RDS_SECRET_DB_CREDENTIALS', 'test'))
json_secret_string = json.loads(rds_secret_cred['SecretString'])
rds_host = json_secret_string['host']
rds_username = json_secret_string['username']
rds_pwd = json_secret_string['password']
rds_db_name = json_secret_string['dbname']


# Connect to the RDS instance
logger.info("Connecting to RDS Postgres database")
try:
    conn_string = "host=%s user=%s password=%s dbname=%s" % (
        rds_host, rds_username, "postgres", rds_db_name)
    conn = psycopg2.connect(conn_string)
except:
    logger.error("ERROR: Could not connect to Postgres instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS Postgres instance succeeded")


# Lambda - Employes
def handler(event, context):
    with conn.cursor() as cursor:
        with open('employe-table.sql', 'r') as script:
            cursor.execute(script.read())
        cursor.execute("SELECT * FROM employe")
        rows = cursor.fetchall()
    return {'statusCode': 200, 'body': json.dumps(rows)}
