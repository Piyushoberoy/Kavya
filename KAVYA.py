import pyttsx3
import speech_recognition as sr
import time
import datetime
import webbrowser
import urllib
import os
import mysql.connector as ms

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 125)

setup=ms.connect(host='localhost',user='root',passwd='1234',database='KAVYA')
c=setup.cursor()

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def user():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing')
        query=r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception:
        print("Say that again please")
        return 'None'
    return query

def help1():
    say('How I can help you?')
    query=user().lower()
    if 'calculate' in query:
        say("If you need to calculate like addition, subtraction, multiplication, etc. You need to just say calculate then, I will ask you which type of calculation you wan't then you have to select just your choice and after typing numbers you will get your answer.")
    elif 'time' in query:
        say("If you need to know time, date and day then, you have to just say 'time' or 'what's the time dear' and something like that.")
    elif 'web' in query:
        say("If you need to open some websites like facebook, twitter, etc then, say your website name only. If it is not in my mind then I will direct you to one of my friend.")
    elif 'apps' or 'app' in query:
        say('If you need to open any application then, just say your application name I will open it for you. If it is not in my mind then I will direct you to one of my friend.')
    elif 'thank you' in query:
        say("You have clear your doubt. Let's proceed further.")
        main()
    else:
        say('Any more doubt, sir. If no then say thank you.')

def clock():
    localtime=time.asctime(time.localtime(time.time()))
    say(localtime)

def wishme():
    h=int(datetime.datetime.now().hour)
    if h>=4 and h<12:
        say('Good Moring sir')
    elif h>=12 and h<18:
        say('Good Afternoon sir')
    elif h>=18 and h<20:
        say('Good Evening sir')
    else:
        say('Good Night. Sweet dreams sir.')

def storage():
    say("Please tell details of person who's contact you wanted to feed, when I ask you about that particular field.")
    storage1()

def storage1():
    query = user().lower()
    if 'name' in query:
        say("Enter name of person.")
        N=input("NAME:")
        storage1()
    elif 'phone number' in query or 'number' in query:
        say("What is phone number of person?")
        p=int(input("PHONE NUMBER:"))
        storage1()
    elif 'address' in query:
        say("Now enter address of that person.")
        a=input("ADDRESS:")
        storage1()
    elif 'email id' in query or 'email' in query:
        say("Lastly, enter person's email id.")
        ei=input("EMAIL ID:")
        storage1()
    else:
        say("Do you wan't to add more details of the person?")
        query = user().lower()
        if 'yes' in query or 'yep' in query or 'ya' in query or 'haa' in query:
            say("Tell me more details.")
            storage1()
        else:
            say("I have saved your earlier details.")
            main()
    d="INSERT INTO CONTACT(S_NO,NAME,PHONE_NUMBER,ADDRESS,EMAIL_ID) VALUES('{}',{},'{}','{}')".format(N,p,a,ei)
    c.execute(d)
    setup.commit()

def web():
    say('Please tell website name which you want to search')
    query = user().lower()
    if 'google' in query:
        webbrowser.open('https://www.google.com/')
    elif 'youtube' in query:
        webbrowser.open('https://www.youtube.com/')
        
    elif 'facebook' in query:
        webbrowser.open('https://www.facebook.com/')
        
    elif 'twitter' in query:
        webbrowser.open('https://twitter.com/')
    
    else:
        say('Your website is not in my mind. Can I search this for you? Please say yes or no.')
        query = user().lower()
        if 'yes' in query:
            if 'yes' or 'yah' or 'ya' in query:
                say("I am directing you to the browser. Please enter your app name there or tell app name to my friend by clicking on the microphone. She will further guide you.")
                dir11="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(dir11)
            else:
                web()

def apps():
    say("Please tell app name which you wan't to open.")
    query=user().lower()
    if 'chrome' in query:
        say("Openning settings..")
        dir1="C:\\Users\\acer\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(dir1)
    elif 'mozilla' in query:
        say("Openning settings..")
        dir2="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(dir2)
    #elif  'calculator' in query:
     #   dir3=""
    elif 'python' in query:
        say("Openning Python..")
        dir4="D:\\PIYUSH\\PYTHON\\Lib\\idlelib\\idle.pyw"
        os.startfile(dir4)
    #elif 'camera' in query:
     #   dir5=""
    elif 'settings' or 'setting' in query:
        say("Openning settings..")
        dir6="%windir%\System32\Control.exe"
        os.startfile(dir6)
    else:
        say("Your application is not in lapi. If you need it then you have to install it. Can I do this for you? Say yes or no.")
        query=user().lower()
        if 'yes' or 'yah' or 'ya' in query:
            say("I am directing you to the browser. Please enter your app name there or tell app name to my friend by clicking on the microphone. She will further guide you.")
            dir11="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(dir11)
        else:
            apps()
def calculate():
    print("1. Addition")
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    say('Sir please enter your choice.')
    C=int(input('Enter your choice:'))
    if C==1:
        l=[]
        s=0
        x=int(input("Enter number of digits you want to add:"))
        for a in range(0,x):
            d=int(input("Enter your " + str(a+1) + " digits:"))
            l.append(d)
        for a1 in l:
            s+=a1
        say("The answer is " + str(s))
    
    elif C==2:
        l=[]
        s=0
        x=int(input("Enter number of digits you wan't to subtract:"))
        for a in range(0,x):
            d=int(input('Enter your ' + str(a+1) + ' digit:'))
            l.append(d)
        for a1 in l:
            s-=a1
        say('The answer is ' + str(s))
        
    elif C==3:
        l=[]
        s=1
        x=int(input("Enter number of digits you wan't to multiply:"))
        for a in range(0,x):
            d=int(input('Enter your ' + str(a+1) + ' digit:'))
            l.append(d)
        for a1 in l:
            s*=a1
        say('The answer is ' + str(s))
        
    elif C==4:
        v1=int(input('Enter first number:'))
        v2=int(input('Enter second number:'))
        s=v1/v2
        say('The answer is ' + str(s))
        
    else:
        say('Sir your choice is not in my mind.')
        calculate()

def main():
        while True:
            query=user().lower()
            if 'time' in query:
                clock()
            elif 'bye' in query:
                say('Bye sir. have a nice day')
                break
            #elif 'calculate' or 'calculator' in query:
            #    calculate()
            elif 'search' in query:
                web()
            elif 'open' in query:
                apps()
            elif 'wait' in query:
                say("Are you sure you want me to wait. Because if so then I will talk to you after your entered time.")
                query=user().lower()
                if 'yes' or 'yah' or 'ya' in query:
                    say("Enter your time after which you wan't me to active.")
                    T=int(input("Enter your time after which you wan't me to active (in minutes):"))
                    t=T*60
                    time.sleep(t)
            elif 'help' in query:
                help1()
            elif 'store' in query:
                storage()
            else:
                say('Any more questions.')
                main()

if __name__ == "__main__":
    wishme()
    say('How I can help you?')
    main()

