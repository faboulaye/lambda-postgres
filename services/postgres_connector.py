import os
import sys
import psycopg2
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# rds settings
rds_host = os.getenv('RDS_HOST', 'localhost')
rds_username = os.getenv('RDS_USER', 'postgres')
rds_user_pwd = os.getenv('RDS_PWD', 'admin')
rds_db_name = os.getenv('RDS_DB', 'rds')

logger.info("Host: %s", rds_host)
logger.info("User: %s", rds_username)
logger.info("DB: %s", rds_db_name)
try:
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
        (rds_host, rds_username, rds_user_pwd, rds_db_name)
    conn = psycopg2.connect(conn_string)
except:
    logger.error("ERROR: Could not connect to Postgres instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS Postgres instance succeeded")


def lambda_handler(event, context):
    with conn.cursor() as cursor:
        rows = []
        cursor.execute("select * from employe")
        for row in cursor:
            print(row)
            rows.append(row)

        return {'statusCode': 200, 'body': rows}
