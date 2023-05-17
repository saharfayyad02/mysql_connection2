import pandas as pd
from pandas._libs.lib import _NoDefault
from sqlalchemy import create_engine

class Model:

    def createengine(conn):
        engine = create_engine(conn)
        return engine

    def send_data(engine,table_name,df):
        return df.to_sql(table_name, con=engine, if_exists='replace', index=False)

    def get_data(queries,engine):
        query=pd.read_sql_query(queries,engine, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None, dtype=None, dtype_backend=_NoDefault.no_default)
        return query