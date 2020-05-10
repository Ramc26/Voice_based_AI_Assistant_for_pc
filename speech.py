import speech_recognition as ram
from gtts import gTTS
from playsound import playsound
import time
import random
import webbrowser
from datetime import datetime
import os
print("""
        |========================================================|
        |       PERSONALIZED VOICE BASED A.I ASSISTANT           | 
        |========================================================|
        |##                   ##  ########  ##########  ##     ##|
        | ##       ###       ##      ##     ##          ##     ##|
        |  ##     ## ##     ##       ##     ##########  #########|
        |   ##   ##   ##   ##        ##             ##  ##     ##|
        |    #####     #####      ########  ##########  ##     ##|
        |========================================================|
        |        CODED AND CREATED BY RAMARAO BIKKINA            |
        |========================================================|
""")
r=ram.Recognizer()
##music=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
##msc=random.choice(music)
##msc="songs/"+str(msc)+".mp3"
##playsound(str(msc))
jokeset=("Doctor: I'm sorry but you suffer from a terminal illness and have only 10 to live.\n Patient: What do you mean, 10? 10 what? Months? Weeks?!\nDoctor: Nine.",
         "Dentist: This will hurt a little.\npatient: OK.\nDentist: I’ve been having an affair with your wife for a while now.",
         "I got another letter from this lawyer today. It said “Final Notice”. Good that he will not bother me anymore.",
         "Two donkeys are standing at a roadside, one asks the other: So, shall we cross?\nThe other shakes his head: No way, look at what happened to the zebra.",
         "Beggar: Babu 8rs unte dharmam cheyandi, tea thagutha.\nMan: Tea 4rs kada?\nBeggar: Naku, na lover ki.\nMan: Beggar ki lover aa?\nBeggar: lover vachake beggar ayyanu...babu",
         "Father: Pakkanti ammaini chudara, 1st class lo pass ayindi......\nSon: Ala chudatum valle,nenu fail ayindi.",
         "Principal: Write ur father name in english.\nStudent: Temple steps water king.\nPrincipal: Are u joking\nStudent: No sir, i am serious. my father name is GUDI METLA GANGA RAJU.")
with ram.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
##    print("I'm listening, code word Please:")
##    playsound('audio/codeword.mp3')
##    audio=r.listen(source)
##    text=r.recognize_google(audio)
##    print("you said "+text+".")
##    if str(text)== "wish" or str(text)=="Wish":
    print("Hello! Boss, Welcome!")
    playsound('audio/greeting.mp3')
    print("""Which application want you to open:
------>Date and Time<-------
---------->Weather<---------
---------->Google<----------
---------->Music<-----------
---------->Movies<----------
---------->Notes<-----------
---------->Editing<---------
------>Tell me a joke<------
---------->Website<---------
-------->Dictionary<--------
Random searchs like Dollor cost, currency conversion, what ever you need, I'm in your service...""")
    while True:
        time.sleep(1)
        print("I'm Listening....")
        playsound('audio/listen.mp3')
        audio=r.listen(source, timeout=5)
        text=r.recognize_google(audio).lower()
        tts = gTTS("Boss. you said "+str(text)+". i'm opening it")
        tts.save('audio/text.mp3')
        print("you said "+text+".")
        playsound('audio/text.mp3')
        os.remove('audio/text.mp3')
        time.sleep(1)
        if str(text)=="music":
            os.startfile("E:\music")
        elif str(text)=="movies":
            os.startfile('E:\movies')
        elif str(text)=="who is your creator" or str(text)=="who created you" or str(text)=="how did you made" or str(text)=="who coded you" :
            print("""
    I was Coded and Created By VEERA VENKATA RAMARAO BIKKINA
    On 21,April, 2020
    """)
            playsound('audio/creator.mp3')
        elif "google" in text:
            os.startfile("chrome.exe")
        elif "notes" in text or "notepad" in text:
            os.system("start notepad.exe")
        elif "editing" in text:
            os.system("start Photoshop.exe")
        elif "song" in text or 'paata' in text:
            for i in range(0,10):
                msc=int(random.randint(0,20))
                msc="songs/"+str(msc)+".mp3"
                playsound(msc, False)
        elif str(text)=='website':
            print("please, Mention website name to be open. I'm Listening...")
            audio=r.listen(source)
            text=r.recognize_google(audio)
            print("I'm going to open " +text.replace(" ","")+".")
            link='https://'+text.replace(" ","")+'.com'
            webbrowser.open(link)
        elif 'date' in text or 'time' in text:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("date and time =", dt_string)
            tts = gTTS("Boss. The Time and date are "+str(dt_string)+". Have a good day")
            tts.save('audio/date.mp3')
            playsound('audio/date.mp3')
            os.remove('audio/date.mp3')
            time.sleep(1)
        elif 'weather' in text:
            webbrowser.open('https://www.google.com/search?q=present+weather')
        elif str(text)=='dictionary':
            print("please, Mention unknown word. I'm Listening...")
            playsound('audio/dict.mp3')
            audio=r.listen(source)
            text=r.recognize_google(audio)
            print("I'm going to search for " +text+".")
            tts = gTTS("Boss. you asked me to search for"+str(text)+". i'm going for search")
            tts.save('audio/dict1.mp3')
            playsound('audio/dict1.mp3')
            os.remove('audio/dict1.mp3')
            time.sleep(1)
            link='https://www.google.com/search?q='+text+'+meaning'
            webbrowser.open(link)
            os.remove('audio/dict1.mp3')
        elif "open gmail" in text or "open mail" in text:
            print("okay Boss, I'm accessing your mail.")
            playsound('audio/mail.mp3')
            time.sleep(2)
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "headlines" in text or "news" in text:
            webbrowser.open('https://epaper.eenadu.net/Home/Index')
        else:
            print("I'm going to search for " +text+".")
            text=text.replace(" ","+")
            link='https://www.google.com/search?q='+text
            webbrowser.open(link)

