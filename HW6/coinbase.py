import json

import requests
from datetime import datetime
import psycopg2



def generate_insert_sql(jsonBtc:dict):
    # Получение аргумента 'of' из контекста

    # Specify the table name
    table_name = 'exchange_rates'
    # Specify the column names of the table
    column_names = ('id', 'name', 'rateUsd', 'trDate')
    # Create the string of column names
    columns_str =', '.join(str(name) for name in column_names)
    insert_queries = []
    # Generate values for each column
    # Create a list of values
    values = ["'"+jsonBtc['id']+"'","'"+ jsonBtc['name']+"'", jsonBtc['rateUsd'], "'"+jsonBtc['trDate']+"'"]
    # Create a string of values
    values_str = ', '.join(str(value) for value in values)
    # Create and append the DML query
    insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});"
    print(insert_query)  # Print to console for debugging
    return insert_query


def write_to_postgres(sql:str):
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


url = 'http://api.coincap.io/v2/rates/bitcoin'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
responses = requests.request("GET", url, headers=headers, data={})
myjson = responses.json()
ourdata = []
listing_dict = dict(id=myjson['data']['symbol'], name=myjson['data']['id'], rateUsd=myjson['data']['rateUsd'], trDate=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print(json.dumps(listing_dict))

print('done')
sql = generate_insert_sql(listing_dict)
print(sql)
write_to_postgres(sql)

