import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    task=''
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('listening...')
        audio = recognizer.listen(source)
    try:
        task = recognizer.recognize_google(audio, language="ru-RU").lower()
    except:
        pass
    return task

while True:
    print(listen())
