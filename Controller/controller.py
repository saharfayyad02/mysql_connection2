import pandas as pd
from model.model import Model
from View.view import Viewdata


class Conttroller(Model,Viewdata):
    def req(file):
        df = pd.read_csv(file)
        return df

    def send_data(engine,table_name,df):
        return Model.send_data(engine,table_name,df)

    def get_data(queries,engine):
        query=Model.get_data(queries,engine)
        return query

    def viewdata(data):
        data = Viewdata.viewdata(data)
        return data



