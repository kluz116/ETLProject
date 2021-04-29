from DataConnections.source_database_con import cnxn
from etl_config import Core

try:
    obj = Core()
    obj.read_from_Transactions(cnxn)
except Exception as e:
    print(e)
