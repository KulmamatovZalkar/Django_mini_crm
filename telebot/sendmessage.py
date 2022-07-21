from django.conf import settings
import requests
from .models import TeleSettings 


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        telesttings = TeleSettings.objects.get(pk=1)
        token = str(telesttings.tg_token)
        chat_id = str(telesttings.tg_chat)
        text = str(telesttings.tg_msg)
        api = "https://api.telegram.org/bot"
        method = api + token + '/sendMessage'

        if text.rfind('{') and text.rfind('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.rfind('{')]
            part_2 = text[text.rfind('}')+1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]

            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slice = text
        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print("ошибка отправки")
            elif req.status_code == 500:
                print("Ошибка 500")
            else:
                print("Сообщение отправлено")
    else:
        pass

