import streamlit
import pandas
import requests

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
streamlit.header('Fruitvice Fruit Advice!')

#new section to display fruityvice api response
fruit_choice = streamlit.text_input('What fruit would you like to information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

#old -- fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#take the json version of the response and normalized it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it in the screen as a table
streamlit.dataframe(fruityvice_normalized)


