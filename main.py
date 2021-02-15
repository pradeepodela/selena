from tr import *
from bot import *
import pyttsx3
import pywhatkit as kit
import webbrowser
import smtplib
import random
import speech_recognition as sr
import datetime
import sys

engine = pyttsx3.init('sapi5')



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning sir!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon sir!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening sir!')

def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("recognizeing...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:

        #speak('sorry sir can you please try by typeing')
        #query = str(input('Command: '))
        query = 'hellow'


    return query
greetMe()
speak('this is your assistent selena how may i help you sir')

if __name__ == '__main__':
    while True:

        query = myCommand()
        query = query.lower()


        

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay sir what do you want to search')
            search = myCommand()
            kit.search(search)


        elif 'open instagram' in query:
            webbrowser.open('www.instagram.com')

        elif 'open twiter' in query:
            webbrowser.open('www.twiter.in')

        elif 'open linkedin' in query:
            webbrowser.open('www.linkedin.in')

        elif 'open github' in query:
            webbrowser.open('www.github.com')

        elif 'open twitter' in query:
            webbrowser.open('www.Twitter.in')

        elif 'open amazon' in query:
            webbrowser.open('www.amazon.in')


        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'john' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("odelapradeep12@gmail.com", 'pradeep9246')
                    server.sendmail('odelapradeep12@gmail.com', "odelaswapna@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'the date' in query:
            year = str(datetime.datetime.now().year)
            month = str(datetime.datetime.now().month)
            date = str(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)
            speak('have a nice day sir')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'how to make' in query:
            kit.playonyt(query)
            speak('got it')


        elif 'open shop' in query:
            bot()



        elif 'the date' in query:
            year = str(datetime.datetime.now().year)
            month = str(datetime.datetime.now().month)
            date = str(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strTime}")



        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'roll a die' in query or 'roller a die' in query:
            numbers = ['1','2','3','4','5','6']
            randomnumber = (random.choice(numbers))
            speak(randomnumber)


        elif 'play the song' in query:
            query = query.replace('play the song','song')
            kit.playonyt(query)

        elif 'play music' in query :
            songs = ['//www.youtube.com/watch?v=BBAyRBTfsOU', 'https://www.youtube.com/watch?v=Pm77L5Loazc', 'https://www.youtube.com/watch?v=LPsyTf6EK5U','https://www.youtube.com/watch?v=kJQP7kiw5Fk']
            randomsong = (random.choice(songs))
            webbrowser.open(randomsong)
            speak('Okay sir')

            speak('Okay, here is your music! Enjoy!')


        else:
            speech(query)


        #speak('plese say the next command sir')
