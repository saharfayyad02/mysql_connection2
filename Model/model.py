import json
import pandas as pd
from pandas._libs.lib import _NoDefault
from sqlalchemy import create_engine


class Model:

    def createengine(conn):
        engine = create_engine(conn)
        return engine


class SalesReciepts:

    def __init__(self,transaction_id,transaction_date,transaction_time,sales_outlet_id,promo_item_yn
    ,unit_price,line_item_amount,quantity,product_id,line_item_id,instore_yn,Ord_er,customer_id,staff_id):
        self.transaction_id=transaction_id
        self.transaction_date=transaction_date
        self.transaction_time=transaction_time
        self.transaction_id=transaction_id
        self.sales_outlet_id=sales_outlet_id
        self.promo_item_yn=promo_item_yn
        self.unit_price=unit_price
        self.line_item_amount=line_item_amount
        self.quantity=quantity
        self.product_id=product_id
        self.line_item_id=line_item_id
        self.instore_yn=instore_yn
        self.Ord_er=Ord_er
        self.customer_id=customer_id
        self.staff_id=staff_id



class Customer:
    def __init__(self,customer_id,home_store,customer_first_name,customer_email,customer_since
                 ,loyalty_card_number,birthdate,gender,birth_year):
        self.customer_id=customer_id
        self.home_store=home_store
        self.customer_first_name=customer_first_name
        self.customer_email=customer_email
        self.customer_since=customer_since
        self.loyalty_card_number=loyalty_card_number
        self.birthdate=birthdate
        self.gender=gender
        self.birth_year=birth_year


    def getCustomer(engine):

        # best_performing_query=SqlQueries.best_performing_query(best_performing='')
        # best_performingquery = pd.read_sql_query(best_performing_query, engine, index_col=None, coerce_float=True, params=None, parse_dates=None,
        #                           chunksize=None, dtype=None, dtype_backend=_NoDefault.no_default)
        # query = best_performingquery.to_dict(orient='records')
        # print(json.dumps(query, indent=4))
        #
        #
        # peak_hour_query = SqlQueries.peak_hour_query(peak_hour='')
        # query_peakhour = pd.read_sql_query(peak_hour_query, engine, index_col=None, coerce_float=True, params=None, parse_dates=None,
        #                           chunksize=None, dtype=None, dtype_backend=_NoDefault.no_default)
        # query_peak_hour = query_peakhour.to_dict(orient='records')
        # print(json.dumps(query_peak_hour, indent=4))
        #
        #
        # best_performing_query = SqlQueries.best_performing_query(best_performing='')
        # best_performingquery = pd.read_sql_query(best_performing_query, engine, index_col=None, coerce_float=True, params=None,
        #                                    parse_dates=None,
        #                                    chunksize=None, dtype=None, dtype_backend=_NoDefault.no_default)
        # best_performingquery = best_performingquery.to_dict(orient='records')
        # print(json.dumps(best_performingquery, indent=4))

        with open('C:\\Users\\user\\PycharmProjects\\mysql_connection2\\SqlQueries\\peak_hour.sql', 'r') as sql_file:
            peah_hour_query = sql_file.read()
        peak_hour = pd.read_sql_query(peah_hour_query, engine, index_col=None, coerce_float=True,
                                                 params=None,parse_dates=None,chunksize=None, dtype=None, dtype_backend=_NoDefault.no_default)

        peakhour = peak_hour.head().to_dict(orient='records')
        print(json.dumps(peakhour, indent=4))


        with open('C:\\Users\\user\\PycharmProjects\\mysql_connection2\\SqlQueries\\best_store.sql', 'r') as sql_file:
            best_store = sql_file.read()

        store = pd.read_sql_query(best_store, engine, index_col=None, coerce_float=True,
                                      params=None, parse_dates=None, chunksize=None, dtype=None,
                                      dtype_backend=_NoDefault.no_default)

        beststore = store.to_dict(orient='records')
        print(json.dumps(beststore, indent=4))


        with open('C:\\Users\\user\\PycharmProjects\\mysql_connection2\\SqlQueries\\performing.sql', 'r') as sql_file:
            best_performing_weekandmonth_of_the_year = sql_file.read()

        best_performint_weekmonth_of_the_year = pd.read_sql_query(best_performing_weekandmonth_of_the_year, engine, index_col=None, coerce_float=True,
                                      params=None, parse_dates=None, chunksize=None, dtype=None,
                                      dtype_backend=_NoDefault.no_default)

        best_performing = best_performint_weekmonth_of_the_year.head().to_dict(orient='records')
        print(json.dumps(best_performing, indent=4))

        new_customer = Customer





