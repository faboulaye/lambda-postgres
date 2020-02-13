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


# Lambda main
def lambda_handler(event, context):
    insert_data()
    rows = read_data()
    return {'statusCode': 200, 'body': rows}


def read_data():
    logger.info("Start fetching data...")
    with conn.cursor() as cursor:
        rows = []
        cursor.execute("select * from employe")
        for row in cursor:
            print(row)
            rows.append(row)
    logger.info("End")
    return rows


def insert_data():
    logger.info("Start fetching data...")
    with conn.cursor() as cursor:
        for i in range(1, 10):
            cursor.execute("INSERT INTO employe (id, name, email, department, salary) VALUES (%d, %s, %s, %s, %d)"
                           % i, "Name %d" % i, "Email %d" % i, "Department %d" % i, 2500 + (i*10))
        cursor.commit()
    logger.info("End")
