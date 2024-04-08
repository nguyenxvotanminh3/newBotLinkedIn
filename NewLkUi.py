import time
import tkinter
import tkinter.messagebox
from datetime import datetime


import customtkinter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager
from LoginFunction import Login_Linkedin
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
from PostFuction import postOnLinkedIn,reciveFromUi
from TimerPostFunction import autoPostFuction
from AutoConnectFunction import autoConnect
from selenium.webdriver.chrome.options import Options



class App(customtkinter.CTk):


    def __init__(self):
        super().__init__()
        global stateOfTimer
        global stateOfAutoPost

        # configure window
        self.title("LinkedIn Tool")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=240, corner_radius=0,height=300)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="LinkedIn Tool", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: Login_Linkedin(driver),text="Auto Login")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: changeModeButton2(),text="Auto Post")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: changeModeButton2(), text="Auto Connect" )
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: changeModeButton2(), text="Auto Join Group")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: changeModeButton2(), text="Auto send Message")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)   




        # self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:reciveFromUi(int(getRowStart), int(getRowEnd)),text="PassVariable")
        # self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10)



        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=30, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="Entry StartRow")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        #
        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Start Row")
        # self.main_button_1.grid(row=3, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")
        #
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="Entry EndRow")
        # self.entry.grid(row=4, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        #
        # self.main_button_2 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,text_color=("gray10", "#DCE4EE"),text="End Row")
        # self.main_button_2.grid(row=4, column=3, padx=(10, 10), pady=(10, 10), sticky="nsew")


        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=400)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Set Time")
        # self.tabview.add("Tab 2")
        # self.tabview.add("Tab 3")
        # configure grid of individual tabs
        self.tabview.tab("Set Time").grid_columnconfigure(0, weight=1)
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # self.optionmenu_2 = customtkinter.CTkOptionMenu(self.tabview.tab("Set Time"), dynamic_resizing=False,
        #                                                 values=["AM","PM"])
        # self.optionmenu_2.grid(row=1, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
        #                                             values=["AM", "PM"])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Set Time"), text="Open Input Time",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Set Time"), text="Check",
                                                           command = lambda : displayTime())
        self.string_input_button.grid(row=3, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=6, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Mode")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0,text="Normal auto post")
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1, text="Timer post" , command= lambda: annouce() )
        self.radio_button_2.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2, text="Normal post" ,command= lambda: annouce())
        self.radio_button_3.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_5 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                           value=3, text="Connect", command=lambda: annouce())
        self.radio_button_5.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_5 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                           value=4, text="Message", command=lambda: annouce())
        self.radio_button_5.grid(row=4, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_6 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var,
                                                           value=5, text="Join Group", command=lambda: annouce())
        self.radio_button_6.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        # create slider and progressbar frame
        # self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        # self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        # self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        # self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        # self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # # # create scrollable frame
        # self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        # self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.scrollable_frame.grid_columnconfigure(0, weight=1)
        # self.scrollable_frame_switches = []
        # for i in range(100):
        #     switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
        #     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        #     self.scrollable_frame_switches.append(switch)

        # # create checkbox and switch frame
        # self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        # self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        # self.checkbox_3.configure(state="disabled")
        # self.checkbox_1.select()
        # self.scrollable_frame_switches[0].select()
        # self.scrollable_frame_switches[4].select()
        # self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("TIME")
        # self.optionmenu_2.set("AM/PM")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start(
        time.sleep(5)

        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")
        # self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        # self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="Entry StartRow")
        self.entry1.grid(row=1, column=1, columnspan=1, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.main_button_1 = customtkinter.CTkButton(master=self,command=lambda:display_text1(), fg_color="transparent", border_width=2,text_color=("gray10", "#DCE4EE"), text="Start Row")
        self.main_button_1.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky="ew")
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Entry EndRow")
        self.entry2.grid(row=2, column=1, columnspan=1, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.main_button_2 = customtkinter.CTkButton(master=self,command=lambda:display_text2(), fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), text="End Row")
        self.main_button_2.grid(row=2, column=2, padx=(5, 5), pady=(5, 5), sticky="ew")


        def annouce():
            value = self.radio_var.get()
            match value:
                case 1:
                    self.textbox.insert("0.0", "Timer mode is set ! " + "\n\n")
                case 2:
                    self.textbox.insert("0.0", "Auto post mode is set! " + "\n\n")
                case 3:
                    self.textbox.insert("0.0", "Connect mode is set! " + "\n\n")
                case 4:
                    self.textbox.insert("0.0", "Message mode is set! " + "\n\n")
                case 5:
                    self.textbox.insert("0.0", "Join Group mode is set! " + "\n\n")


        def displayTime():
            alarm = dialog1 # recive from Gui
            current_time = "Son tung mtp"
            while (alarm != current_time):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                self.textbox.insert("0.0", current_time + "\n\n")
                time.sleep(1)


        def display_text1():
            global getRowStart
            getRowStart = self.entry1.get()
            self.textbox.insert("0.0", "Start : " + getRowStart + "\n\n")
            self.textbox.delete(0.0,len(getRowStart))
        def display_text2():
            global getRowEnd
            getRowEnd = self.entry2.get()
            self.textbox.insert("0.0","End : " + getRowEnd + "\n\n")

        def changeModeButton2():
            value = self.radio_var.get()
            match value:
                case 1:
                    reciveFromUi(int(getRowStart), int(getRowEnd))
                    autoPostFuction(driver, alarmUi=dialog1)
                case 2:
                    reciveFromUi(int(getRowStart), int(getRowEnd))
                    postOnLinkedIn(driver)
                case 3:
                    autoConnect(driver)
                case default:
                    self.textbox.insert("0.0", "Please Chose mode " + getRowEnd + "\n\n")

    def open_input_dialog_event(self):
        global dialog1
        dialog = customtkinter.CTkInputDialog(text="Type in time", title="CTkInputDialog")

        dialog1 =dialog.get_input()


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")



# service = Service(executable_path='./chromedriver.exe')
# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\lop12\\PycharmProjects\\TestBot\\Profile 1")
# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get("https://www.google.co.in")


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.co.in")




if __name__ == "__main__":
    app = App()
    app.mainloop()
