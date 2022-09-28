import tkinter
from tkinter import filedialog
import playsound
import datetime
import time


aaud=''

w=tkinter.Tk()
w.title('⏰ALARM CLOCK')
w.geometry('950x600')
w.resizable(0,0)



ev1=tkinter.StringVar(w)
ev2=tkinter.StringVar(w)
ev3=tkinter.IntVar(w)
ev4=tkinter.IntVar(w)
ev5=tkinter.StringVar(w)

rb3=tkinter.Radiobutton(w,text='am',variable=ev4,value=0,font=('Calibri',15))
rb4=tkinter.Radiobutton(w,text='pm',variable=ev4,value=1,font=('Calibri',15))

err=tkinter.Label(w,text='***Enter the correct responses in the prescribed format',fg='red',font=('calibri',15))

cn2=tkinter.Canvas(w,width=100,height=100)
img=tkinter.PhotoImage(file='aalaarmc.png')
cn2.create_image(180,120,image=img,anchor='se')


def browse():
    global aaud
    aud=tkinter.filedialog.askopenfilename(filetypes=(('Audio Files',"*.mp3 .m4a .amr .ogg .aac .flac"), ))
    ev5.set(aud)
    aaud=str(aud)

def a24(a,b):
    global aaud
    while True:
        time.sleep(1)
        current_time=datetime.datetime.now()
        ndate=current_time.strftime("%d/%m/%Y")
        print(ndate,'\n')
        if ndate==b:
            while True:
                time.sleep(1)
                current_time=datetime.datetime.now()
                ntime=current_time.strftime("%H:%M:%S")
                print(ntime)
                if ntime==a:
                    playsound.playsound(aaud)
                    tkinter.messagebox.showinfo(title='ALARM',message="It's High Time")
                    ev1.set('')
                    ev2.set('')
                    ev5.set('')
                    return
                
                    


def a12(a,b,d):
    if d==0:
        a24(a,b)
    elif d==1:
        a=str(int(a[:2])+12)+a[2:]
        a24(a,b)

def error():
    err.place(x=265,y=450)
    return
    

def rem():
    rb3.place_forget()
    rb4.place_forget()
    

def mer():
    rb3.place(x=600,y=250)
    rb4.place(x=600,y=275)
    

def stl():
    a=ev1.get()
    b=ev2.get()
    c=ev3.get()
    d=ev4.get()
    if len(a)!=8 or len(b)!=10:
        error()
    elif a[:2].isdigit or a[3:5].isdigit or a[6:].isdigit or b[:2].isdigit or b[3:5].isdigit or b[6:].isdigit:
        err.place_forget()
        if c==0:
            a24(a,b)
        elif c==1:
            a12(a,b,d)
    else:
        error()
        
    

lbh=tkinter.Label(w,text='ALARM CLOCK',width=50,font=('Algerian',24),bg='cyan',fg='blue')
lbh.place(x=0,y=0)

cn1=tkinter.Canvas(w,width=180,height=120)
cn1.place(x=0,y=0)
img=tkinter.PhotoImage(file='aalaarmc.png')
cn1.create_image(120,125,image=img,anchor='se')

ms1=tkinter.Label(w,text='Enter the Time of your alarm in HH:MM:SS :-',justify='left',width=36,font=('Arial',15))
ms1.place(x=150,y=100)

en1=tkinter.Entry(w,textvariable=ev1,font=('Arial',18))
en1.place(x=580,y=100)

ms2=tkinter.Label(w,text='Enter the Date for alarm in DD/MM/YYYY :-',justify='left',width=36,font=('Arial',15))
ms2.place(x=150,y=160)

en2=tkinter.Entry(w,textvariable=ev2,font=('Arial',18))
en2.place(x=580,y=160)

en3=tkinter.Entry(w,textvariable=ev5,width=42,font=('calibri',12))
en3.place(x=280,y=390)

ms3=tkinter.Label(w,text='Format :-',justify='left',width=36,font=('Calibri Bold',20),fg='green')
ms3.place(x=50,y=210)

ms4=tkinter.Label(w,text='Select the Audio File :-',font=('Calibri',18),fg='blue')
ms4.place(x=150,y=340)

rb1=tkinter.Radiobutton(w,text='24-Hour Format',variable=ev3,value=0,font=('Calibri',15),command=rem)
rb2=tkinter.Radiobutton(w,text='12-Hour Format',variable=ev3,value=1,font=('Calibri',15),command=mer)
rb1.place(x=300,y=250)
rb2.place(x=300,y=280)

bt1=tkinter.Button(w,text='BROUSE',font=('Arial Black',10),fg='teal',bg='light green',command=browse)
bt1.place(x=630,y=385)

bt2=tkinter.Button(w,text='SET ALARM',font=('Cooper Black',20),bg='wheat',fg='brown',command=stl)
bt2.place(x=400,y=500)




w.mainloop()
