import customtkinter
from customtkinter import *
from PIL import Image,ImageTk

app= customtkinter.CTk()
app.geometry("1530x790")
set_appearance_mode("dark")

image=Image.open("login4.jpg")
image=ImageTk.PhotoImage(image,height=100,width=100)

image_label=customtkinter.CTkLabel(app,image=image)
image_label.place(x=0,y=0,relheight=1,relwidth=1)


frame=customtkinter.CTkFrame(app,width=500,height=550)
frame.place(relx=0.35,rely=0.25)



app.mainloop()