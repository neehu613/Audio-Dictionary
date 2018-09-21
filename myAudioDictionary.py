from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import pyttsx3
import re

def womanAudio(string):
    engine.say(string)
    engine.runAndWait()

engine = pyttsx3.init()
#engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')	works with windows only

x=1

while x == 1:
    womanAudio("Enter a word to search its meaning")
    word = input("Enter a word to search its meaning: ")
    womanAudio("The entered word is ")
    womanAudio(word)
    synonyms = wordnet.synsets(word)
    if synonyms == []:
        print("Nothing in the dictionary")
        womanAudio("I don't know what that means...I'm sorry!")
        continue
    womanAudio("The following are the various synonyms of " + word)
    count = 1

    for i in synonyms:
        print(i)
        womanAudio(count)
        word1 = re.findall(r"'[a-z]*", str(i))
        womanAudio(word1)
        womanAudio("Definition")
        print(i.definition())
        womanAudio(i.definition())
        womanAudio("Examples")
        if i.examples() == []:
            print("No examples, sorry")
            womanAudio("Oops, my dictionary has no example sentences for that word")
        else:
            print(i.examples())
            womanAudio(i.examples())
        
        print('\n\n')
        womanAudio("Do you want more meanings of the word ")
        womanAudio(word)
        
        print("Do you want more meanings?")
        choice = input("Enter 'Y' or 'N': ")

        if choice == 'Y' or choice == 'y':
            count+=1
        elif choice == 'N' or choice == 'n':
            break
        else:
            print("Invalid choice")

    womanAudio("Wanna continue with another word? Press ENTER to do so. Or go ahead and type Q U I T")
    terminate = input("Enter 'QUIT' to terminate the program\n")
    if terminate == "QUIT" or terminate == "quit":
        engine.say("Thank you for using Shahid Nehal's Audio Dictionary")
        engine.runAndWait()
        break
    else:
        continue
