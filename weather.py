import requests
import tkinter as tk
import datetime as dt
api_key = '02d15f5175c343aca514bfc25b153d86'

def get_weather():
    user_input = entry.get()

    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    data = weather_data.json()

    if weather_data.status_code == 200:

        try:
            # for day in data['daily']:
            #     date = day['dt']
            #     date = dt.utcfromtimestamp(date).strftime('%y-%m-%d')

            weather = data['weather'][0]['main']
            temp = round(data['main']['temp'])
            humidity = data['main']['humidity']

            # date_output = f'Date:{date}'
            weather_output =f'the weather in {user_input} is: {weather}\n'
            temp_output = f'the temperature in {user_input} is: {temp}°F\n'
            humidity_output = f'the humidity in {user_input} is: {humidity}%\n'

            text_widget.delete(1.0, tk.END)
            # text_widget.insert(tk.END, date_output)
            text_widget.insert(tk.END, weather_output)
            text_widget.insert(tk.END, temp_output)
            text_widget.insert(tk.END, humidity_output)
        
        except KeyError as e:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, {e})

    else:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "Error: city not found or invalid request!")

root = tk.Tk()
label = tk.Label(root, text = 'Search Your Favorite Cities', font='bold')
label.grid()

root.title("weather app")
root.geometry("500x500")

entry = tk.Entry(root, width=50, border=5)
entry.grid(row=10, column=0, columnspan=4, padx=10, pady=10)

text_widget = tk.Text(root, height=10, width=57, border= 10,)
text_widget.grid()

button1= tk.Button(root, text='Get Weather', command=get_weather)
button1.grid()

root.mainloop()