import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(width=False, height=False)
        self.configure(width=400, height=300)

        # Create a label named pageLabel using Label() function and pass it text and font parameters
        self.pageLabel = Label( text = "Please login to continue",
                                font = "Helvetica 14 bold")
        # Place the pageLabel using place() method and pass it relx, rely for x and y axis positions
        self.pageLabel.place(relx = 0.2,
                             rely = 0.07)
        
        # Create and input box using Entry() method and pass it font parameter
        self.nameEntry = Entry(font = "Helvetica 14")
        self.nameEntry.place(relwidth = 0.4,
                            relheight = 0.12,
                            relx = 0.35,
                            rely = 0.2)
        self.nameEntry.focus()


app = GUI()
app.mainloop()

# nickname = input("Choose your nickname: ")

# client.connect((ip_address, port))
# print("Connected with the server...")

# def receive():
#     while True:
#         try:
#             message = client.recv(2048).decode('utf-8')
#             print(message)
#         except:
#             print("An error occurred!")
#             client.close()
#             break
        

# def write():
#     while True:
#         message = '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('utf-8'))

# receive_thread = Thread(target=receive)
# receive_thread.start()

# write_thread = Thread(target=write)
# write_thread.start()