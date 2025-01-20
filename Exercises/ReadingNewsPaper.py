from win32com.client import Dispatch
import json
import requests

def speak(str):
    sp = Dispatch("SAPI.SpVoice")
    sp.Speak(str)

url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=b12672ede9ca4916bbfd9bb0e0b37399')
speak("Today's News Headlines")
httpRequest = requests.get(url).text
jsonRequest = json.loads(httpRequest)
print(jsonRequest['articles'])
articles = jsonRequest['articles']
# speak("Tumhara kia haal ha?? Shan Ali Mughal, tum kahan pr rehty ho or kia krty ho?")
for items in articles:
    speak(items['title'])
    speak("I am going to read next news Sir!")
    speak("Mister Shan Ali Mughal Please Listen Carefully...")

