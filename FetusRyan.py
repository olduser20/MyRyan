

# OK! Let's begin. Today is 2 June 2019. This is Saber

import speech_recognition as sr


# Get audio input (sample)

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio=r.listen(source)



