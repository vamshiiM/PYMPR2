# creating a login page

import customtkinter,tkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("500x500")
app.title("FUCK OFF")

frame = customtkinter.CTkFrame(master=app,width=350,height=500,bg_color="green",fg_color="white",corner_radius=10)
frame.pack(padx=20,pady=20)

user_id_entry = customtkinter.CTkEntry(master=frame,placeholder_text="ENTER YOUR NAME",width=150,height=30,border_width=2,corner_radius=10)
user_id_entry.place(relx=0.5 , rely=0.2,anchor=tkinter.CENTER)

user_id_password = customtkinter.CTkEntry(master=frame,placeholder_text="ENTER YOUR PASSWORD",width=150,height=30,border_width=2,show="*",corner_radius=10)
user_id_password.place(relx=0.5 , rely=0.4,anchor=tkinter.CENTER)

user_id="vamshi"
password="12345"
text_var=StringVar()
text_var2=StringVar()
text_var3=StringVar(value="")
def event():

    if(user_id_entry.get()==user_id) and (user_id_password.get()==password):
        text_var2.set("CONNECTED")
    else:
        text_var2.set("NOPE")

    name= str(user_id_entry.get())
    p=str(user_id_password.get())
    gender=str(gender_combobox.get())
    text_var.set(f"Name:{name}\n Password:{p}\n GENDER:{gender}")

button = customtkinter.CTkButton(master=frame,height=30,width=100,text="SUBMIT",command=event)
button.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(text="hiii",textvariable=text_var2,master=frame,width=120,height=25,fg_color=("white","gray"),corner_radius=8)
label.place(relx=0.5 , rely=0.75,anchor=tkinter.CENTER)

label2 = customtkinter.CTkLabel(text="hllo", textvariable=text_var ,master=frame,width=120,height=25,fg_color=("white","gray"),corner_radius=8)
label2.place(relx=0.5 , rely=0.85,anchor=tkinter.CENTER)


#adding combobox
optionmenu_var = customtkinter.StringVar(value="GENDER")

gender_combobox = customtkinter.CTkComboBox(master=frame,values=["male","female"],variable=optionmenu_var)
gender_combobox.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

#ADDING SEGMENTED BUTTONS #this is used for showing different
def seg_button(value):
    text_var3.set("")
    if value == "NAME":
      text_var3.set(f"NAME:{user_id_entry.get()}")
    if value =="PASSWORD":
      text_var3.set(f"PASSWORD:{user_id_password.get()}")

segmented_button = customtkinter.CTkSegmentedButton(master=frame,
                                                    values=["NAME","PASSWORD"],
                                                    command = seg_button)
segmented_button.place(relx=0.27,rely=0.9)
segmented_button.set("NAME")
label3 = customtkinter.CTkLabel(text="hllo", textvariable=text_var3 ,master=frame,width=120,height=25,fg_color=("white","gray"),corner_radius=8)
label3.place(relx=0.5 , rely=0.99,anchor=tkinter.CENTER)

#creating a switch
swi_var_1 = customtkinter.StringVar(value="ON")
swi_var_2=customtkinter.StringVar(value="OFF")

def switch_event():
    if swi_var_1.get()=='on':
        customtkinter.set_appearance_mode("light")
    else :
        customtkinter.set_appearance_mode("dark")
    # if swi_var_1.get() == 'off' and swi_var_2.get() == 'on':
    #     customtkinter.set_appearance_mode("dark")


swi_1=customtkinter.CTkSwitch(master=frame,text="SWITCH APP MODE",command=switch_event,variable=swi_var_1,onvalue="on",offvalue="off")
swi_1.place(relx=0.5,rely=0.1)
swi_2=customtkinter.CTkSwitch(master=frame,text="LOCK",command=switch_event,variable=swi_var_2,onvalue="on",offvalue="off")
swi_2.place(relx=0.5,rely=0.3)



app.mainloop()

