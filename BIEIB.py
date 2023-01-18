import os
import random
import pyjokes
import speech_recognition as sr
import pyttsx3
import datetime as dt
import wikipedia
import webbrowser as wb
import pywhatkit
import math

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',187)
engine.setProperty('voice',voices[2].id)


def wishme():
    current_hour = dt.datetime.now().hour
    if current_hour >= 4 and current_hour < 12:
        speak("Good Morning ," + name() + "How may I help you today?")
    elif current_hour >= 12 and current_hour < 15:
        speak("Good afternoon ," + name() + "I'm at your service")
    elif current_hour >= 15 and current_hour <= 22:
        speak("Good evening ," + name() + "How may I help you?")
    else:
        speak("How may I help you?")


def take_command():
    r = sr.Recognizer()
    mic = sr.Microphone()
    query = ''
    with mic as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("You said : " + query)
    except:
        speak("Say it again...")
        take_command()
    return query


def speak(arg):
    engine.say(arg)
    engine.runAndWait()


def name():
    speak("What should I call you?")
    return take_command()


def open(command):
    if 'google' in command:
        wb.open('google.com')
    elif 'youtube' in command:
        wb.open('youtube.com')
    elif 'netflix' in command:
        wb.open('netflix.com')
    elif 'amazon' in command:
        wb.open('amazon.in')
    elif 'prime video' in command:
        wb.open("primevideo.in")
    elif 'gmail' in command:
        wb.open('gmail.com')
    else:
        print("Sorry , Currently that's beyond my ability")
        speak("Sorry , Currently that's beyond my ability")


def wiki(arg):
    result = wikipedia.summary(arg, sentences=2)
    print(result)
    speak(result)


def mathematics(arg):
    if 'add' in arg:
        arg = arg.replace('add', '')
        lst = arg.split('and')
        num1 = float(lst[0])
        num2 = float(lst[1])
        print("Sum of {0} and {1} is {2}".format(num1, num2, num1 + num2))
        speak("Sum of {0} and {1} is {2}".format(num1, num2, num1 + num2))
    elif 'subtract' in arg:
        arg = arg.replace('subtract', '')
        lst = arg.split('from')
        num1 = float(lst[1])
        num2 = float(lst[0])
        print("Subtraction of {1} from {0} is {2}".format(num1, num2, num1 - num2))
        speak("Subtraction of {1} from {0} is {2}".format(num1, num2, num1 - num2))
    elif 'multiply' in arg:
        arg = arg.replace('multiply', '')
        lst = arg.split('and')
        num1 = float(lst[0])
        num2 = float(lst[1])
        res = num1 * num2
        print("Multiplication of {0} and {1} is {2}".format(num1, num2, res))
        speak("Multiplication of {0} and {1} is {2}".format(num1, num2, res))
    elif 'divide' in arg:
        arg = arg.replace('divide', '')
        lst = arg.split('by')
        num1 = float(lst[0])
        num2 = float(lst[1])
        res = round((num1 / num2), 2)
        print("Division of {0} and {1} is {2}".format(num1, num2, res))
        speak("Division of {0} and {1} is {2}".format(num1, num2, res))
    elif 'square root of' in arg:
        arg = arg.replace('square root of', '')
        num = int(arg)
        res = round(math.sqrt(num), 2)
        print("Square root of {0} is {1}".format(num, res))
        speak("Square root of {0} is {1}".format(num, res))
    elif 'power' in arg:
        arg = arg.split('power')
        num1 = float(arg[0])
        num2 = float(arg[1])
        res = round(num1 ** num2, 2)
        print("{0} to the power of {1} is {2}".format(num1, num2, res))
        speak("{0} to the power of {1} is {2}".format(num1, num2, res))


def fun_stuff(arg):
    if 'f*** you' in arg:
        print("It would be better if you mind your language...")
        speak("It would be better if you mind your language...")
    elif 'i love you' in arg:
        print("So sweet of you , I love you too....but as a friend")
        speak("So sweet of you , I love you too....but as a friend")
    elif 'i hate you' in arg:
        print("Never mind")
        speak("Never mind")
    elif 'who are you' in arg:
        print("I am Friday , your personal assistant")
        speak("I am Friday , your personal assistant")
    elif 'how are you' in arg:
        print("I am fine , thanks for asking...Hope you are doing good too")
        speak("I am fine , thanks for asking...Hope you are doing good too")


if __name__ == '__main__':
    fun_lst = ['f*** you', 'i love you', 'i hate you', 'how are you', 'who are you']
    wishme()
    while True:
        command = take_command().lower()
        if command in fun_lst:
            fun_stuff(command)
        elif 'who' in command or 'what' in command:
            if 'who' in command:
                command = command.replace('who', '')
            if 'what' in command:
                command = command.replace('what', '')
            wiki(command)
        elif 'open' in command:
            command = command.replace('open', '')
            open(command)
        elif 'date' in command:
            res = dt.datetime.now().strftime('%x')
            print(res)
            speak(res)
        elif 'current time' in command:
            res = dt.datetime.now().strftime('%X')
            print(res)
            speak(res)
        elif 'add' in command or 'subtract' in command or 'multiply' in command or 'divide' in command or 'square root of' in command or 'power' in command:
            mathematics(command)
        elif 'play' in command:
            command = command.replace('play', '')
            pywhatkit.playonyt(command)
        elif 'joke' in command:
            res = pyjokes.get_joke()
            print(res)
            speak(res)
        elif 'break' in command or 'exit' in command or 'stop' in command or 'bye' in command:
            speak("See you again")
            break

engine.runAndWait()
