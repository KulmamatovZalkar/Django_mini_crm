import requests

TOKEN = '5531230395:AAFTyb-cebAtIPX2JmP3co1e3IK_oXEx8uc'
chat_id = 222675157
text = "Test_2"

def sendTelegram():
    api = "https://api.telegram.org/bot"
    method = api + TOKEN + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })

sendTelegram()