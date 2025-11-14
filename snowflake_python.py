from snowflake.snowpark.session import Session
from snowflake.snowpark.types import IntegerType, FloatType
from snowflake.snowpark.functions import avg, sum, col, udf, call_udf, call_builtin, year, month
import pandas as pd
from snowflake.snowpark.functions import col
from datetime import datetime
print("\n\t Start Time:",datetime.now().strftime("%H:%M:%S.%f"))
# Session
connection_parameters = {
    "account": "np89695.ap-southeast-1",
    "user": "Kumar1240",
    "password": "Kusuma@1246"
      }

session = Session.builder.configs(connection_parameters).create()
# test if we have a connectiondd
#session.sql("select current_account() acct, current_warehouse() wh, current_database() db, current_schema() schema, current_version() version").show()

session.close()