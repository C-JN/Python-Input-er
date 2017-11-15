
from tkinter import Tk, Label, Text, Button, mainloop #Imports items listed. This allows them to be used.
root=Tk()
root.title("Inuter")#"" Defines name at the top of window./
root.configure(background="#F0F0F0")
def retrieve_input():

    inputValue=textBox.get("1.0","end-1c") #This is controlling the text box
    print(inputValue)
userAsk=Label(root, text="Typer 2.0")
userAsk.pack()
textBox=Text(root, height=6, width=30) #This adds a textbox with desired dimensions.
textBox.pack()
buttonCommit=Button(root, height=1, width=20, text="Enter", #This is the box size this changes how it looks still movable by dragging
                    command=lambda: retrieve_input())
buttonCommit.pack()

#controls
mainloop()
