import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Menu')

streamlit.text(' 🥣 Omega 3 & Bluebetty Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#lets put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#displays fruityvice api response
#new section to display fruityvice api response
streamlit.header('Fruitvice Fruit Advice!')

#snowflake related functions:
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM fruit_load_list")
         return my_cur.fetchall()
      
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list ('from streamlit')")
         return "Thanks for adding " + new_fruit

#Add a button to load the fruit
if streamlit.button('Get fruit load list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)
      
      
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT * FROM fruit_load_list")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from snowflake")
#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

#new section to display fruityvice api response
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('The user entered', add_my_fruit)

#Add a button to add the fruit
if streamlit.button('Add a fruit to the list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     streamlit.dataframe(back_from_function)
      
#create a repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information")
  else:
    ##streamlit.write('The user entered', fruit_choice)
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #old -- fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
    #take the json version of the response and normalized it
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    #output it in the screen as a table
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
except URLError as e:
  streamlit.error()
