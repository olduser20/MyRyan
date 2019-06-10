

# OK! Let's begin. Today is 2 June 2019. This is Saber

import speech_recognition as sr


class Weather:
    @staticmethod
    def Message():
        print("This is Weather class.")



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


class Walkthorough:
    @staticmethod
    def SelectTask(command):
        if command==('weather'):
            Weather.Message()
        elif command==('stock market'):
            StockMarket.Message()
        elif command==('route finder'):
            RouteFinder.Message()
        elif command==('news'):
            News.Message()
        else:
            print("I don't know how to do it yet! :(")

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

    Walkthorough.SelectTask(command)


except OSError:
    print("No microphone device is detected!")
    Walkthorough.SelectTypingMode()

    






