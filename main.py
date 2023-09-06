import requests

def getCyrptoData():
    response = requests.get(url="https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    return response.json()

cyrptoResponse = getCyrptoData()
userInput = input("Enter your cyrpto : ")
for cyr in cyrptoResponse:
    if cyr["currency"] == userInput:
        print(cyr["price"])