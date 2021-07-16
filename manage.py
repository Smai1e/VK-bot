import re
import random
import vk_api
import json
import requests
from labs import labs_OS, labs_Network, labs_OOP

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot

def get_file(lab):
        for x in lab:
            vk.method("messages.send", {"peer_id": event.user_id, "attachment": x,  "random_id": 0})

main_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "О боте 🎯"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Полезные ссылки 🌏"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Лабы 📃"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Контакты 📙"
            },
            "color": "primary"
        }]
    ]
}

main_keyboard = json.dumps(main_keyboard, ensure_ascii=False).encode('utf-8')
main_keyboard = str(main_keyboard.decode('utf-8'))

about_us_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Для чего нужен бот?"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Что он умеет?"
            },
            "color": "positive"
        }],
		[{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Контакты 📙",
            },
            "color": "primary"
        }]
    ]
}

about_us_keyboard = json.dumps(about_us_keyboard, ensure_ascii=False).encode('utf-8')
about_us_keyboard = str(about_us_keyboard.decode('utf-8'))


labs_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "ОС"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Сети"
            },
            "color": "primary"
        },
		{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "ООП",
            },
            "color": "primary"
        }]
    ]
}

labs_keyboard = json.dumps(labs_keyboard, ensure_ascii=False).encode('utf-8')
labs_keyboard = str(labs_keyboard.decode('utf-8'))

app_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"1\"}",
                "label": "Расписание занятий 🕐",
                "link": "https://www.tu-bryansk.ru/education/schedule/"
            }
        }],
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"2\"}",
                "label": "Сайт БГТУ 📟",
                "link": "https://www.tu-bryansk.ru/"
            }
        }],
		[{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"3\"}",
                "label": "ARM ☢",
                "link": "http://arm.iipo.tu-bryansk.ru/"
            }
        }],
		[{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"4\"}",
                "label": "ЭИОС БГТУ 📖",
                "link": "http://edu.tu-bryansk.ru/"
            }
        }]
    ]
}

app_keyboard = json.dumps(app_keyboard, ensure_ascii=False).encode('utf-8')
app_keyboard = str(app_keyboard.decode('utf-8'))

contacts_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"1\"}",
                "label": "Андрею",
                "link": "https://vk.com/andreyromashin"
            }
        }],

    ]
}

contacts_keyboard = json.dumps(contacts_keyboard, ensure_ascii=False).encode('utf-8')
contacts_keyboard = str(contacts_keyboard.decode('utf-8'))

def write_msg(user_id, message, key):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'keyboard': key,
               'random_id': random.randint(0, 2048)})

vk = vk_api.VkApi(token=
                  "........")


longpoll = VkLongPoll(vk)


try:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                bot = VkBot(event.user_id)

                message = event.text.lower()

                if event.text.lower() == "о боте 🎯":
                    write_msg(event.user_id, "Немного о проекте", about_us_keyboard)
                elif event.text.lower() == "полезные ссылки 🌏":
                    write_msg(event.user_id, "Посмотри, что есть здесь!", app_keyboard)
                elif event.text.lower() == "лабы 📃":
                    write_msg(event.user_id, "Посмотри, что есть здесь!", labs_keyboard)
                elif event.text.lower() == "ос":
                	get_file(labs_OS)
                elif event.text.lower() == "сети":
                	get_file(labs_Network)
                elif event.text.lower() == "ооп":
                	get_file(labs_OOP)
                elif event.text.lower() == "контакты 📙":
                    write_msg(event.user_id, "По любым вопросам можешь обращаться к:", contacts_keyboard)
                elif event.text.lower() == "фото":
                    vk.method("messages.send", {"peer_id": event.user_id, "message": "Это я. Ля какой красивый!", "attachment": "photo-205338911_457239017", "random_id": 0})
                else:
                    write_msg(event.user_id, bot.new_message(event.text), main_keyboard)

except Exception as e:
    print(e)
