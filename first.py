import customtkinter
import tkinter
from tkinter import*
from customtkinter import *
from PIL import *

app = customtkinter.CTk() # ctk is variable
customtkinter.set_appearance_mode("system")# for dark and light mode
customtkinter.set_default_color_theme("green")
app.geometry("1000x1000")

def button_function():   # task function for the button
    print("FUCK OFF")

    button3.place(relx=0.6, rely=0.6)


button = customtkinter.CTkButton(master = app,text="click me",command = button_function)
button.place(relx=0.2 , rely=0.5 , anchor = tkinter.CENTER)

button1 = customtkinter.CTkButton(master = app,text="click me 1",command = button_function)
button1.place(relx=0.2 , rely=0.6 , anchor = tkinter.CENTER)

button2 = customtkinter.CTkButton(master = app,text="click me 2",command = button_function)
button2.place(relx=0.2 , rely=0.7 , anchor = tkinter.CENTER)

# creating frames
frame = customtkinter.CTkFrame( master=app,width=100,height=100,corner_radius=20,bg_color="yellow")
frame.pack(padx = 20 ,pady=20)
# frame.place(relx=0.5,rely=0.5)

#CREATING TABVIEW
tabView =customtkinter.CTkTabview(master=app,width=100,height=100)
tabView.place(relx=0.5,rely=0.5,anchor = tkinter.CENTER)
tabView.add("tab1")
tabView.add("tab2")

tabView.set("tab1")

button3 = customtkinter.CTkButton(master = app,text="click me 2",command = button_function,width=50,height=50)
button3.place(relx=0.5, rely=0.5 )

"""
# creating textbox

textbox = customtkinter.CTkTextbox(app,height=200,width=100)
textbox.place(relx=0.2, rely=0.2,)
text = ""
           
    
textbox.insert("0.0",text)
textbox.configure(state="normal")# in configure function you can use to normal or disable in textbox
#disabled means you cannot update the textbox

def work():
    print(textbox.get("0.0","end")) # Due to this the text will  appear on console screen entered by user


button4= customtkinter.CTkButton(master = app,text="butt",command=work )
button4.place(relx=0.1,rely=0.1,anchor=tkinter.CENTER)


#creating sroll bar to the textbox object
frame2 = customtkinter.CTkFrame(master=app,width=200,height=200,corner_radius=20)
frame2.pack(padx=20,pady=20)
tk_textbox = tkinter.Text(frame2,highlightthickness=0)
tk_textbox.grid(row=0,column=0,sticky="nsew")
ctk_textbox_scrollbar = customtkinter.CTkScrollbar(frame2,command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0,column=1,sticky="ns")

tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set) #due to this command the scroll bar will be synchronised with textbox object

def event():
 print(tk_textbox.get("0.0","end")) # this will show the string in console
 textbox_text=tk_textbox.get("0.0","end")# due to this the string is copied into the textbox_text
 my_string_var.set(str(textbox_text))# this is used to print it in the label

button5=customtkinter.CTkButton(master=frame2,text="b4",command=event)
button5.place(relx=0.8,rely=0.9,anchor=tkinter.CENTER)

my_string_var = StringVar()


# CREATING A LABEL OBJECT
#USING LABEL OBJECT
label  =customtkinter.CTkLabel(master=frame2,
                               #text="LABEL",# this will be the name of the label
                               textvariable= my_string_var,
                                width=150,
                                height=30,
                                 fg_color=("white","gray57"),
                                corner_radius=8)
label.grid(padx=20,pady=10)

"""













app.title("TEACHER PAGE")
app.mainloop()