

# OK! Let's begin. Today is 2 June 2019. This is Saber

import speech_recognition as sr


class Weather:
    def Message():
        print("This is Weather class.")



class StockMarket:
    def Message():
        print("This is StockMarket class.")



class RouteFinder:
    def Message():
        print("This is RouteFinder class.")



class News:
    def Message():
        print("This is News class.")

    




# Get audio input (sample)

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

if (command=="weather"):
    print("Call the Weather class.")
elif (command=="stock market"):
    print("Call the StockMarket class.")

