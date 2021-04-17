import requests

def get_prediction(mode='temwind'):
    r = requests.get('http://wttr.in/moscow?format=4')
    temp, wind = r.text.split(' ')[2][2:], r.text.split()[3][3:]
    if mode == 'temp':
        return temp
    elif mode == 'wind':
        return wind
    elif mode == 'tempwind':
        return temp, wind