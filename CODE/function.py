from imports import *


def say_stuff(whattosay, slow_tof):
    gts = gTTS(text=whattosay, lang='en', slow=slow_tof)
    gts.save("StuffToSayTEMP.mp3")
    playsound("StuffToSayTEMP.mp3")
    if os.path.exists("StuffToSayTEMP.mp3"):
        os.remove("StuffToSayTEMP.mp3")
