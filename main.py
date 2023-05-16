import pandas as pd
from sqlalchemy import create_engine
import mysql.connector


df = pd.read_csv('C:\\Users\\user\\Desktop\\april\\201904 sales reciepts.csv')
df_customer = pd.read_csv('C:\\Users\\user\\Desktop\\april\\customer.csv')
df_product = pd.read_csv('C:\\Users\\user\\Desktop\\april\\product.csv')
df_sales = pd.read_csv('C:\\Users\\user\\Desktop\\april\\sales_outlet.csv')


engine = create_engine('mysql+mysqlconnector://root:sahar2001@localhost:3306/sys')

table_name = 'sales_reciepts'
df.to_sql(table_name, con=engine, if_exists='replace', index=False)
df_customer.to_sql('customer', con=engine, if_exists='replace', index=False)
df_product.to_sql('product', con=engine, if_exists='replace', index=False)
df_sales.to_sql('sales_outlet', con=engine, if_exists='replace', index=False)

engine.dispose()


mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="sahar2001",
    port= "3306",
    database="sys",
)


mycursor = mydb.cursor()
the_query="""select s.sales_outlet_id,sum(s.order) as sums from sales_reciepts s where(select s2.sales_outlet_id from sales_outlet s2 
where s.sales_outlet_id = s2.sales_outlet_id 
)GROUP BY sales_outlet_id 
ORDER BY sum(s.order) DESC
LIMIT 1  
;"""

mycursor.execute(the_query)
users = mycursor.fetchall()
for i in users:
    print(i)


the_query2="""
SELECT s.sales_outlet_id, s.transaction_time, MAX(s.order) AS max_order
FROM sales_reciepts s 
where (select s2.sales_outlet_id from sales_outlet s2 
where s.sales_outlet_id = s2.sales_outlet_id 
)
GROUP BY s.sales_outlet_id,s.transaction_time
ORDER BY max_order DESC
LIMIT 0, 1000;"""


mycursor.execute(the_query2)
users2 = mycursor.fetchall()
for i in users2:
    print(i)

