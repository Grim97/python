import json
import time
import requests

Bot_Token = 'xxx' # Token ID here ;)
baselink = "https://api.telegram.org/bot{}/".format(Bot_Token)

def getme_url(link):
    response = requests.get(link)
    content = response.content.decode("utf8")
    return content

def get_last_chat_id_and_text(offset):
    link = baselink + "getUpdates?timeout=5000"
    if offset:
        link = link + '&offset={}'.format(offset)
    fetched_data = json.loads(getme_url(link))
    total_updates = len(fetched_data['result'])
    last_update = total_updates -1
    text = fetched_data["result"][last_update]["message"]["text"]
    chat_id = fetched_data["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def sendmessage(ChatId, Msg):
    link = baselink + "sendMessage?chat_id={}&text={}".format(ChatId, Msg)
    getme_url(link)

def main():
    last_chat = (None, None)
    while(True):
        print("Getting Updates")
        offset = None
        text, chat_id = get_last_chat_id_and_text(offset)
        if(text, chat_id) != last_chat:
            if (text == 'Hee'):
                sendmessage(chat_id, 'Hello' )
            elif(text == 'Hello'):
                sendmessage(chat_id, 'Hey you')
            elif(text == '/weather'):
                import openweather
                openweather.owapi()
                print(openweather.climate)
                sendmessage(chat_id, 'weather-{}'.format(openweather.climate))
            last_chat = (text, chat_id)
        time.sleep(2)

if __name__ == "__main__":
    main()

