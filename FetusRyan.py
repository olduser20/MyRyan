

# OK! Let's begin. Today is 2 June 2019. This is Saber.

import speech_recognition as sr
import openweather
from datetime import datetime
import requests, json
import pyttsx3
import math
import iexfinance


import matplotlib.pyplot as plt
from datetime import datetime


##### API KEYS #####

stock_api_key='sk_1dd5739d86f64fc387146df87ab22837'
weather_api_key = "2a7e2e367325658696e865497fd6aaea"



class Weather:
    @staticmethod
    def Message():
        print("This is Weather class.")
        # Speech.ReadText("This is weather class.")

    @staticmethod
    def GetLocation():
        #strLocation=str(input("Please enter the location (country, city, town, ...): "))

        
        
        # base_url variable to store url 
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        
        # Give city name 
        city_name = input("Enter city name : ") 
        
        # complete_url variable to store 
        # complete url address 
        complete_url = base_url + "appid=" + weather_api_key + "&q=" + city_name 
        # print(complete_url)
        
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
            
            # store the value of "sys" 
            # key in variable s 
            s = x["sys"] 

            # store the value corresponding 
            # to the "country" key of s 
            country = s["country"] 

            # store the value of "main" 
            # key in variable y 
            y = x["main"]             
        
            # store the value corresponding 
            # to the "temp" key of y 
            current_temperature = int(y["temp"]-273.15)  
        
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

            # engine = pyttsx3.init()
            # engine.say("This is the weather condition for {0}".format(city_name))
            # engine.runAndWait()
        
            # print following values
            print(" Country = " +
                            str(country) +
                "\n Temperature (in Celsius unit) = " +
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
            Weather.GetLocation()
        

        # Walkthrough.TaskDone()




class StockMarket:

    

    @staticmethod
    def Message():
        print("This is StockMarket class.")
        
    @staticmethod
    def plotHistoricalData():

        from iexfinance.stocks import get_historical_data

        start=datetime(2018,1,1)
        end=datetime.today()
        

        symbol=input("Reporting Historical Data; Enter symbol: ")
        try:
            df=get_historical_data(symbol,start,end,output_format='pandas',token=stock_api_key)

            df.plot()
            plt.show()

        except:
            print("Symbol not found!")


    @staticmethod
    def getBalanceSheet():
        from iexfinance.stocks import Stock

        symbol=input("Reporting Balance Sheet; Enter symbol: ")

        try:
            stck=Stock(symbol,output_format='pandas',token=stock_api_key)
            print(stck.get_balance_sheet())
            
        except:
            print("Symbol not found!")


     



    @staticmethod
    def getIncomeStatement():
        from iexfinance.stocks import Stock

        symbol=input("Reprting Income Statement; Enter symbol: ")

        try:
            stck=Stock(symbol,output_format='pandas',token=stock_api_key)
            print(stck.get_income_statement())
            
        except:
            print("Symbol not found!")



    @staticmethod
    def getCashFlow():
        print(1)




    @staticmethod
    def SymbolForecasting():
        print(1)



class RouteFinder:
    @staticmethod
    def Message():
        print("This is RouteFinder class.")



class News:
    @staticmethod
    def Message():
        print("This is News class.")


class Flights:
    @staticmethod
    def Message():
        print("This is Flights class.")


class Speech:
    @staticmethod
    def ReadText(text):
        print("Wait please...")


class Walkthrough:
    @staticmethod
    def SelectTask(command):
        if command=='weather' or command=='1':
            Weather.Message()
            Weather.GetLocation()

            Walkthrough.TaskDone()

        elif command=='stock market' or command=='2':
            StockMarket.Message()
            StockMarket.plotHistoricalData()
            #StockMarket.getBalanceSheet()
            # StockMarket.getIncomeStatement()
            Walkthrough.TaskDone()

        elif command=='route finder' or command=='3':
            RouteFinder.Message()
            Walkthrough.TaskDone()

        elif command=='news' or command=='4':
            News.Message()
            Walkthrough.TaskDone()

        elif command=='flights' or command=='5':
            Flights.Message()
            Walkthrough.TaskDone()

        else:
            print("I don't know how to do it yet! :(")
            Walkthrough.TaskDone()

    @staticmethod
    def SelectTypingMode():
        strMode=input("Do you want to activate the typing mode [y/n]? ")
        if strMode=="y" or strMode=="Y":
            print("Typing mode activated.")
            Walkthrough.GetTypingCommand()
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
        print("[5] Flights\n")
        strCommand=str(input("Please select task: "))
        Walkthrough.SelectTask(strCommand)


    @staticmethod
    def TaskDone():
        strMsg=str(input("This task is done. Please enter 1 if you want to start over: "))
        
        if strMsg=='again' or strMsg=='1':
            Walkthrough.GetTypingCommand()
        
        


# Get audio input (sample)
try:
    # engine = pyttsx3.init()
    # engine.say("This is Ryan.")
    # engine.runAndWait()


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
        Walkthrough.SelectTask(command)
    except  sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    


except OSError:
    print("No microphone device is detected!")
    # engine = pyttsx3.init()
    # engine.say("This is Ryan.")
    # engine.runAndWait()
    Walkthrough.SelectTypingMode()
    



    






