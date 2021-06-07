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
import akinator
import requests
from bs4 import BeautifulSoup
from pyzbar.pyzbar import decode
import numpy as np
import cv2

engine = pyttsx3.init('sapi5')



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)




def NewsFromBBC():

	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "4dbc17e007ab436fb66416009dfb59a8"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []

	for ar in article:
		results.append(ar["title"])
	speak('todays news is ')
	for i in range(len(results)):

		# printing all trending news
		speech = i + 1, results[i]

		speak(speech)
		print(i + 1, results[i])


	speak('this is todays news')


def speak(audio):
    print(audio)
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
        print(query)

        

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
            
            
        elif 'horoscope'  in query:
            speak('welcome to my horiscope ')
            speak('plese say your sunsign')
            hrs = myCommand()
            url = f'https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/{hrs}/'
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            hrp = soup.find("p", class_="margin-top-xs-0")
            speak(f'todays horiscope for your sunsign {hrs} is ')
            speak(hrp)

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
        elif "today's news" in query:
            NewsFromBBC()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'flames' in query:
            # function for removing common characters
            # with their respective occurrences
            def remove_match_char(list1, list2):

                for i in range(len(list1)):
                    for j in range(len(list2)):

                        # if common character is found
                        # then remove that character
                        # and return list of concatenated
                        # list with Ture Flag
                        if list1[i] == list2[j]:
                            c = list1[i]

                            # remove character from the list
                            list1.remove(c)
                            list2.remove(c)

                            # concatenation of two list elements with *
                            # * is act as border mark here
                            list3 = list1 + ["*"] + list2

                            # return the concatenated list with True flag
                            return [list3, True]

                # no common characters is found
                # return the concatenated list with False flag
                list3 = list1 + ["*"] + list2
                return [list3, False]


            # Driver code
            if __name__ == "__main__":

                # take first name
                speak('welcome to flames')
                speak('plese say Player 1 name')
                p1 = myCommand()
                speak('plese say Player 2 name')
                p2 = myCommand()
                #p1 = input("Player 1 name : ")

                # converted all letters into lower case
                p1 = p1.lower()

                # replace any space with empty string
                p1.replace(" ", "")

                # make a list of letters or characters
                p1_list = list(p1)

                # take 2nd name
                #p2 = input("Player 2 name : ")
                p2 = p2.lower()
                p2.replace(" ", "")
                p2_list = list(p2)

                # taking a flag as True initially
                proceed = True

                # keep calling remove_match_char function
                # untill common characters is found or
                # keep looping untill proceed flag is True
                while proceed:
                    # function calling and store return value
                    ret_list = remove_match_char(p1_list, p2_list)

                    # take out concatenated list from return list
                    con_list = ret_list[0]

                    # take out flag value from return list
                    proceed = ret_list[1]

                    # find the index of "*" / border mark
                    star_index = con_list.index("*")

                    # list slicing perform

                    # all characters before * store in p1_list
                    p1_list = con_list[: star_index]1

                    # all characters after * store in p2_list
                    p2_list = con_list[star_index + 1:]

                # count total remaining characters
                count = len(p1_list) + len(p2_list)

                # list of FLAMES acronym
                result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

                # keep looping untill only one item
                # is not remaining in the result list
                while len(result) > 1:

                    # store that index value from
                    # where we have to perform slicing.
                    split_index = (count % len(result) - 1)

                    # this steps is done for performing
                    # anticlock-wise circular fashion counting.
                    if split_index >= 0:

                        # list slicing
                        right = result[split_index + 1:]
                        left = result[: split_index]

                        # list concatenation
                        result = right + left

                    else:
                        result = result[: len(result) - 1]

                # print final result
                print("your both Relationship status is:", result[0])
                speak(f'your both Relationship status is {result[0]} ')





        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
            
        elif 'toss a coin' in query:
            coin = ['heads','tails']
            random_coin = (random.choice(coin))
            speak(f'i tossed a coin and got {random_coin}')

        elif 'roll a die' in query or 'roller a die' in query:
            numbers = ['1','2','3','4','5','6']
            randomnumber = (random.choice(numbers))
            speak(randomnumber)



        elif 'play the song' in query:
            query = query.replace('play the song','song')
            kit.playonyt(query)

        elif 'open akinator' in query:
            speak('welcome to Akinator i can read your mind')

            aki = akinator.Akinator()

            q = aki.start_game()

            while aki.progression <= 80:
                speak(q)
                a = myCommand()
               # a = input(q + "\n\t")
                if a == "b":
                    try:
                        q = aki.back()
                    except akinator.CantGoBackAnyFurther:
                        pass
                else:
                    q = aki.answer(a)
            aki.win()
            
            
            speak(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?{aki.first_guess['absolute_picture_path']}")
            correct = myCommand()
            #correct = input(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
            if correct.lower() == "yes" or correct.lower() == "y":
                speak('yaa')
                print("Yay\n")
            else:
                speak(oof)
                print("Oof\n")
            

        elif 'play music' in query :
            songs = ['//www.youtube.com/watch?v=BBAyRBTfsOU', 'https://www.youtube.com/watch?v=Pm77L5Loazc', 'https://www.youtube.com/watch?v=LPsyTf6EK5U','https://www.youtube.com/watch?v=kJQP7kiw5Fk']
            randomsong = (random.choice(songs))
            webbrowser.open(randomsong)
            speak('Okay sir')
            speak('Okay, here is your music! Enjoy!')




        else:
            speech(query)


        #speak('plese say the next command sir')