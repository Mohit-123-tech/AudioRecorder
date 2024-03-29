from json import load
from speech_recognition import Recognizer, Microphone
from playsound import playsound

API = load(open("src/json/api.json"))

r = Recognizer()

FileName = input("Enter Audio File Name : ")

path = API["audio"]

with Microphone() as s:
    data = r.listen(source=s)
    
    with open(f"{path}{FileName}.wav", 'wb') as f:
        f.write(data.get_wav_data())
        f.close()       

playsound(path+FileName+".wav")

