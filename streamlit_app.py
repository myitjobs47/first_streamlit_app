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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list,index))
streamlit.dataframe(my_fruit_list)
