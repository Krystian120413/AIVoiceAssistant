import speech_recognition
import pyttsx3 as tts

recognizer = speech_recognition.Recognizer()

speaker = tts.init()

# speaker.setProperty('voice', speaker.getProperty('voices')[1].id)
speaker.setProperty('rate', 150)


def speak(text):
    speaker.say(text)
    speaker.runAndWait()


def ifInclude(string, words):
    return [element for element in words if element in string.lower()]


'''
    for element in words:
        if element in string.lower():
            list.append(element)
'''

FIND_GREETING = ['witaj', 'dzień dobry', 'dobry wieczór', 'cześć']
answer_Greeting = 'Cześć!'
FIND_WHO = ['kim jesteś', 'jak się nazywasz']
answer_Who = 'Nie jestem prawdziwy, ale możemy porozmawiać'

FIND = [FIND_GREETING, FIND_WHO]
answers = [answer_Greeting, answer_Who]

while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Nasluchuje...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio, language='pl-PL')
            text = text.lower()

            print(f"Rozpoznano: {text}")
            if len(ifInclude(text, FIND_GREETING)):
                print(answer_Greeting)
                speak(answer_Greeting)
            elif len(ifInclude(text, FIND_WHO)):
                print(answer_Who)
                speak(answer_Who)
            elif len(ifInclude(text, ["zakończ"])):
                print("Do zobaczenia")
                speak("Do zobaczenia")
                break
            else:
                print("Przykro mi, ale nie mogę odpowiedzieć na to pytanie.")
                speak("Przykro mi, ale nie mogę odpowiedzieć na to pytanie.")

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
