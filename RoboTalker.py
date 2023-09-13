import platform
import pyttsx3

if __name__ == '__main__':
    while True:
        x = input("Enter what you want to be spoken: ")
        print("Type 'q' to quit the program")

        if x == 'q':
            break

        if platform.system() == 'Windows':
            pyttsx3.speak(x)
        else:
            print("Text-to-speech is not supported on this platform")

