

# OK! Let's begin. Today is 2 June 2019. This is Saber.

import speech_recognition as sr
import openweather
from datetime import datetime
import requests, json


class Weather:
    @staticmethod
    def Message():
        print("This is Weather class.")

    @staticmethod
    def GetLocation():
        #strLocation=str(input("Please enter the location (country, city, town, ...): "))

        # Enter your API key here 
        api_key = "09835e32386d52ba64714d2e8bb04c67"
        
        # base_url variable to store url 
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        
        # Give city name 
        city_name = input("Enter city name : ") 
        
        # complete_url variable to store 
        # complete url address 
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
        
        # get method of requests module 
        # return response object 
        response = requests.get(complete_url) 
        
        # json method of response object  
        # convert json format data into 
        # python format data 
        x = response.json() 
        #print(x)
        
        # Now x contains list of nested dictionaries 
        # Check the value of "cod" key is equal to 
        # "404", means city is found otherwise, 
        # city is not found 
        if x["cod"] != "404": 
        
            # store the value of "main" 
            # key in variable y 
            y = x["main"] 
        
            # store the value corresponding 
            # to the "temp" key of y 
            current_temperature = y["temp"] 
        
            # store the value corresponding 
            # to the "pressure" key of y 
            current_pressure = y["pressure"] 
        
            # store the value corresponding 
            # to the "humidity" key of y 
            current_humidiy = y["humidity"] 
        
            # store the value of "weather" 
            # key in variable z 
            z = x["weather"] 
        
            # store the value corresponding  
            # to the "description" key at  
            # the 0th index of z 
            weather_description = z[0]["description"] 
        
            # print following values 
            print(" Temperature (in kelvin unit) = " +
                            str(current_temperature) + 
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                "\n description = " +
                            str(weather_description)) 
        elif x["cod"] == "401":
            print("API key has problems.")


        else: 
            print(" City Not Found ")
        

        



class StockMarket:
    @staticmethod
    def Message():
        print("This is StockMarket class.")



class RouteFinder:
    @staticmethod
    def Message():
        print("This is RouteFinder class.")



class News:
    @staticmethod
    def Message():
        print("This is News class.")


class Walkthrough:
    @staticmethod
    def SelectTask(command):
        if command=='weather' or command=='1':
            Weather.Message()
            Weather.GetLocation()
        elif command=='stock market' or command=='2':
            StockMarket.Message()
        elif command=='route finder' or command=='3':
            RouteFinder.Message()
        elif command=='news' or command=='4':
            News.Message()
        else:
            print("I don't know how to do it yet! :(")
            Walkthrough.TaskDone()

    @staticmethod
    def SelectTypingMode():
        strMode=input("Do you want to activate the typing mode [y/n]? ")
        if strMode=="y" or strMode=="Y":
            print("Typing mode activated.")
            Weather.Message()
        elif strMode=="n" or strMode=="N":
            print("Closing the program...")
        else:
            print("Wrong input!")


    @staticmethod
    def GetTypingCommand():
        print("Up until now, I can inform you about these things:\n")
        print("[1] Weather\n")
        print("[2] Stock Market\n")
        print("[3] Route Finder\n")
        print("[4] News\n")
        strCommand=str(input("Please select task: "))
        Walkthrough.SelectTask(strCommand)


    @staticmethod
    def TaskDone():
        strMsg=str(input("This task is done. Please enter 1 if you want to start over: "))        
        
        if strMsg=='again' or strMsg=='1':
            Walkthrough.GetTypingCommand()
        
        






# Get audio input (sample)
try:
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        audio=r.listen(source)

    # Using Sphinx
    # try:
    #     print("Sphinx thinks you said "+r.recognize_sphinx(audio))
    # except  sr.UnknownValueError:
    #     print("Sphinx could not understand audio")
    # except sr.RequestError as e:
    #     print("Sphinx error; {0}".format(e))


    # Using Google speech recognition
    try:
        command=r.recognize_google(audio)
        print("Google Speech Recognition thinks you said "+command)
    except  sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    Walkthrough.SelectTask(command)


except OSError:
    print("No microphone device is detected!")
    Walkthrough.SelectTypingMode()
    Walkthrough.GetTypingCommand()


    






