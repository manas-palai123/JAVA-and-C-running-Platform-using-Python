import subprocess
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
#import speech_recognition as sr


def ask():

    query=my_text2.get()
    if "java program" in query:
        try:
            text_file1=open("sum.java",'r')
            open_text.text_file="sum.java"
            stuff = text_file1.read()
            my_text.insert(END,stuff)
            text_file1.close()

            #speak("Searching Wikipedia...")
            #query=query.replace("wikipedia","")
            #results=wikipedia.summary(query,sentences=2)
            #speak("According to wikipedia")
            #print(results) 
            #speak(results)
        except Exception as e:
            my_text1.insert(END,e)
    elif "c program" in query:
        try:
            text_file1=open("text.c",'r')
            open_text.text_file="text.c"
            stuff = text_file1.read()
            my_text.insert(END,stuff)
            text_file1.close()
        except Exception as e:
            my_text1.insert(END,e)
    else:
        mb.showerror("Error","Sorry my friend i can not find similar kind of page")

root=Tk()
root.title("Codec Manas")
root.geometry("700x500")
def saveas_text():
    text_file = filedialog.asksaveasfilename(initialdir="C:/Users/user/Desktop/FamilyTutor/", title="Save c file",filetypes=(("C Source files","*.c"), ))
    text_file=open(text_file,'w')
    text_file.write(my_text.get(1.0,END))
    my_text.delete('1.0',END)
#global text_file
def open_text(): 
    open_text.text_file= filedialog.askopenfilename(initialdir="C:/Users/user/Desktop/FamilyTutor/", title="Open  file",filetypes=(("C Source files","*.c"),("JAVA Source file","*.java") ))
    text_file1=open_text.text_file
    text_file1=open(text_file1,'r')
    stuff = text_file1.read()
    my_text.insert(END,stuff)
    text_file1.close()
    #open_text.text_file.close()

    #text_file.close()
def save_text():
    text_file2=open_text.text_file
    text_file2=open(text_file2,'w')
    text_file2.write(my_text.get(1.0,END))
    open_text.text_file=text_file2
    print("saved....")
    my_text.delete('1.0',END)
    my_text1.delete('1.0',END)
def run_codec():
    subprocess.call(["gcc",open_text.text_file])
    subprocess.call("a.exe")
    var1=subprocess.getoutput("a.exe")
    my_text1.insert(END,var1)
def run_codej():
    
    cmd = 'javac '+open_text.text_file
    proc = subprocess.Popen(cmd,shell=True)
    #proc.__class_getitem__
    cmd1 = 'java '+os.path.splitext(os.path.basename(open_text.text_file))[0]
    proc1=subprocess.Popen(cmd1,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    #my_text1.insert(END,proc1.stdout)
    #cmd2=my_text1.get(1.0,END)
    #my_text1.insert(tk.INSERT,proc1.stdout.read())    
    
    
    
    
    proc2 = proc1.communicate(input=b"3\n4\n")[0]
    #subprocess.STD_INPUT_HANDLE(cmd2,shell=True,stdout=subprocess.PIPE)
    my_text1.insert(END,proc2.decode())
    #subprocess.call()
    #my_text1.insert(END,proc1.stdout.read())
    #inr=proc1.stdin.read()
    #cmd1=my_text1.get(1.0,END)
    #proc2=subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE)
    #my_text1.insert(1.0,proc1.stdout.read())
    #var1=proc1.stdout.read()
    #var.set(var1)
#def reset():
    #var.set("")
def clear():
     my_text.delete('1.0',END)
     my_text1.delete('1.0',END)
     var.set(" ")
global var
var=StringVar()

my_text=Text(root,width=40,height=10,bg="black",fg="white",insertbackground="white",font=("Helvetica",16),relief=RAISED)
my_text.pack(pady=20)
my_text1=Text(root, width=40,height=5,relief=RAISED)
my_text1.pack()
my_text2=Entry(root,width=40,textvariable=var,relief=RAISED)
my_text2.pack()
my_text2.insert(END,"Add your Command here...")
#reset_button=Button(root,width=15,text="reset",bg="grey",font=("Algerian",9),command=reset)
#reset_button.pack()
#reset_button.place(x=520,y=300)
ask_button=Button(root,width=15,text="Ask",bg="grey",font=("Algerian",9),command=ask)
ask_button.pack(pady=10)
#ask_button.place(x=520,y=340)
clr_button=Button(root,width=15,text="Clear",bg="red",fg="white",font=("Algerian",9),command=clear)
clr_button.pack(pady=10)
#clr_button.place(x=520,y=380)
open_button=Button(root,width=15,text="open", bg="pink",font=("Algerian",9),command=open_text)
open_button.pack()
open_button.place(x=70,y=300)
save_button=Button(root,width=15,text="save",bg="grey",font=("Algerian",9),command=save_text)
save_button.pack()
save_button.place(x=70,y=330)
save_button=Button(root,width=15,text="save as",bg="yellow",font=("Algerian",9),command=saveas_text)
save_button.pack()
save_button.place(x=70,y=360)
runc=Button(root,width=15,text="run C",bg="orange",font=("Algerian",9),command=run_codec)
runc.pack()
runc.place(x=515,y=310)
runj=Button(root,width=15,text="run JAVA",bg="cyan",font=("Algerian",9),command=run_codej)
runj.pack()
runj.place(x=515,y=340)
root.mainloop()