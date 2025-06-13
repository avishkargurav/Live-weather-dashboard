import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_autorefresh import st_autorefresh

api_key='0762b634424e391f29e0f305d4028551'


cities=[
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
    "Nagpur", "Indore", "Bhopal", "Patna", "Ludhiana", "Agra", "Kanpur", "Varanasi", "Nashik", "Thane",
    "Surat", "Vadodara", "Amritsar", "Raipur", "Ranchi", "Jabalpur", "Guwahati", "Dehradun", "Chandigarh", "Coimbatore",
    "Kochi", "Vijayawada", "Mysuru", "Madurai", "Jodhpur", "Udaipur", "Shillong", "Gangtok", "Panaji", "Trivandrum",
    "Imphal", "Aizawl", "Itanagar", "Dispur", "Port Blair", "Patiala", "Dhanbad", "Gaya"]
weather_data=[]
for city in cities:
      url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
      response=requests.get(url)
      
      if response.status_code==200:
       data=response.json()
       
       weather_detail={
       "city":city,
       "Teamperature(*C)":data['main']['temp'],
       "Humidity (%)":data['main']['humidity'],
       "weather":data['weather'][0]['main'],
       "description":data['weather'][0]['description'],
       "wind speed (m/s)":data['wind']['speed']

    }
      weather_data.append(weather_detail)
else: print(f"fail to get the data of {city} city....")
 


    
df=pd.DataFrame(weather_data)
df.to_csv("india weather.csv",index=False)
print("\n weather data is stored in database")
# df=pd.read_csv("india_weather.csv")
pd.set_option('display.max_rows',None)


st.title("Welcome To Check Live Data From Your favourite cities")
st.dataframe(df)
st.subheader("Temprature Comparison")
fig,ax=plt.subplots(figsize=(10,16))#matplotlib code
ax.barh(df['city'],df['Teamperature(*C)'])



plt.xlabel("Temprature (*c)",fontsize=30)

plt.ylabel("The All India Cities Name", fontsize=30)

plt.tight_layout()
st.pyplot(fig)
Top_rainy = df[df['description'].str.contains("rain", case=False)].head(10)
st.subheader("Top 10 Raining Cities")
st.dataframe(Top_rainy)

st.subheader("Top 10 Raining Cities Chart")
fig_rain, ax_rain = plt.subplots(figsize=(10, 6))
ax_rain.bar(Top_rainy['city'], Top_rainy['Teamperature(*C)'], color='blue')
ax_rain.set_xlabel("City")
ax_rain.set_ylabel("Temperature (°C)")
plt.tight_layout()
st.pyplot(fig_rain)

Top_clear_weather = df[df['weather'].str.contains("clear", case=False)].head(10)
st.subheader("Top 10 Clear Weather Cities")
st.dataframe(Top_clear_weather)

st.subheader("Top 10 Clear Weather Cities Chart")
fig_clear, ax_clear = plt.subplots(figsize=(10, 6))
ax_clear.bar(Top_clear_weather['city'], Top_clear_weather['Teamperature(*C)'], color='green')
ax_clear.set_xlabel("City")
ax_clear.set_ylabel("Temperature (°C)")
plt.tight_layout()
st.pyplot(fig_clear)

Top_cloudy_weather=df[df['weather'].str.contains("clouds",case=False)].head(10)
st.subheader("Top 10 Cloudy Cities")
st.dataframe(Top_cloudy_weather)
fig_cloud,ax_cloud=plt.subplots(figsize=(10,6))
ax_cloud.bar(Top_cloudy_weather['city'],Top_cloudy_weather['Teamperature(*C)'],color="blue")
ax_cloud.set_xlabel("Cities Name")
ax_cloud.set_ylabel("Temprature (°C)")
plt.tight_layout()
st.pyplot(fig_cloud)
 
st.title("Thank you For visiting MyProject..\n" \
" We can add new charts soon like:- Camparision Chart,Most cloudy City,most rainy city")
st_autorefresh(interval=3000000,key="Refresh")
if st.button("Refresh The Data"):
    st.rerun()