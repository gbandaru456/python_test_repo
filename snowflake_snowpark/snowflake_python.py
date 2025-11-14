from snowflake.snowpark.session import Session
from snowflake.snowpark.types import IntegerType, FloatType
from snowflake.snowpark.functions import avg, sum, col, udf, call_udf, call_builtin, year, month
import pandas as pd
from snowflake.snowpark.functions import col
from datetime import datetime
import json
print("\n\t Start Time:",datetime.now().strftime("%H:%M:%S.%f"))
cred_file='./snowflake_snowpark/creds.json'
# Session
with open(cred_file) as f:
    data = json.load(f)
    SF_ACCOUNT = data['account']
    USERNAME = data['user']
    PASSWORD = data['password']   
connection_parameters = {
    "account": SF_ACCOUNT,
    "user": USERNAME,
    "password": PASSWORD
      }

session = Session.builder.configs(connection_parameters).create()
# test if we have a connectiondd
#session.sql("select current_account() acct, current_warehouse() wh, current_database() db, current_schema() schema, current_version() version").show()

session.close()