from tkinter import *
import tkinter as tk
import base64
from turtle import width

class welcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        welcome = tk.Label(self, text =('welcome'),font=("Bangna New",60),fg='white',bg='gray19').place(x=285, y = 110)
        to_en_de = tk.Label(self,font = ('Bangna New',20), text ='to Encrypting - Decrypting message',fg='white',bg='gray19').place(x=220, y = 210)

        Button = tk.Button(self,font = ('Bangna New',20), text="Let's start!",bg='gray8',fg='black',width=15, command=lambda: controller.show_frame(firstPage))
        Button.place(x=295, y=280)

class firstPage(tk.Frame):
    def __init__(self, parent, controller):
        def Exit():
            self.quit()

        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Button = tk.Button(self, text="en-code", font=("Bangna New", 40), command=lambda: controller.show_frame(encodePage))
        Button.place(x=190, y=180)

        Button = tk.Button(self, text="de-code", font=("Bangna New", 40), command=lambda: controller.show_frame(decodePage))
        Button.place(x=450, y=180)

        exit = tk.Button(self, font = ('Bangna New',30),text= 'EXIT' , width = 10, command = Exit)
        exit.place(x=310,y=290)

class encodePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Text = StringVar()
        # private_key = StringVar()
        private_key0 = StringVar()
        private_key1 = StringVar()
        private_key2 = StringVar()
        private_key3 = StringVar()
        private_key4 = StringVar()
        private_key5 = StringVar()
        private_key6 = StringVar()
        private_key7 = StringVar()
        private_key8 = StringVar()
        private_key = private_key0.get() +private_key1.get()+private_key2.get()+private_key3.get()+private_key4.get()+private_key5.get()+private_key6.get()+private_key7.get()+private_key8.get()
        mode = StringVar()
        Result = StringVar()

        def Encode(key,message):
            enc=[]

            for i in range(len(message)):
                key_c = key[i % len(key)]
                enc.append(chr((ord(message[i]+32) + ord(key_c)) % 128))
            return base64.urlsafe_b64encode("".join(enc).encode()).decode()

        def Mode():
            Result.set(Encode(private_key.get(), Text.get()))
                
        def Exit():
            self.quit()

        def Reset():
            Text.set("")
            # private_key.set("")
            private_key0.set("")
            private_key1.set("")
            private_key2.set("")
            private_key3.set("")
            private_key4.set("")
            private_key5.set("")
            private_key6.set("")
            private_key7.set("")
            private_key8.set("")
            mode.set("")
            Result.set("")

        Label(self,font=('Bangena new',20),text='En - code Page',fg='white',bg='gray19').place(x=350,y=60)

        Label(self,font=('Bangena new',20),text='RESULT',fg='white',bg='gray19').place(x=150,y=320)

        Label(self, font= ('Bangena new',25), text='MESSAGE : ',fg='white',bg='gray19').place(x= 150,y=130)
        Entry(self, font = ('Bangena new',20), textvariable = Text,fg='Black', bg = 'CadetBlue1').place(x=350, y = 130,height = 40,width = 330)

        Label(self, font = ('Bangena new',25), text ='KEY : ',fg='white',bg='gray19').place(x=150, y = 190)
        # Entry(self, font = ('Bangena new',20), textvariable = private_key ,fg='Black', bg ='CadetBlue1').place(x=250, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key0 ,fg='Black', bg ='CadetBlue1').place(x=250, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key1 ,fg='Black', bg ='CadetBlue1').place(x=305, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key2 ,fg='Black', bg ='CadetBlue1').place(x=360, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key3 ,fg='Black', bg ='CadetBlue1').place(x=415, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key4 ,fg='Black', bg ='CadetBlue1').place(x=470, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key5 ,fg='Black', bg ='CadetBlue1').place(x=525, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key6 ,fg='Black', bg ='CadetBlue1').place(x=580, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key7 ,fg='Black', bg ='CadetBlue1').place(x=635, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key8 ,fg='Black', bg ='CadetBlue1').place(x=690, y = 190,height=40,width = 50)

        Entry(self, font = ('Bangena new',20), textvariable = Result, bg ='CadetBlue1',fg='black').place(x=240, y = 375 , height = 40, width = 330)

        Button(self, font = ('Bangena new',20), text = 'ENCODE'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=260, y = 260)

        Button(self, font = ('Bangena new',20) ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=450, y = 260)

        Button(self, font = ('Bangena new',15),text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=640, y = 450)

        Buttona = tk.Button(self, text="HOME", font=('Bangena new',15), padx=2, pady=2, command=lambda: controller.show_frame(firstPage))
        Buttona.place(x=70, y=450)



class decodePage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='gray19')

        Text = StringVar()
        # private_key = StringVar()
        private_key0 = StringVar()
        private_key1 = StringVar()
        private_key2 = StringVar()
        private_key3 = StringVar()
        private_key4 = StringVar()
        private_key5 = StringVar()
        private_key6 = StringVar()
        private_key7 = StringVar()
        private_key8 = StringVar()
        print("get : ",private_key0)
        print("get : ",private_key1)
        print("get : ",private_key2)
        print("get : ",private_key3)
        print("get : ",private_key4)
        print("get : ",private_key5)
        print("get : ",private_key6)
        print("get : ",private_key7)
        print("get : ",private_key8)
        private_key = private_key0.get() +private_key1.get()+private_key2.get()+private_key3.get()+private_key4.get()+private_key5.get()+private_key6.get()+private_key7.get()+private_key8.get()
        print("get : ",private_key)
        mode = StringVar()
        Result = StringVar()

        def Decode(key,message):
            dec=[]
            message = base64.urlsafe_b64decode(message).decode()

            for i in range(len(message)):
                key_c = key[i % len(key)]
                dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
            return "".join(dec)

        def Mode():
            Result.set(Decode(private_key.get(), Text.get()))

        def Exit():
            self.quit()

        def Reset():
            Text.set("")
            # private_key.set("")
            private_key0.set("")
            private_key1.set("")
            private_key2.set("")
            private_key3.set("")
            private_key4.set("")
            private_key5.set("")
            private_key6.set("")
            private_key7.set("")
            private_key8.set("")
            mode.set("")
            Result.set("")
    
        Label(self,font=('Bangena new',20),text='De - code Page',fg='white',bg='gray19').place(x=350,y=60)

        Label(self,font=('Bangena new',20),text='RESULT',fg='white',bg='gray19').place(x=150,y=320)

        Label(self, font= ('Bangena new',25), text='MESSAGE : ',fg='white',bg='gray19').place(x= 150,y=130)
        Entry(self, font = ('Bangena new',20), textvariable = Text,fg='Black', bg = 'CadetBlue1').place(x=350, y = 130,height = 40,width = 330)

        Label(self, font = ('Bangena new',25), text ='KEY : ',fg='white',bg='gray19').place(x=150, y = 190)
        # Entry(self, font = ('Bangena new',20), textvariable = private_key ,fg='Black', bg ='CadetBlue1').place(x=330, y = 190,height=40,width = 330)
        Entry(self, font = ('Bangena new',20), textvariable = private_key0 ,fg='Black', bg ='CadetBlue1').place(x=250, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key1 ,fg='Black', bg ='CadetBlue1').place(x=305, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key2 ,fg='Black', bg ='CadetBlue1').place(x=360, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key3 ,fg='Black', bg ='CadetBlue1').place(x=415, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key4 ,fg='Black', bg ='CadetBlue1').place(x=470, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key5 ,fg='Black', bg ='CadetBlue1').place(x=525, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key6 ,fg='Black', bg ='CadetBlue1').place(x=580, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key7 ,fg='Black', bg ='CadetBlue1').place(x=635, y = 190,height=40,width = 50)
        Entry(self, font = ('Bangena new',20), textvariable = private_key8 ,fg='Black', bg ='CadetBlue1').place(x=690, y = 190,height=40,width = 50)

        Entry(self, font = ('Bangena new',20), textvariable = Result, bg ='CadetBlue1',fg='black').place(x=240, y = 375 , height = 40, width = 330)

        Button(self, font = ('Bangena new',20), text = 'DECODE'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=260, y = 260)

        Button(self, font = ('Bangena new',20) ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=450, y = 260)

        Button(self, font = ('Bangena new',15),text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=640, y = 450)

        Buttona = tk.Button(self, text="HOME", font=('Bangena new',15), padx=2, pady=2, command=lambda: controller.show_frame(firstPage))
        Buttona.place(x=70, y=450)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (welcomePage, firstPage, encodePage, decodePage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.show_frame(welcomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(1000, 800)
app.mainloop()