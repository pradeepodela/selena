##### BOT ######
import pyttsx3
import speech_recognition as sr

iteams = []
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
pizzahurtmenu = ['chicken pizza','veg pizza','chees pizza']

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

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
        speak('hellow')

    return query

def shope():
    speak('we have')
    for x in pizzahurtmenu:
        speak(x)
def add(iteamss):
    iteamss = iteamss.split()
    if 'to' in iteamss:
        x = iteamss.replace("to","2")
        iteams.append(x)
        print(iteams)



def bot():
    while True:
        speak('hallow sir welcome to pizahurt how may i help you')
        query = myCommand()
        query = query.lower()


        if 'menu' in  query:
            shope()

        elif 'cost' and 'chicken pizza' in query:
            speak('the cost for chicken pizza is 10 dollars only')

        elif 'cost' and 'veg pizza' in query:
            speak('the cost for veg pizza is 15 dollars only')


        elif 'cost' and 'cheese pizza' in query:
            speak('the cost for chese pizza is 20 dollars only')


        elif 'add' or 'ad' in query:
            speak('what iteams would u want to add sir')
            iteams = myCommand()
            add(iteams)


