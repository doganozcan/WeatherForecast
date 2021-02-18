from flask import Flask, render_template, request, url_for
import requests
import json 

app = Flask(__name__)

def weather_Forecast(self):
    city=self

    apiKey='YOUR_API_KEY' #https://home.openweathermap.org/users/sign_up            

    response= requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}')

    weatherData=response.json()

    skyDescription=weatherData['weather'][0]['description']
    cityName=weatherData['name']
    skyTypes = ['clear sky', 'few clouds','overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','snow','mist']

    for i in range(len(skyTypes)):
        if skyDescription == skyTypes[i]:
            skyDescription=skyTypes[i]
        
     
    temp=round((weatherData['main']['temp']-273.15),2)
    feels_temp=round((weatherData['main']['feels_like']-273.15),2)
    temp_min=round((weatherData['main']['temp_min']-273.15),2)
    temp_max=round((weatherData['main']['temp_max']-273.15),2)
    
    
    weatherForecast={
    "City":cityName,
    "Sky":skyDescription,
    "Temp":temp,
    "Feels":feels_temp,
    "Min":temp_min,
    "Max":temp_max    
}
    return weatherForecast

@app.route("/", methods=['POST','GET'])
def index():

    if request.method == 'POST':
        city = request.form['data']
        if not city:
            return render_template('index.html')

        a =  weather_Forecast(city)
        return render_template('result.html', result = a)
    else:
        return render_template('index.html')
        
if __name__=="__main__":
    
    app.run(debug=True)