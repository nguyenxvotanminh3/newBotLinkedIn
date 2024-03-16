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

        self.post1 = tk.Button(root, text="Yes", command=lambda:reciveFromUi(int(getRow)),
                              background="black", foreground="white", pady=30)
        self.post1.pack()



        win = Tk()
        def display_text():
            global getRow
            getRow = entry.get()
            label.configure(text="Test your option , you want to print Row : " + getRow)

        label = Label(win, text="", font=("Courier 22 bold"))
        label.pack()

        tk.Button(win, text="Okay", width=20, command=display_text).pack(pady=20)

        entry = tk.Entry(
            root,
            width=10,
            justify="center",
        )
        entry.focus_set()
        entry.pack()






driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
root = tk.Tk()
app = Application(master=root)
app.master.title("LinkedIn auto tools")
app.master.minsize(300, 200)
app.mainloop()
