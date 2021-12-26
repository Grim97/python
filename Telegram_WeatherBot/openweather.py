# import requests
# import json
# import os

def owapi():
    apikey = os.environ.get( 'BOT2' )
    apicall = "http://api.openweathermap.org/data/2.5/weather?q=Chennai&units=metric&appid={}".format(apikey)
    api = requests.get(apicall)
    apifinal = api.content.decode('utf8')
    apifinal = json.loads(apifinal)

    def predic():
        global climate
        climate = apifinal["weather"][0]["description"]
        #Debugging Print statement
        print(climate)
        #Return for the calling function
        #return climate
        for m in apifinal["main"]:
            print(type(m))

    predic()

#Uncomment below one line for #Complete RUN
#owapi()

#Uncomment below code to run this script independently
# if __name__ == "__main__":
#     owapi()

