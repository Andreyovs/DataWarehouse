from __future__ import annotations

# [START tutorial]
# [START import_module]
import json
import pendulum
from datetime import datetime
from datetime import date
import requests
import psycopg2
from airflow.decorators import dag, task


# [END import_module]


# [START instantiate_dag]
@dag(
    schedule=None,
    start_date=pendulum.today(),
    catchup=False,
    tags=["my_Dag"],
)
def taskflow_btc():
    """
    Transfer data from 'http://api.coincap.io/v2/rates/bitcoin' to postgresql
    """

    # [END instantiate_dag]

    def generate_insert_sql(jsonBtc: dict):
        # Получение аргумента 'of' из контекста

        # Specify the table name
        table_name = 'exchange_rates'
        # Specify the column names of the table
        column_names = ('id', 'name', 'rateUsd', 'trDate')
        # Create the string of column names
        columns_str = ', '.join(str(name) for name in column_names)
        insert_queries = []
        # Generate values for each column
        # Create a list of values
        values = ["'" + jsonBtc['id'] + "'", "'" + jsonBtc['name'] + "'", jsonBtc['rateUsd'],
                  "'" + jsonBtc['trDate'] + "'"]
        # Create a string of values
        values_str = ', '.join(str(value) for value in values)
        # Create and append the DML query
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});"
        print(insert_query)  # Print to console for debugging
        return insert_query

    def write_to_postgres(sql: str):
        connection_string = 'postgres://admin:Passw0rd@localhost/analytics'
        conn = psycopg2.connect(connection_string)
        # Create a cursor object
        cur = conn.cursor()
        # Execute the SQL query
        cur.execute(sql)

        # Commit the changes to the database
        conn.commit()
        # Close the cursor and connection
        cur.close()
        conn.close()

    # [START extract]
    @task()
    def extract():
        """
        #### Extract task
        """
        url = 'http://api.coincap.io/v2/rates/bitcoin'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        responses = requests.request("GET", url, headers=headers, data={})
        btc_rate_json = responses.json()
        print('Extract done')

        return btc_rate_json

    # [END extract]

    # [START transform]
    @task(multiple_outputs=True)
    def transform(btc_rate_json: json):
        """
        #### Transform task
        Transforms JSON
        """
        listing_dict = dict(id=btc_rate_json['data']['symbol'], name=btc_rate_json['data']['id'],
                            rateUsd=btc_rate_json['data']['rateUsd'],
                            trDate=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        return listing_dict

    # [END transform]
    # [START load]
    @task()
    def load(btc_rate_json: dict):
        """
        #### Load task
        A simple task loading JSON to PostgreSQL
        """
        sql = generate_insert_sql(btc_rate_json)
        write_to_postgres(sql)

    # [END load]

    # [START main_flow]
    btc = extract()
    btc_trm = transform(btc)
    load(btc_trm)
    # [END main_flow]


# [START dag_invocation]
taskflow_btc()
# [END dag_invocation]

# [END tutorial]
