import pandas as pd
from model.model import Model
from View.view import Viewdata
from pandas._libs.lib import _NoDefault


class Conttroller(Model,Viewdata):
    def req(file):
        df = pd.read_csv(file)
        return df

    def send_data(engine, table_name, df):
        return df.to_sql(table_name, con=engine, if_exists='replace', index=False)

    def get_data(queries, engine):
        query = pd.read_sql_query(queries, engine, index_col=None, coerce_float=True, params=None, parse_dates=None,
                                  chunksize=None, dtype=None, dtype_backend=_NoDefault.no_default)
        return query

    def viewdata(data):
        data = Viewdata.viewdata(data)
        return data



