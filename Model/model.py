import json
import pandas as pd
from pandas._libs.lib import _NoDefault
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine ,Column, Integer, String,ForeignKey,CHAR



class Model:

    def createengine(conn):
        engine = create_engine(conn)
        return engine

Base = declarative_base()

class SalesReciepts(Base):
    __tablename__ = 'sales_re'

    transaction_id = Column("transaction_id",Integer,primary_key=True)
    transaction_date = Column("transaction_date",Integer)
    transaction_time = Column("transaction_time",Integer)
    sales_outlet_id = Column("sales_outlet_id",Integer)
    promo_item_yn = Column("promo_item_yn",String)
    line_item_amount = Column("line_item_amount",Integer)
    quantity = Column("quantity",Integer)
    product_id = Column("product_id",Integer)
    line_item_id = Column("line_item_id",Integer)
    instore_yn = Column("instore_yn",String)
    Ord_er = Column("order",Integer)
    customer_id = Column("customer_id",Integer)
    staff_id = Column("staff_id",Integer)
    unit_price= Column("unit_price",Integer)


    def __init__(self, transaction_id, transaction_date, transaction_time, sales_outlet_id, promo_item_yn
                 , unit_price, line_item_amount, quantity, product_id, line_item_id, instore_yn, Ord_er, customer_id,
                 staff_id):
        self.transaction_id = transaction_id
        self.transaction_date = transaction_date
        self.transaction_time = transaction_time
        self.transaction_id = transaction_id
        self.sales_outlet_id = sales_outlet_id
        self.promo_item_yn = promo_item_yn
        self.unit_price = unit_price
        self.line_item_amount = line_item_amount
        self.quantity = quantity
        self.product_id = product_id
        self.line_item_id = line_item_id
        self.instore_yn = instore_yn
        self.Ord_er = Ord_er
        self.customer_id = customer_id
        self.staff_id = staff_id


class Customer:
    def __init__(self, customer_id, home_store, customer_first_name, customer_email, customer_since
                 , loyalty_card_number, birthdate, gender, birth_year):
        self.customer_id = customer_id
        self.home_store = home_store
        self.customer_first_name = customer_first_name
        self.customer_email = customer_email
        self.customer_since = customer_since
        self.loyalty_card_number = loyalty_card_number
        self.birthdate = birthdate
        self.gender = gender
        self.birth_year = birth_year

    def getCustomer(engine):

        with open('C:\\Users\\user\\PycharmProjects\\mysql_connection2\\SqlQueries\\peak_hour.sql', 'r') as sql_file:
            peah_hour_query = sql_file.read()
        peak_hour = pd.read_sql_query(peah_hour_query, engine, index_col=None, coerce_float=True,
                                      params=None, parse_dates=None, chunksize=None, dtype=None,
                                      dtype_backend=_NoDefault.no_default)

        # peakhour = peak_hour..to_dict(orient='records')
        peak_hour.to_excel('result.xlsx')
       # print(json.dumps(peakhour, indent=4))
        print(peak_hour)

        with open('C:\\Users\\user\\PycharmProjects\\mysql_connection2\\SqlQueries\\best_store.sql', 'r') as sql_file:
            best_store = sql_file.read()

        store = pd.read_sql_query(best_store, engine, index_col=None, coerce_float=True,
                                  params=None, parse_dates=None, chunksize=None, dtype=None,
                                  dtype_backend=_NoDefault.no_default)

        beststore = store.to_dict(orient='records')
        #print(json.dumps(beststore, indent=4))

        with open('C:\\Users\\user\\PycharmProjects\\mysql_connection2\\SqlQueries\\performing.sql', 'r') as sql_file:
            best_performing_weekandmonth_of_the_year = sql_file.read()

        best_performint_weekmonth_of_the_year = pd.read_sql_query(best_performing_weekandmonth_of_the_year, engine,
                                                                  index_col=None, coerce_float=True,
                                                                  params=None, parse_dates=None, chunksize=None,
                                                                  dtype=None,
                                                                  dtype_backend=_NoDefault.no_default)

        best_performing = best_performint_weekmonth_of_the_year.head().to_dict(orient='records')
        #print(json.dumps(best_performing, indent=4))

