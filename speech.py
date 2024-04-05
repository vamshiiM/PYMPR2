import threading
import speech_recognition as sr
import tkinter as tk


def start_listening():
    global is_listening
    is_listening = True
    print("Listening...")

    # Start listening in a separate thread
    listener_thread = threading.Thread(target=listen_to_speech)
    listener_thread.start()


def stop_listening():
    global is_listening
    is_listening = False


def listen_to_speech():
    while is_listening:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            text_area.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


# Create Tkinter window
root = tk.Tk()
root.title("Speech to Text")

# Create text area
text_area = tk.Text(root)
text_area.pack()

# Create buttons
start_button = tk.Button(root, text="Start Listening", command=start_listening)
start_button.pack(side=tk.LEFT, padx=5, pady=5)

stop_button = tk.Button(root, text="Stop Listening", command=stop_listening)
stop_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Initialize SpeechRecognition
recognizer = sr.Recognizer()

# Variable to track if listening is active
is_listening = False

root.mainloop()


