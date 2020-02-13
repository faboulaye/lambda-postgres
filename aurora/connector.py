import boto3
import json
import os
import time

# Update these 3 parameters for your environment
database_name = 'ec2_inventory_db'
db_cluster_arn = 'arn:aws:rds:us-east-1:123456789012:cluster:dev-aurora-ec2-inventory-cluster'
db_credentials_secrets_store_arn = 'arn:aws:secretsmanager:us-east-1:123456789012:secret:dev-AuroraUserSecret-DhpkOI'

# This is the Data API client that will be used in our examples below
rds_client = boto3.client('rds-data')


# Lambda main
def lambda_handler(event, context):
    create_table()
    insert_data()
    rows = read_data()
    return {'statusCode': 200, 'body': rows}


# Timing function executions
def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print(f'Function: {f.__name__}')
        print(f'*  args: {args}')
        print(f'*  kw: {kw}')
        print(f'*  execution time: {(te-ts)*1000:8.2f} ms')
        return result
    return timed


def create_table():
    print("Hello world")


def insert_data():
    print("Hello world")


def read_data():
    print("Hello world")
    return []


def execute_statement(sql, sql_parameters=[]):
    response = rds_client.execute_statement(
        secretArn=db_credentials_secrets_store_arn,
        database=database_name,
        resourceArn=db_cluster_arn,
        sql=sql,
        parameters=sql_parameters
    )
    return response
