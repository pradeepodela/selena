import pyttsx3
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def speech(input):



    if 'what are you doing' in input:
        speak('learning something new to improve my self')

    elif  'you' and 'happy' in input:
        speak('i am always happy wen i surrounded by smart people and i am exited to meet people like you')


    elif 'your' and 'favourite' and 'color' in input:
        speak("my favorite color is green")


    elif 'your' and 'favourite' and 'actor' in input:
        speak("i like sir rajnikanth")

    elif 'your' and 'favourite' and 'food' in input:
        speak("my yourfavorite food is charging because i dont eat foods which humans eat")
        
    elif 'how are you' in input:
        speak('i am fine hope you are also doing good')


    elif 'your' and'favourite' and 'movie'  in input:
        speak("i like robo movie which was of sir rajnikanth")
    
    elif 'you' and 'safe' in input:
        speak(' yes i am a safe robo who is friendly with humans i was invented to help humans')

    elif 'AI' and 'safe' and 'humans' in input:
        speak("yes AI is safe for humans it helps the humans in many ways unless u dont misusize the AI is safe")
    elif 'who invited you' in input:
        speak('i was developed by sir pradeep he is my founder')

    elif 'hello' in input:
        speak('Hello Sir')

    elif 'who invented you' in input or 'who made you' in input:
        speak('i was developed by sir pradeep he is my founder')

    elif 'thank you' in input:
        speak('hoo your welcome sir ')


    elif 'do you lie' in input:
        speak("no  robots never ever lie")

    elif 'who are you' in input or 'what is your name' in input or 'introduce yourself' in input:
        speak("my name is selena i am a personal assistent robo on a mession to help people in many ways i was invented by pradeep ")
        
    elif 'you' and 'are' and'great' in input:
        speak('thanks for your compliment')
        
    else:
        input = input
        speak('Searching...')
        try:
            results = wikipedia.summary(input, sentences=2)
            speak(results)

        except:
            speak("sorry sir say again")
        return input











