# file1.py
import tkinter as tk
import file2

class File1App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File 1 Window")

        # Create an instance of File2App from file2.py
        self.file2_app = file2.File2App()

        # Create a button in the first file
        self.button = tk.Button(self.root, text="Enable Second File Button", command=self.enable_button)
        self.button.pack()

    def enable_button(self):
        self.file2_app.enable_button()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = File1App()
    app.run()


