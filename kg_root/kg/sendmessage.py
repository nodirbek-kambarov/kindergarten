import requests

token = '1507036531:AAElnvTaU1w-ElViM4wTRW_ujW3bOMi0c4o'
chat_id = '-527330715'


def sendTelegram(text):
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage?'
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text

    })
