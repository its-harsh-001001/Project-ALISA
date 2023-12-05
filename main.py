import pyttsx3
import os
import speech_recognition as sr
# from googletrans import Translator
import datetime
from time import sleep
import pyautogui
import keyboard
import requests
import openai


def introduction():
    print("My name is alisa and I am a virtual assistant")
    speak_eng("My name is alisa and I am a virtual assistant")
    
def ai_chat(prompt):
    openai.api_key = "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"

    response = openai.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": f"{prompt}"}
    ]
    )

    temp = response.choices[0].message.content
    temp_index = temp.find(":")
    message = temp[temp_index+3:-2]
    print(message)
    speak_eng(message)
    return message


def ai_query(query):
    openai.api_key = "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"

    response = openai.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": f"{query}"}
    ]
    )

    temp = response.choices[0].message.content
    temp_index = temp.find(":")
    message = temp[temp_index+3:-2]
    return message


def greet():
    print("Hi there! ")
    speak_eng("hi there")
    print("I am Alisa, your personal assistant. ")
    speak_eng("I am Alisa, your personal assistant")
    print("How can I assist you today sir?")
    speak_eng("how can I assist you today sir")


def speak_eng(text):
    engine1 = pyttsx3.init()
    voices = engine1.getProperty("voices")
    engine1.setProperty("voice", voices[1].id)
    engine1.setProperty("rate", 180)
    engine1.say(text)
    engine1.runAndWait()


# def speak_hin(text):
#     engine2 = pyttsx3.init()
#     voices = engine2.getProperty('voices')
#     engine2.setProperty('voice', voices[2].id)
#     engine2.setProperty('rate', 180)
#     engine2.say(text)
#     engine2.runAndWait()

# def translate(query):

#     t = Translator()
#     initial_text = query.lower()
#     from_lang = 'hi'
#     to_lang = 'en'


#     text_to_translate = t.translate(initial_text,src=from_lang,dest=to_lang)
#     text = text_to_translate.text
#     return text


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            return "Some Error Occurred."


def Whatsapp_auto_message(name, message):
    app_opener("Brave")
    sleep(2)
    keyboard.write("https://web.whatsapp.com/")
    sleep(0.5)
    keyboard.press("enter")
    sleep(10)
    pyautogui.click(209, 253)
    sleep(0.5)
    keyboard.write(name)
    sleep(1)
    pyautogui.click(248, 403)
    sleep(1)
    keyboard.write(message)
    sleep(1)
    keyboard.press("enter")
    sleep(1)
    keyboard.press_and_release("alt+F4")
    sleep(0.5)
    keyboard.press_and_release("alt+tab")
    print("Message sent sir")
    speak_eng("message sent sir")


def music_player(song_name):
    song_url = f"https://www.youtube.com/results?search_query={song_name}"
    app_opener("Brave")
    sleep(5)
    keyboard.write(song_url)
    sleep(0.5)
    keyboard.press('enter')
    sleep(4)
    pyautogui.click(x=1161, y=332)
    sleep(5)
    keyboard.press("f")


def app_opener(app_name):
    pyautogui.press('win')
    sleep(1)
    keyboard.write(app_name)
    sleep(0.5)
    keyboard.press("enter")

# def weather(input_city):
#     api_key = "1c1ee454d5c69a85ee8cf890348e149a"
#     city = input_city
#     weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
#     if weather_data.json()["cod"] == "404":
#         print("Please tell correct city name ")
#         speak_eng("please tell correct city name")
#     else:
#         weather_status = weather_data.json()["weather"][0]["description"]
#         weather_temp = weather_data.json()["main"]["temp"]
#         print(
#             f"The weather at {city} is {weather_status} with temperature of {weather_temp} sir"
#         )
#         speak_eng(
#             f"The weather at {city} is {weather_status} with temperature of {weather_temp} sir"
#         )


def auto_photo_taker():
    app_opener("Camera")
    sleep(5)
    print("Here you go sir\nSay Cheese!!")
    speak_eng("Here you go sir, say Cheese")
    pyautogui.click(x=1862, y=525)
    sleep(5)
    print("Here take a look")
    speak_eng("here take a look")
    pyautogui.click(x=1862, y=949)


if __name__ == "__main__":

    Websites = [
            ["Youtube", "https://youtube.com/"],
            ["Google", "https://www.google.com/"],
            ["Whatsapp", "https://web.whatsapp.com/"],
            ["Github", "https://github.com/"],
            ["gmail", "https://mail.google.com/mail/u/0/#inbox"],
            ["Bard", "https://bard.google.com/"],
            ["AI", "https://chat.openai.com/"],
        ]
    
    App_list = [
            "Google chrome",
            "WPS office",
            "visual studio code",
            "snipping tool",
            "notepad",
            "Camera",
            "terminal",
            "calculator",
            "recorder",
            "brave",
            "android studio",
            "edge",
            "clock",
            "arduino",
            "file explorer",
            "photos",
            "recycle bin",
            "settings",
        ]
    
    with open("D:\PROJECTS\Project- ALISA\Test 1.gif", "r") as gif:
        os.startfile("D:\PROJECTS\Project- ALISA\Test 1.gif")
        sleep(0.5)
        keyboard.press("F11")

    loop_iteration = 0

    while True:
        if loop_iteration == 0:
            loop_iteration = 1
            greet()

        else:
            print("Is there any thing I can help you with sir?")
            speak_eng("Is there any thing I can help you with sir")

        command = takeCommand()
        print(command)

        for app in App_list:
            if f"Open {app}".lower() in command.lower():
                print(f"Opening {app} sir...")
                speak_eng(f"opening {app} sir")
                app_opener(app_name=app)
                break

        for website in Websites:
            if f"Open {website[0]}".lower() in command.lower():
                print(f"Opening {website[0]} Sir...")
                speak_eng(f"opening {website[0]} sir")
                app_opener("Brave")
                sleep(2)
                keyboard.write(website[1])
                sleep(0.5)
                keyboard.press("")
                break

        Contacts = ["Mummy", "Dad", "Mam"]

        for contact in Contacts:
            if f"Message {contact}".lower() in command.lower():
                print("What message do you want to send?")
                speak_eng("what message do you want to send")
                message = str(takeCommand())
                print("Sending your message sir...")
                speak_eng("Sending your message sir")
                Whatsapp_auto_message(name=contact, message=message)
                continue


        if "No".lower() in command.lower():
            print("Ok Sir\nCall me anytime you need me")
            speak_eng("Ok Sir call me anytime you need me")
            sleep(1)
            keyboard.press_and_release("alt+F4")
            break
        
        elif "Play".lower() in command.lower():
            split_index = command.lower().find("play") + len("play")
            music_name = command[split_index:].lower().strip()
            print(f"Playing {music_name} on youtube sir")
            speak_eng(f"Playing {music_name} on youtube sir")
            music_player(music_name)
            break

        # elif ("What is the weather in".lower() or "What is weather in".lower() in command.lower()):
        #     split_index = command.lower().find("in") + len("in")
        #     city_name = command[split_index:].lower().strip()
        #     weather(city_name)
        #     continue

        elif "Take a photo".lower() in command.lower():
            auto_photo_taker()

        elif "What is the time".lower() in command.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the current time is {current_time}")
            speak_eng(f"Sir the time is {current_time}")

        elif "Chat with me".lower() in command.lower():
            chat_mode = 1
            while chat_mode == 1:
                chat_time = 1
                if chat_time == 1:
                    print("Ok, What do you want to talk about?")
                    speak_eng("Ok, what do you want to talk about")
                    topic = takeCommand()
                    chat = ai_chat(topic)
                    with open("D:\PROJECTS\Project- ALISA\chat_history.txt","a") as chat_history:
                        chat_history.write("Ok, What do you want to talk about? \n"+topic+chat)
                    chat_time = 2
                    continue
                else:
                    user_input = takeCommand()
                    if "stop chat".lower() in user_input():
                        chat_mode = 0
                        break
                    else:
                        chat = ai_chat(user_input)
                        with open("D:\PROJECTS\Project- ALISA\chat_history.txt","a") as chat_history:
                            chat_history.write("\n"+user_input+chat)


        elif "Using artificial intelligence".lower() in command.lower():
            answer = ai_query(query=command)
            print("Ok sir I have done that and stored the result")
            speak_eng("Ok sir I have done that and stored the result")
            print("Would you like to take a look?")
            speak_eng("Would you like to take a look?")
            choice = takeCommand()
            print(choice)
            if "Yes".lower() in command.lower():
                with open("D:\PROJECTS\Project- ALISA\openai_answer.txt","a") as answers:
                    answers.write("\n"+command+"\n"+answer)
                os.startfile("D:\PROJECTS\Project- ALISA\openai_answer.txt")
                sleep(0.5)
                keyboard.press_and_release("win+UP_Arrow")
                break
            elif "No".lower() in command.lower():
                print("Ok Sir")
                speak_eng("Ok Sir")
                continue

        else:
            print("Sorry I didnot get that")
            speak_eng("Sorry I didnot get that")
