import streamlit
import pandas

streamlit.title('My Mom\'s New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.write('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.write('🥤 Kale, Spinach & Rocket Smoothie')
streamlit.write('🥚 Hard-boiled Free-Range Egg')
streamlit.write('🥑 Avocado Toast')
streamlit.header('🍓🍊Build Your Own Fruit Smoothie🍉🍌')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Apple','Banana'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
##streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
