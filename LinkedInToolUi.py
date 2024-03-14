import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from LoginFunction import Login_Linkedin,Login_Linkedin_1
from PostFuction import postOnLinkedIn
import pyautogui


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.login = tk.Button(self, text="Auto Login Linkedln", command=lambda: Login_Linkedin(driver) , )
        self.login.pack(pady = 15)

        self.login1 = tk.Button(self, text="Basic Login Linkedln", command=lambda: Login_Linkedin_1(driver))
        self.login1.pack(pady = 15)


        self.post = tk.Button(root2, text="Auto post LinkedIn", command=lambda: postOnLinkedIn(driver))
        self.post.pack()


        self.post1 = tk.Label(root2, text="Post Content of index: ")
        self.post1.pack()
        iloc_start_entry = tk.Entry(
            root2,
            width=10,
            justify="center",
        )
        iloc_start_entry.pack()


        self.quit = tk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
root = tk.Tk()
root2 = tk.Tk()
app = Application(master=root)
app.master.title("LinkedIn auto tools")
app.master.minsize(300, 200)
app.mainloop()