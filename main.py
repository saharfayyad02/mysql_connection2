import pandas as pd
from sqlalchemy import create_engine ,Column, Integer, String,ForeignKey,CHAR
from Controller.controller import Conttroller
from Model.model import Customer ,SalesReciepts
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from prefect import flow,task
from pandas._libs.lib import _NoDefault


def request(file):
    req = Conttroller.req(file)
    return req


def send_data_tosql(engine, table_name, df):
    data = Conttroller.send_data(engine, table_name, df)
    return data

#
# def get_queries(queries, engine):
#     query = Conttroller.get_data(queries, engine)
#     return query
#
#
# def viewdata(data):
#     data = Conttroller.viewdata(data)
#     return data
@task
def extract_data():
    engine = create_engine('mysql+mysqlconnector://root:sahar2001@localhost:3306/sys2')
    sales_re_table=pd.read_sql_table('sales_re', engine, schema=None, index_col=None, coerce_float=True, parse_dates=None, columns=None, chunksize=None, dtype_backend=_NoDefault.no_default)
    product_table=pd.read_sql_table('product', engine, schema=None, index_col=None, coerce_float=True, parse_dates=None, columns=None, chunksize=None, dtype_backend=_NoDefault.no_default)

    #print(sales_re_table)
    sales_re_table2=sales_re_table[["unit_price", "product_id", "transaction_id"]]
    product_table2=product_table[["product_id","product"]]

    mearged_table = pd.merge(sales_re_table2, product_table2, on='product_id', how='right')

   # print(mearged_table)
    unit_price_sum = mearged_table.iloc[:,[0]].sum()
    total_items = mearged_table.iloc[:,[3]].count()
    transcation_count = mearged_table.iloc[:,[2]].count()

    #print(unit_price_sum)
    #print(total_items)
    #print(transcation_count)

    return [unit_price_sum,total_items,transcation_count,engine]

@task
def transformation(num1,num2,name):
    return pd.DataFrame({name: [num1/num2]})

@task
def load(engine,table_name,df):
    return df.to_sql(table_name, con=engine, if_exists='replace', index=False)

@flow
def common_flow(config: dict):
    list = extract_data()
    Spending_per_receipt = transformation(list[0].iloc[0], list[2].iloc[0],'Spending_per_receipt')
    Items_per_receipt = transformation(list[1].iloc[0], list[2].iloc[0],'Items_per_receipt')
    print(Spending_per_receipt)
    print(Items_per_receipt)

    engine = list[3]

    load(engine, 'spending_perreceipt', Spending_per_receipt)
    load(engine, 'items_perreceipt', Items_per_receipt)

@flow
def main_flow():
    data = common_flow(config={})

if __name__ == '__main__':
    main_flow()

 #   en=extract_data()
    # sales_re = request('C:\\Users\\user\\Desktop\\april\\sales.csv')
    # customer = request('C:\\Users\\user\\Desktop\\april\\customer.csv')
    # product = request('C:\\Users\\user\\Desktop\\april\\product.csv')
    # sales = request('C:\\Users\\user\\Desktop\\april\\sales_outlet.csv')
    # date = request('C:\\Users\\user\\Desktop\\april\\Dates.csv')
    # generations = request('C:\\Users\\user\\Desktop\\april\\generations.csv')
    # pastry_inventory= request('C:\\Users\\user\\Desktop\\april\\pastry inventory.csv')
    # sales_targets= request('C:\\Users\\user\\Desktop\\april\\sales targets.csv')
    # staff=request('C:\\Users\\user\\Desktop\\april\\staff.csv')

    # Session = sessionmaker(bind=engine)
    # session = Session()

    # send_data_tosql(engine, 'sales_re', sales_re)
    # send_data_tosql(engine, 'customer', customer)
    # send_data_tosql(engine, 'product', product)
    # send_data_tosql(engine, 'sales_outlet', sales)
    # send_data_tosql(engine, 'date', date)
    # send_data_tosql(engine, 'generations', generations)
    # send_data_tosql(engine, 'pastry_inventory', pastry_inventory)
    # send_data_tosql(engine, 'sales_targets', sales_targets)
    # send_data_tosql(engine, 'staff', staff)


    #engine.dispose()

    # employees = session.query(SalesReciepts).filter(SalesReciepts.sales_outlet_id == 3).all()
    #
    # for employee in employees:
    #     employee_data = {
    #         'transaction_id': employee.transaction_id,
    #         'transaction_date': employee.transaction_date,
    #         'transaction_time': employee.transaction_time,
    #     }
    #     print(json.dumps(employee_data, indent=4))

