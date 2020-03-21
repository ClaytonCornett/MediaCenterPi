from Tkinter import *
import webbrowser

window = Tk()
window.title("Testing")

#open Netflix
def openNetflix():
	webbrowser.open('http://netflix.com')

#Create website button
b = Button(window, text="Netflix", command=openNetflix)
b.pack()


window.mainloop()
