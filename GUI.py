from tkinter import* #library use for GUI
from PIL import Image, ImageTk  #this modul(pillow) helps to use png/jpg image in our program
import speech_to_text
import action

root = Tk() #root variable
root.title("AI Desktop Assistant")  #set the title of project
root.geometry("750x700")    #set the default size of the GUI
root.resizable(False,False) #make the GUI unresizable
root.config(bg="#6F8FAF")   #set the background color of GUI


#implementing the ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.tasks(user_val)
    text.insert(END, "User --->"+user_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT <---"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()


#implementing the send function
def send():
    send = entry.get()
    bot = action.tasks(send)
    text.insert(END, "User ---> " +send+"\n")
    if bot != None:
        text.insert(END, "BOT <--- " +str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()


#implementing the delete function
def del_text():
    text.delete('1.0',"end")

#Root-frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=7, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=80, pady=20)

#text-lable frame
text_label=Label(frame, text="AI Assistant", font=("comic Sans ms", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

#image on frame 
image = ImageTk.PhotoImage(Image.open("image/assistant.jpg"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

#adding a text widget
text = Text(root, font = ('courier 10 bold'), bg="#356696")
text.grid(row=2, column=0)
text.place(x=180, y=445, width=375, height=100) #text.place(location,size)

#entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=190, y=550, width=350, height=30) #entry.place(location,size)

#button 1
Button1 = Button(root, text="ASK", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=160, y=600)

#button 2
Button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=310, y=600)

#button 3
Button3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=460, y=600)


root.mainloop()
