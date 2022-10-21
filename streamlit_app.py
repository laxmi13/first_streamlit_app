import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's New Healthy Diner")

#displays fruityvice api response
#new section to display fruityvice api response
streamlit.header('Fruitvice Fruit Advice!')

#snowflake related functions:
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM fruit_load_list")
         return my_cur.fetchall()
      
#Add a button to load the fruit
if streamlit.button('Get fruit load list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)
      
      

