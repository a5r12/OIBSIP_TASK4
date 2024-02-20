from tkinter import *
import requests

w_api=Tk()
w_api.title("weather API")
w_api.geometry("350x550")
w_api.configure(background="black")

    # OpenWeatherMap API key
api_key = '0fb86636424303c56b385400b08a7a98'
city_name = StringVar()  # desired city name

country_= StringVar()
temperature_= StringVar()
description_ = StringVar()
humidity_= StringVar()
error_=StringVar()


def get_weather():

        # API endpoint URL for current weather data
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name.get()}&appid={api_key}&units=metric'

        # Send a GET request to the API
    response = requests.get(url)


    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        weather_data = response.json()

        # Extract relevant information
        country=weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        # providing data to the global variables
        country_.set(country)
        temperature_.set(temperature)
        description_.set(description)
        humidity_.set(humidity)
        error_.set('')
        

    else:
        e = f'Error: Unable to fetch weather data. Status Code: {response.status_code}'

        error_.set(e)
        
        # for error set all the data as 0 and the 'error_' variable as msg 'e'
        country= 0
        temperature = 0
        description = 0
        humidity = 0

        country_.set(country)
        temperature_.set(temperature)
        description_.set(description)
        humidity_.set(humidity)



# labels, button and entry to create simple gui structure..

Label(w_api,text="Enter city name:",bg="black",fg="yellow",font="bold").pack(ipady=5, pady=5)
Entry(w_api,textvariable=city_name,bg="white",fg="blue",font='bold').pack(ipady=5,ipadx=5)

Button(w_api,text='Show weather',bg='yellow',fg='black',command=get_weather,font='bold').pack(ipadx=2,ipady=2 , pady=15)

Label(w_api,text="Country name:",bg="black",fg="yellow",font="bold").pack(ipady=5, pady=5)
Entry(w_api,textvariable=country_,fg='blue',bg="black",font= 'bold').pack()

Label(w_api,text="Temperature (in C): ",bg="black",fg="yellow",font="bold").pack(ipady=5, pady=5)
Entry(w_api,textvariable=temperature_,fg='blue',bg="black",font= 'bold').pack()

Label(w_api,text="Description: ",bg="black",fg="yellow",font="bold").pack(ipady=5, pady=5)
Entry(w_api,textvariable=description_,fg='blue',bg="black",font= 'bold').pack()

Label(w_api,text="Humidity (in %):",bg="black",fg="yellow",font="bold").pack(ipady=5, pady=5)
Entry(w_api,textvariable=humidity_,fg='blue',bg="black",font= 'bold').pack()

Label(w_api,textvariable=error_, fg="red",bg="black").pack(pady=5)


w_api.mainloop()

