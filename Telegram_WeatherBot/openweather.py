import requests
import json

def owapi():
    apicall = "http://api.openweathermap.org/data/2.5/weather?q=Chennai&units=metric&appid=xxx" #TOken ID here xxx ;)
    api = requests.get(apicall)
    apifinal = api.content.decode('utf8')
    apifinal = json.loads(apifinal)

    def predic():
        global climate
        #count=0
        climate = apifinal["weather"][0]["description"]
        #print(climate)
        return climate
        #print(climate)
        # if climate == "mist":
        #     #return (climate + "-" "Wear your sweaters")
        #     print(climate + "-" "Wear your sweaters")
        #     #count= count+1
        #
        # else:
        #     return ("COOOLLLD")

    predic()

owapi()
# if __name__ == "__main__":
#     owapi()
