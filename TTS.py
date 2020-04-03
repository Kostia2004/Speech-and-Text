import speech

def talk(words):
    speech.say(words)

while True:
    s = input()
    talk(s) 
