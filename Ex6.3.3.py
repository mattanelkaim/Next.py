import pyttsx3
# import gtts

# Approach 1: Offline
my_str = "first time i'm using a package in next.py course"

engine = pyttsx3.init()
engine.say(my_str)
engine.runAndWait()

# Approach 2: Online (using API to create a file)
# file_name = "test.mp3"  # To create
#
# tts = gtts.gTTS(my_str)
# tts.save(file_name)
