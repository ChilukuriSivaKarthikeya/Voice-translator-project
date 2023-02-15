from django.shortcuts import render,redirect
from django.http import HttpResponse
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
import pygame
src_lang=to_lang=query=text=""

def home(request):
    return render(request,"voice.html")
def listen(request):
    global src_lang,to_lang
    src_lang = request.POST["src_lang"]
    to_lang = request.POST["dest_lang"]  
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
           print("listening.....")
           #r.pause_threshold = 1
           r.adjust_for_ambient_noise(source,duration=1)
           audio = r.listen(source)
        try:
           print("Recognizing.....")
           query1 = r.recognize_google(audio, language=src_lang)
           print(f"The User said {query1}\n")
        except Exception as e:
           print("can't Recognizing.....")
           text1="can't recognize please speak again"
           speak = gTTS(text=text1, lang=to_lang, slow=False)
           file1 = BytesIO()
           speak.write_to_fp(file1)
           pygame.mixer.init()
           pygame.mixer.music.load(file1,"mp3")
           pygame.mixer.music.play()
           clock = pygame.time.Clock()
           while pygame.mixer.music.get_busy():
                clock.tick(60)
           return "None"
        return query1
    global query
    query = takecommand()
    while (query == "None"):
        query = takecommand()
    translator = Translator()
    text_to_translate = translator.translate(query,src=src_lang,dest=to_lang)
    global text
    text = text_to_translate.text
    content={"src":query,"dest":text}
    return render(request,"translator.html",content)

def speak_src(request):
    global src_lang,text,query
    speak = gTTS(text=query, lang=src_lang, slow=False)
    file1 = BytesIO()
    speak.write_to_fp(file1)
    pygame.mixer.init()
    pygame.mixer.music.load(file1,"mp3")
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
         clock.tick(60)
    content={"src":query,"dest":text}
    return render(request,"translator.html",content)

def speak_dest(request):
    global to_lang,query,text
    speak = gTTS(text=text, lang=to_lang, slow=False)
    file1 = BytesIO()
    speak.write_to_fp(file1)
    pygame.mixer.init()
    pygame.mixer.music.load(file1,"mp3")
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
         clock.tick(60)
    content={"src":query,"dest":text}
    return render(request,"translator.html",content)


