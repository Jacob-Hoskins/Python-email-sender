from tkinter import *
import SendEmail

bgColor = 'gray'

root = Tk()
root.configure(bg=bgColor)
root.title('Email App')


class LoginView:
    def __init__(self, master):
        self.UserEmailLabel = Label(master, text="Email", bg=bgColor)
        self.UserEmailLabel.pack()
        self.UserEmailInput = Entry(master)
        self.UserEmailInput.pack()
        self.UserEmailPass = Label(master, text="Password", bg=bgColor)
        self.UserEmailPass.pack()
        self.UserEmailPassInput = Entry(master)
        self.UserEmailPassInput.pack()
        self.LoginButton = Button(master, text="Login", command=self.verify)
        self.LoginButton.pack()

        self.TechicalDetails = Label(master, text="*Gmail less secure apps must be turned on.", bg=bgColor)
        self.TechicalDetails.pack()

        self.WrongInfo = Label(master, text="Wrong email or password", bg=bgColor)


    def verify(self):
        print('clicked')
        email = self.UserEmailInput.get()
        password = self.UserEmailPassInput.get()
        if SendEmail.auth(email, password) == True:

            self.UserEmailLabel.destroy()
            self.UserEmailInput.destroy()
            self.UserEmailPass.destroy()
            self.UserEmailPassInput.destroy()
            self.LoginButton.destroy()
            self.TechicalDetails.destroy()
            self.WrongInfo.destroy()

            print('true')
            EmailUI(root, password)


        elif SendEmail.auth(email, password) == False:
            print('error')
            self.WrongInfo.pack()


class EmailUI():

    def __init__(self, master, password):
        self.password = password

        EmailFrame = Frame(master)
        EmailFrame.pack()

        EmailSenderLabel = Label(master, text="Email:", bg=bgColor)
        EmailSenderLabel.pack()

        self.EmailSenderInput = Entry(master)
        self.EmailSenderInput.pack()

        EmailRecieverLabel = Label(master, text="To:", bg=bgColor)
        EmailRecieverLabel.pack()

        self.EmailReciverInput = Entry(master)
        self.EmailReciverInput.pack()

        EmailSubjectLabel = Label(master, text="Subject", bg=bgColor)
        EmailSubjectLabel.pack()

        self.EmailSubjectInput = Entry(master)
        self.EmailSubjectInput.pack()

        self.EmailMessageInput = Text(master)
        self.EmailMessageInput.pack()

        self.SendEmailButton = Button(master, text="Send", command=self.sendEmail)
        self.SendEmailButton.pack()


    def sendEmail(self):
        sender = self.EmailSenderInput.get()
        reciver = self.EmailReciverInput.get()
        subject = self.EmailSubjectInput.get()
        message = self.EmailMessageInput.get("1.0", END)

        SendEmail.sendMessage(sender, reciver, subject, message, self.password)





app = LoginView(root)

root.mainloop()


# def UIMain():
#     #EmailInfo()
#     root.mainloop()

