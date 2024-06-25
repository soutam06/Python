# import win32com.client as wicl

# speaker = wicl.Dispatch("SAPI.SpVoice") 
# names=["Soutam","samu","nirupon","soham","bikram"]

# for s in names:
#     speaker.Speak(f"Shout-out to {s}") 


from gtts import gTTS

import os

mytext = 'Congratulation Soutam!'

language = 'en'

myobj = gTTS(text=mytext, lang=language,slow=True)
myobj.save("greet_slow2.mp3")

# Playing the converted files
os.system("start greet_slow2.mp3")
