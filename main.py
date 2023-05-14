import google_sheet
from tkinter import *
from tkinter import ttk
import time

# For Clear Screen (cmd) 
import os
os.system('cls')

# Making a Canva
master = Tk()

# Current time
CURRENT_TIME = time.ctime(time.time())

# All the games
game_options = ["Badminton", "Football", "Basketball","Table Tenis","Chess","Vollyball", "Cricket","Yoga"]

# Displaying NSO Attendence System (IIT BHILAI)
x = Label(master,text="NSO Attendence System (IIT BHILAI)",background="#D1DBBD",padx=20, pady=10)
x.pack()

# Displaying Time
TIME = Label(master)
TIME.pack()

# Updating time Function
def update_time():
    CURRENT_TIME = time.ctime(time.time())
    TIME.config(text=CURRENT_TIME)
    TIME.after(1000,update_time)

# Displaying Game
GAME_SELECTION = Label(master,text="GAME",padx=20,pady=10)
GAME_SELECTION.pack(side=TOP)
game_input = ttk.Combobox(master,values=game_options)
game_input.pack(side=TOP)

# Displaying player and input
PLAYER = Label(master,text="ID number")
PLAYER.pack()
player_input = Entry(master)
player_input.pack()

# Function on marking attendence
def mark_attendence():
    print(game_input.get()," ",player_input.get(), " ", type(player_input.get()))
    ROLL_NUMBER = google_sheet.hello(player_input.get())    
    name.config(text=f"Marked {ROLL_NUMBER}",fg="green")

# Attendence Mark button
mark_button = Button(master,text="Mark Attendence", padx=5,pady=2, command=mark_attendence)
mark_button.pack()

# Output the name after marking the attendence.
name = Label(text="")
name.pack()

update_time()
master.mainloop()