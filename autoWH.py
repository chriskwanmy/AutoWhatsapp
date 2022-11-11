import tkinter as tk
import math
import os
import webbrowser
from cefpython3 import cefpython as cef
import ctypes
import sys
import platform
import logging as _logging
import pyautogui
import time
import pygetwindow as gw

window = tk.Tk()
window.title('Whatsapp Auto Link')
window.geometry('300x450')
window.configure(background='white')

def click(event=None):
    number = str(num_entry.get())
    text = str(num_entry1.get())
    link = "https://api.whatsapp.com/send?phone=852"+number+"&text="+text
    #link = "https://api.whatsapp.com/send?phone=852"+number+"&text="+"Hello, I am Chris"
    webbrowser.open(link)
    f = open("log.txt", "a")
    f.write(number+ '\n')
    f.close()

def save_history(number):
	number = str(num_entry.get())

def get_history():
	with open('log.txt', 'r') as filehandle:
	    for line in filehandle:
	        currentPlace = line[:-1]
	        hist.append(currentPlace)
	show_hist()

def clear_hist():
	open('log.txt', 'w').close()
	hist = []

def show_hist():
	os.startfile('log.txt')

def reset():
	num_entry['text']=''

def sendSchMsg(sleeptime=3):
	number = str(num_entry.get())
	delay = int(delaytime.get())
	msg = str(schmsg.get())
	link = "https://api.whatsapp.com/send?phone=852"+number+"&text="+str(msg)
	#link = "https://api.whatsapp.com/send?phone=852"+number+"&text="+"Hello, I am Chris"
	webbrowser.open(link)

	time.sleep(1)
	gwt = gw.getWindowsWithTitle('WhatsApp')[0]

	time.sleep(delay)

	sendbtn1 = pyautogui.locateOnScreen('send.jpg', confidence=0.7)

	x,y = pyautogui.center(sendbtn1)
	pyautogui.click(x,y)

hist = []


# contact number default
contact_f = tk.Frame(window)
contact_f.pack(side=tk.TOP)
contact_l = tk.Label(contact_f, text='contact:')
contact_l.pack(side=tk.LEFT)
num_entry = tk.Entry(contact_f)
num_entry.pack(side=tk.LEFT)

contact_1f = tk.Frame(window)
contact_1f.pack(side=tk.TOP)
contact_1l = tk.Label(contact_1f, text='text:')
contact_1l.pack(side=tk.LEFT)
num_entry1 = tk.Entry(contact_1f)
num_entry1.pack(side=tk.LEFT)

# enter button
window.bind('<Return>', click)
sendBTN = tk.Button(window, text='send msg', command=click)
sendBTN.pack()

histBTN = tk.Button(window, text='history', command=get_history)
histBTN.pack()

clearBTN = tk.Button(window, text='clear history', command=clear_hist)
clearBTN.pack()

usage = tk.Label(window, text='Input phone number, press "send msg" or press Enter.')
usage.pack()

delaytimelabel = tk.Label(window, text='send after X seconds')
delaytimelabel.pack()
delaytime = tk.Entry(window)
delaytime.pack()


schmsg = tk.Entry(window)
schmsg.pack()
schsendBTN = tk.Button(window, text="send schmsg", command = lambda: sendSchMsg(int(delaytime.get())))
schsendBTN.pack()

window.mainloop()