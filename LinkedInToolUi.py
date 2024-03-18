import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from LoginFunction import Login_Linkedin,Login_Linkedin_1
from tkinter import *


from PostFuction import postOnLinkedIn,reciveFromUi


class Application(tk.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):



        self.login = tk.Button(self, text="Auto Login Linkedln", command=lambda: Login_Linkedin(driver) ,background="black" ,foreground="white" )
        self.login.pack(pady = 15)

        self.login1 = tk.Button(self, text="Basic Login Linkedln", command=lambda: Login_Linkedin_1(driver) ,background="black" ,foreground="white" )
        self.login1.pack(pady = 15)



        # self.post1 = tk.Label(root, text="Post Content of index: " + getRow)
        # entry = tk.Entry(
        #     root,
        #     width=10,
        #     justify="center",
        # )
        # getRow = entry.get()
        # entry.pack()
        # self.post1.pack()


        self.post = tk.Button(self, text="Auto Post", command=lambda: postOnLinkedIn(driver),
                                background="black", foreground="white")
        self.post.pack(pady=15)

        #test
        # can set post but dont recive getRow

        self.post1 = tk.Button(root, text="Pass Variable", command=lambda:reciveFromUi(int(getRowStart), int(getRowEnd)),
                              background="black", foreground="white", pady=30)
        self.post1.pack()




        def display_text1():
            global getRowStart
            getRowStart = entry.get()

            label.configure(text="Start Row : " + getRowStart)

        def display_text2():
            global getRowEnd
            getRowEnd = entry1.get()

            label.configure(text="End Row : " + getRowEnd)

        label = Label(root, text="", font=("Courier 22 bold"))
        label.pack()

        tk.Button(root, text="Start Row", width=20, command=display_text1).pack(pady=20)

        entry = tk.Entry(
            root,
            width=10,
            justify="center",
        )
        entry.focus_set()
        entry.pack()

        tk.Button(root, text="End Row", width=20, command=display_text2).pack(pady=20)

        entry1 = tk.Entry(
            root,
            width=10,
            justify="center",
        )

        entry1.pack()






driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
root = tk.Tk()
app = Application(master=root)
app.master.title("LinkedIn auto tools")
app.master.minsize(300, 200)
app.mainloop()
