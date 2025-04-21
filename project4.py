import speech_recognition as sr  # it reconginise the what we said

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Tell me your dream...")
    audio = r.listen(source)

try:
    dream_text = r.recognize_google(audio)
    print("You said:", dream_text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand.")
except sr.RequestError:
    print("Speech recognition service is down.")