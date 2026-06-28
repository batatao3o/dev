import requests

while True:                              # ← loop starts here
    city = input('which city? ')

    try:

        response = requests.get(f'https://wttr.in/{city}?format=j1')
        data = response.json()
        if 'current_condition' in data and data['current_condition']:
            temp = data['current_condition'][0]['temp_C']
            feels_like = data['current_condition'][0]['FeelsLikeC']
            description = data['current_condition'][0]['weatherDesc'][0]['value']
            print(f'{city} weather right now:')
            print(f'temperature: {temp}°C')
            print(f'feels like: {feels_like}°C')
            print(f'condition: {description}')
        else:
            print('sorry, we could not find weather for that city')
    except:                                # catches any crash
        print('something went wrong, please try again')
        
    again = input('check another city? (yes/no): ')
    if again == 'no':
        print('goodbye!')
        break

