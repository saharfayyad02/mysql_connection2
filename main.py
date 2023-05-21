from sqlalchemy import create_engine
from Controller.controller import Conttroller
from Model.model import Customer


def request(file):
       req = Conttroller.req(file)
       return req

def send_data_tosql(engine,table_name,df):
    data=Conttroller.send_data(engine,table_name,df)
    return data

def get_queries(queries,engine):
    query = Conttroller.get_data(queries,engine)
    return query

def viewdata(data):
    data =Conttroller.viewdata(data)
    return data

if __name__ == '__main__':
    recipit_sales = request('C:\\Users\\user\\Desktop\\april\\201904 sales reciepts.csv')
    customer=request('C:\\Users\\user\\Desktop\\april\\customer.csv')
    product=request('C:\\Users\\user\\Desktop\\april\\product.csv')
    sales=request('C:\\Users\\user\\Desktop\\april\\sales_outlet.csv')
    date=request('C:\\Users\\user\\Desktop\\april\\Dates.csv')


    engine = create_engine('mysql+mysqlconnector://root:sahar2001@localhost:3306/sys')


    send_data_tosql(engine,'sales_reciepts',recipit_sales)
    send_data_tosql(engine,'customer',customer)
    send_data_tosql(engine,'product',product)
    send_data_tosql(engine,'sales_outlet',sales)
    send_data_tosql(engine,'date',date)
    engine.dispose()

    Customer.getCustomer(engine)

    #
    # most_selling_item_query="""select s.sales_outlet_id,sum(s.order) as sums from sales_reciepts s where(select s2.sales_outlet_id from sales_outlet s2
    # where s.sales_outlet_id = s2.sales_outlet_id
    # )GROUP BY sales_outlet_id
    # ORDER BY sum(s.order) DESC
    # LIMIT 1
    # ;"""
    #
    # peak_hour_query = """
    #  SELECT s.sales_outlet_id, s.transaction_time, MAX(s.order) AS max_order
    #  FROM sales_reciepts s
    #  where (select s2.sales_outlet_id from sales_outlet s2
    #  where s.sales_outlet_id = s2.sales_outlet_id
    #  )
    #  GROUP BY s.sales_outlet_id,s.transaction_time
    #  ORDER BY max_order DESC;"""
    #
    # best_performing_query = """
    #  select s.sales_outlet_id,month(s.transaction_date) as month,max(s.order) from sales_reciepts s
    #  where(select s2.sales_outlet_id from sales_outlet s2
    #  where s.sales_outlet_id = s2.sales_outlet_id )
    #  GROUP BY s.sales_outlet_id ,month(s.transaction_date)
    #  ORDER BY max(s.order)  DESC;"""
    #
    # most_selling_item=get_queries(most_selling_item_query,engine)
    # #viewdata(most_selling_item)
    #
    # peak_hour = get_queries(peak_hour_query,engine)
    # #viewdata(peak_hour)
    #
    # best_performing = get_queries(best_performing_query,engine)
    # Customer.getCustomer(engine)
    #
    #
    # #viewdata(best_performing)
    #
    #
    #
    #
