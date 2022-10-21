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
      
#snowflake related functions:
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('from streamlit')")
         return "Thanks for adding " + new_fruit
      
#Add a button to load the fruit
if streamlit.button('Get fruit load list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)
      #new section to display fruityvice api response

      
add_my_fruit = streamlit.text_input('What fruit would you like to add?')      
#Add a button to add the fruit
if streamlit.button('Add a fruit to the list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     #streamlit.dataframe(back_from_function)
     streamlit.write(back_from_function)
      

