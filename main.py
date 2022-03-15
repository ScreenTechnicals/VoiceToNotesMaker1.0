import speech_recognition as sr

# empty string
note = ""

# Functions
def takeNotes():
    '''It takes microphone input from the user and returns a string output'''

    global note
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recogniser.pause_threshold = 1
        audio = recogniser.listen(source)

        try:
            print("Recognizing...")
            note = recogniser.recognize_google(audio, language="en-in")
            # print(note)
        except Exception as e:
            print(e)

def writeNotes():
    '''Writing the notee in the text file'''

    global note
    with open("notes.txt", "a+") as file:
        file.writelines(note)
        file.writelines("\n")
        print("Notes written !")


if __name__ == '__main__':
    takeNotes()
    writeNotes()

    while True:
        ask = input("Do you want to take more inputs?[y/N]: ")
        if ask == "y":
            takeNotes()
            writeNotes()
        if ask == "N":
            print("Thanks For using us !")
            break
