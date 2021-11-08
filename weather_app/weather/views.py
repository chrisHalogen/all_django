from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '665a90a6f9232d4680203ea3702e1763'
        try:
            request_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        except:
            return render(request,"City Not Found")

        source = urllib.request.urlopen(request_url).read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }

    else:
        data = {}

    return render(request,'main/index.html',data)