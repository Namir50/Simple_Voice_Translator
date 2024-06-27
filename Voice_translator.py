import googletrans
import speech_recognition
import gtts
import playsound

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print(googletrans.LANGUAGES)
    lan = input("Enter language code to convert: ")
    print("Speak Now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice)
    print(text)
    
translator = googletrans.Translator()
translation = translator.translate(text, dest = lan)
print("Translation: ",translation.text)
sound = gtts.gTTS(translation.text)
sound.save("translation.mp3")
playsound.playsound("translation.mp3")