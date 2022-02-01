#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asyncio.windows_events import NULL
import os
import requests
import json
import sys

class BotApi:
    
    _bot_token = os.environ.get('BOT1')
    baselink = "https://api.telegram.org/bot{}/".format(_bot_token)

    def __init__(self):
        pass

    def getme_url(self, link):
        try:
            response = requests.get(link)
            print(type(response))
        except requests.ConnectionError:
            print("Please Check your Internet")
        except requests.Timeout:
            print("Took too much time. Try again!")
            sys.exit("Exit due to Connection Issue")   
        except Exception as e:
            print("Exception Occurred", e)
            sys.exit("Error -", requests.status_codes)
        content = response.content.decode("utf8")
        return content

    def get_last_chat_id_and_text(self, offset):
        link = self.baselink + "getUpdates?timeout=10"
        if offset:
            link = link + '&offset={}'.format(offset)
        fetched_data = json.loads(self.getme_url(link))
        print(fetched_data)
        total_updates = len(fetched_data['result'])
        last_update = total_updates -1
        print(total_updates, last_update)
        text = fetched_data["result"][last_update]["message"]["text"].lower()
        chat_id = fetched_data["result"][last_update]["message"]["chat"]["id"]
        user = fetched_data["result"][last_update]["message"]["from"]["first_name"]
        return (text, chat_id, user)

    def sendmessage(self, ChatId, Msg):
        link = self.baselink + "sendMessage?chat_id={}&text={}".format(ChatId, Msg)
        self.getme_url(link)

def main():
    token = BotApi()
    token.getme_url(token.baselink)
    last_chat = (None, None)
    while(True):
        offset = NULL
        text, chat_id, user = token.get_last_chat_id_and_text(offset)
        if(text, chat_id) != last_chat:
            if text in ['hi', 'hello', 'hey']:
                token.sendmessage( chat_id, 'Hello there {}'.format(user))
            elif(text == '/weather'):
                import openweather
                openweather.owapi()
                print(openweather.climate)
                token.sendmessage(chat_id, 'weather-{}'.format(openweather.climate))
            last_chat = (text, chat_id)
            print("Debug---->", last_chat)

if __name__ == "__main__":
    main()
