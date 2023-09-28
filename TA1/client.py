import socket
from threading import Thread
# Import tkinter as tk
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

class GUI:
    # Create initializer method
    def __init__(self):
        # Create an instance variable named window using TK()
        self.window = Tk()
        # Set title of the window using title() method
        self.window.title("Login")
        # Make window resizable to false using resizable() method
        self.window.resizable(width=False, height=False)
        # Use configure() method to set width and height of the window
        self.window.configure(width=400, height=300)
        # Call mainloop() method on window to tell that this component to be run
        self.window.mainloop()


app = GUI()
app.mainloop()

# Comment rest of the code
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