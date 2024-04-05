# file2.py
import tkinter as tk

class File2App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File 2 Window")

        # Create a button in the second file initially in disabled state
        self.button = tk.Button(self.root, text="Button in File 2", state=tk.DISABLED)
        self.button.pack()

    def enable_button(self):
        self.button.config(state=tk.NORMAL)  # Enable the button

if __name__ == "__main__":
    app = File2App()
    app.root.mainloop()
