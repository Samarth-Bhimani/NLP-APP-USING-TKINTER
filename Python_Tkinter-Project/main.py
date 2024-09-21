from tkinter import *
from tkinter import messagebox
from db import Database
from myapi import API

class Validation(Exception):

    def __init__(self,message):
        print(message)

class NLPApp:

    def __init__(self):

        self.dbo = Database()
        self.apio = API()

        self.root = Tk()

        self.root.title('NLPApp')
        # self.root.iconbitmap('')
        self.root.geometry('400x650')
        self.root.configure(bg='black')
        self.Login_GUI()

        self.root.mainloop()

    def Login_GUI(self):

        self.clear()

        # Heading for Login GUI
        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 25, 'bold'))

        # Label for Email
        label1 = Label(self.root, text="Enter your Email : ", bg='black', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 15, 'bold'))

        # Email Input Box
        self.email_input = Entry(self.root, width=35,bg='white',fg='black')
        self.email_input.pack(pady=(10, 10), ipady=3)

        # Label for Password
        label2 = Label(self.root, text="Enter your Password : ", bg='black', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 15, 'bold'))

        # Password Input Box
        self.password_input = Entry(self.root, width=35, show='*',bg='white',fg='black')
        self.password_input.pack(pady=(10, 10), ipady=3)

        # Login Button
        login_button = Button(self.root, text="Login", width=15, bg='black', command=self.Perform_Login)
        login_button.pack(pady=(30, 30))
        login_button.configure(font=('verdana', 12, 'bold'))

        # Label for Register
        label3 = Label(self.root, text="Not a member ?", bg='black', fg='white')
        label3.pack(pady=(20, 10))
        label3.configure(font=('verdana', 12, 'bold'))

        # Register Button
        register_button = Button(self.root, text="Register", width=15, bg='black', command=self.Register_GUI)
        register_button.pack(pady=(5, 10))
        register_button.configure(font=('verdana', 12, 'bold'))

    def Register_GUI(self):

        self.clear()

        # Heading for Register GUI
        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 25, 'bold'))

        # Label for Name
        label1 = Label(self.root, text="Enter your Name : ", bg='black', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 15, 'bold'))

        # Name Input Box
        self.name_input = Entry(self.root, width=35,bg='white',fg='black')
        self.name_input.pack(pady=(10, 10), ipady=3)

        # Label for Email
        label2 = Label(self.root, text="Enter your Email : ", bg='black', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 15, 'bold'))

        # Email Input Box
        self.email_input = Entry(self.root, width=35,bg='white',fg='black')
        self.email_input.pack(pady=(10, 10), ipady=3)

        # Label for Password
        label3 = Label(self.root, text="Enter your Password : ", bg='black', fg='white')
        label3.pack(pady=(10, 10))
        label3.configure(font=('verdana', 15, 'bold'))

        # Password Input Box
        self.password_input = Entry(self.root, width=35, show='*',bg='white',fg='black')
        self.password_input.pack(pady=(10, 10), ipady=3)

        # Register Button
        register_button = Button(self.root, text="Register", width=15, bg='black', command=self.Perform_Registration)
        register_button.pack(pady=(30, 30))
        register_button.configure(font=('verdana', 12, 'bold'))

        # Label for Login
        label3 = Label(self.root, text="Already a member ?", bg='black', fg='white')
        label3.pack(pady=(20, 10))
        label3.configure(font=('verdana', 12, 'bold'))

        # Login Button
        login_button = Button(self.root, text="Login", width=15, bg='black', command=self.Login_GUI)
        login_button.pack(pady=(5, 10))
        login_button.configure(font=('verdana', 12, 'bold'))

    def Perform_Registration(self):

        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        try:
            if self.email_input.get() == "" or self.password_input.get() == "" or self.name_input.get() == "":
                raise Validation("email or password field cant be empty")

            response = self.dbo.Add_Data(name, email, password)

            if response:
                messagebox.showinfo('Success','User Registered Successfully, you can login now')
                self.Login_GUI()
            else:
                messagebox.showerror('Error','Email already Exists')

        except Validation as e:
            pass

    def Perform_Login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        try:
            if self.email_input.get() == "" or self.password_input.get() == "":
                raise Validation("email or password field cant be empty")

        except Validation as e:
            pass

        else:
            response = self.dbo.Search(email,password)

            if response == 1:
                messagebox.showinfo('Success','User logged in successfully')
                self.Home_GUI()
            elif response == -1:
                messagebox.showerror('Error', "User does not exists")
            else:
                messagebox.showerror('Error','Incorrect password')

    def Home_GUI(self):

        self.clear()

        # Heading for Home_GUI Page
        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 25, 'bold'))

        # Button for Sentiment Analysis
        Sentiment_button = Button(self.root, text="Sentiment Analysis", width=25, height=3, bg='black', command=self.Sentiment_GUI)
        Sentiment_button.pack(pady=(40, 30))
        Sentiment_button.configure(font=('verdana', 15, 'bold'))

        # Button for Named Entity Recognition
        NER_button = Button(self.root, text="Named Entity Recognition", width=25, height=3, bg='black', command=self.NER_GUI)
        NER_button.pack(pady=(30, 30))
        NER_button.configure(font=('verdana', 15, 'bold'))

        # Button for Emotion Prediction
        Emotion_button = Button(self.root, text="Emotion Prediction", width=25, height=3, bg='black', command=self.Emotion_GUI)
        Emotion_button.pack(pady=(30, 30))
        Emotion_button.configure(font=('verdana', 15, 'bold'))

        # Logout Button
        Logout_button = Button(self.root, text="Logout", width=15, height=2, bg='black', command=self.Login_GUI)
        Logout_button.pack(pady=(50, 30))
        Logout_button.configure(font=('verdana', 12, 'bold'))

    def Sentiment_GUI(self):

        self.clear()

        # Heading for Sentiment_GUI Page
        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 25, 'bold'))

        # Heading-2 for Sentiment_GUI
        heading2 = Label(self.root, text='Sentiment Analysis', bg='black', fg='white')
        heading2.pack(pady=(15, 30))
        heading2.configure(font=('verdana', 20, 'bold'))

        # Label for Input Text
        label1 = Label(self.root, text="Enter Text : ", bg='black', fg='white')
        label1.pack(pady=(20, 10))
        label1.configure(font=('verdana', 15, 'bold'))

        # Input Box
        self.sentiment_input = Entry(self.root, width=35, bg='white', fg='black')
        self.sentiment_input.pack(pady=(10, 10), ipady=4)

        # Button to Analyse Sentiment
        sentiment_button = Button(self.root, text="Analyse Sentiment", width=15, bg='black',command=self.Do_Sentiment)
        sentiment_button.pack(pady=(20, 10))
        sentiment_button.configure(font=('verdana', 12, 'bold'))

        # Label for Result
        self.sentiment_result = Label(self.root, text="", bg='black', fg='white')
        self.sentiment_result.pack(pady=(40, 40))
        self.sentiment_result.configure(font=('verdana', 20, 'bold'))

        # Button for Going back
        goback_button = Button(self.root, text="Go Back", width=15, bg='black', command=self.Home_GUI)
        goback_button.pack(pady=(10, 10))
        goback_button.configure(font=('verdana', 12, 'bold'))

    def NER_GUI(self):

        self.clear()

        # Heading for NER_GUI Page
        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 25, 'bold'))

        # Heading-2 for NER_GUI
        heading2 = Label(self.root, text='Named Entity Recognition', bg='black', fg='white')
        heading2.pack(pady=(15, 30))
        heading2.configure(font=('verdana', 20, 'bold'))

        # Label for Input Text
        label1 = Label(self.root, text="Enter Text : ", bg='black', fg='white')
        label1.pack(pady=(20, 10))
        label1.configure(font=('verdana', 15, 'bold'))

        # Input Box
        self.NER_input = Entry(self.root, width=35, bg='white', fg='black')
        self.NER_input.pack(pady=(10, 10), ipady=4)

        # Button to Recognize Entity
        NER_button = Button(self.root, text="Recognize Entity", width=15, bg='black', command=self.Do_NER)
        NER_button.pack(pady=(20, 10))
        NER_button.configure(font=('verdana', 12, 'bold'))

        # Label for Result
        self.NER_result = Label(self.root, text="", bg='black', fg='white')
        self.NER_result.pack(pady=(40, 40))
        self.NER_result.configure(font=('verdana', 20, 'bold'))

        # Button for Going back
        goback_button = Button(self.root, text="Go Back", width=15, bg='black', command=self.Home_GUI)
        goback_button.pack(pady=(10, 10))
        goback_button.configure(font=('verdana', 12, 'bold'))

    def Emotion_GUI(self):

        self.clear()

        # Heading for Emotion_GUI Page
        heading = Label(self.root, text='NLPApp', bg='black', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 25, 'bold'))

        # Heading-2 for Emotion_GUI
        heading2 = Label(self.root, text='Emotion Prediction', bg='black', fg='white')
        heading2.pack(pady=(15, 30))
        heading2.configure(font=('verdana', 20, 'bold'))

        # Label for Input Text
        label1 = Label(self.root, text="Enter Text : ", bg='black', fg='white')
        label1.pack(pady=(20, 10))
        label1.configure(font=('verdana', 15, 'bold'))

        # Input Box
        self.emotion_input = Entry(self.root, width=35, bg='white', fg='black')
        self.emotion_input.pack(pady=(10, 10), ipady=4)

        # Button to Predict Emotion
        emotion_button = Button(self.root, text="Predict Emotion", width=15, bg='black', command=self.Do_Emotion)
        emotion_button.pack(pady=(20, 10))
        emotion_button.configure(font=('verdana', 12, 'bold'))

        # Label for Result
        self.emotion_result = Label(self.root, text="", bg='black', fg='white')
        self.emotion_result.pack(pady=(40, 40))
        self.emotion_result.configure(font=('verdana', 20, 'bold'))

        # Button for Going back
        goback_button = Button(self.root, text="Go Back", width=15, bg='black', command=self.Home_GUI)
        goback_button.pack(pady=(10, 10))
        goback_button.configure(font=('verdana', 12, 'bold'))

    def Do_Sentiment(self):

        text = self.sentiment_input.get()
        response = self.apio.Sentiment(text)
        self.sentiment_result['text'] = response

    def Do_NER(self):

        text = self.NER_input.get()
        response = self.apio.NER(text)
        self.NER_result['text'] = response

    def Do_Emotion(self):

        text = self.emotion_input.get()
        response = self.apio.Emotion(text)
        self.emotion_result['text'] = response

    def clear(self):

        for i in self.root.pack_slaves():
            i.destroy()


nlp = NLPApp()