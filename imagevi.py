from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Geography Flash Card")
root.geometry("500x600")
root.resizable(0,0)


#OPENING AND THEN RESIZING THE IMAGE AND THEN STOTRING IT AS PHOTO IMAGE
my_image0=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Geography Flash Card App\\Images\\boston.png")
my_image0=my_image0.resize((320,320),Image.ANTIALIAS)
my_image0=ImageTk.PhotoImage(my_image0)

my_image1=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Geography Flash Card App\\Images\\florida.png")
my_image1=my_image1.resize((320,320),Image.ANTIALIAS)
my_image1=ImageTk.PhotoImage(my_image1)

my_image2=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Geography Flash Card App\\Images\\nevada.png")
my_image2=my_image2.resize((320,320),Image.ANTIALIAS)
my_image2=ImageTk.PhotoImage(my_image2)

my_image3=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Geography Flash Card App\\Images\\new york.png")
my_image3=my_image3.resize((320,320),Image.ANTIALIAS)
my_image3=ImageTk.PhotoImage(my_image3)

my_image4=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Geography Flash Card App\\Images\\texas.png")
my_image4=my_image4.resize((320,320),Image.ANTIALIAS)
my_image4=ImageTk.PhotoImage(my_image4)

my_image5=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Geography Flash Card App\\Images\\washington.png")
my_image5=my_image5.resize((320,320),Image.ANTIALIAS)
my_image5=ImageTk.PhotoImage(my_image5)

image_list=[my_image0,my_image1,my_image2,my_image3,my_image4,my_image5]

my_label0=Label(image=my_image0)
my_label1=Label(image=my_image1)
my_label2=Label(image=my_image2)
my_label3=Label(image=my_image3)
my_label4=Label(image=my_image4)
my_label5=Label(image=my_image5)

global Entry1
Entry1=Entry(root,font=("Helvetica",20))
Entry1.grid(row=1,column=0,pady=20)

global i
i=0
global label_list,state_name,correct
label_list=[my_label0,my_label1,my_label2,my_label3,my_label4,my_label5]
correct=0

label_list[i].grid(row=0,column=0,padx=60,pady=10)

def next():
    global label_list
    global i
    if(i<5):
        i+=1
        label_list[i].grid(row=0,column=0,padx=60,pady=10)
    else:
        submit_btn = Button(root, text="Submit", state=DISABLED)
        submit_btn.grid(row=2, column=0)

def check_answer():
    global i,correct
    submitted_answer=Entry1.get()
    state_name = ['boston', 'florida', 'nevada', 'new york', 'texas', 'washington']

    if(submitted_answer==state_name[i]):
        answer_label=Label(root,text="You gave the correct answer")
        answer_label.grid(row=3,column=0)
        correct+=1
    else:
        answer_label = Label(root, text="You gave the wrong answer")
        answer_label.grid(row=3, column=0)

    if(correct==6):
        result_label = Label(root, text="CONGRATS ! All the answers you gave were correct.")
        result_label.grid(row=3, column=0)

    Entry1.delete(0,END)

    next()

if(i<5):
    submit_btn=Button(root,text="Submit",command=check_answer)
    submit_btn.grid(row=2,column=0)


root.mainloop()