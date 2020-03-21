from Tkinter import *
import webbrowser
import subprocess

root = Tk()

def openTwitch():
	webbrowser.open('http://twitch.tv')

def openXFL():
	webbrowser.open('http://home.nflbite.com/')

def openKodi():
	subprocess.call("/home/pi/Desktop/Kodi.sh")

def openTorrentSites():
        webbrowser.open('http://192.168.1.82:8112')
        webbrowser.open('https://torrentfreak.com/top-10-most-popular-torrent-sites-of-2019/')
        subprocess.call("/home/pi/Desktop/Deluge.sh")
        
        
def openSurfShark():
        subprocess.call("/home/pi/Desktop/SeattleVPN.sh")
        
def openDeluge():
        webbrowser.open('http://localhost:8112')

def openHockey():
        webbrowser.open('https://nhl66.ir/')

def openFootball():
        webbrowser.open('https://home.nflbite.com/')

def openBaseball():
        webbrowser.open('https://www.reddit.com/r/MLBStreams/')

def openBasketball():
        webbrowser.open('https://home.nbabite.com/')
        
def openYoutube():
        webbrowser.open('http://youtube.com')
        
def openChromium():
        webbrowser.open('https://google.com')
        


        



# frame = Frame(root, width=500, height=0)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.focus_set()
# frame.pack()

photo1 = PhotoImage(file = "kodilogo.gif")
b1 = Button(root, text="Kodi", image=photo1, command=openKodi)
b1.grid(row=0, column=0)
#b1.focus_force()

photo2 = PhotoImage(file = "twitchlogo.gif")
b2 = Button(root, text="Twitch", image=photo2, command=openTwitch)
b2.grid(row=0, column=1)

photo3 = PhotoImage(file = "battlehawkslogo.gif")
b3 = Button(root, text="XFL",image=photo3, command=openXFL)
b3.grid(row=1, column=0)

photo4 = PhotoImage(file = "delugelogo.gif")
b4 = Button(root, text="Deluge", image=photo4, command=openDeluge)
b4.grid(row=1, column=1)

photo7 = PhotoImage(file = "blueslogo.gif")
b7 = Button(root, text="Hockey", image=photo7, command=openHockey)
b7.grid(row=2, column=0)

photo8 = PhotoImage(file = "kclogo.gif")
b8 = Button(root, text="Football", image=photo8, command=openFootball)
b8.grid(row=2, column=1)

photo9 = PhotoImage(file = "cardslogo.gif")
b9 = Button(root, text="Baseball", image=photo9, command=openBaseball)
b9.grid(row=3, column=0)

photo10 = PhotoImage(file = "celticslogo.gif")
b10 = Button(root, text="Basketball", image=photo10, command=openBasketball)
b10.grid(row=3, column=1)

photo11 = PhotoImage(file = "ytlogo.gif")
b11 = Button(root, text="Youtube", image=photo11, command=openYoutube)
b11.grid(row=4, column=0)

photo12 = PhotoImage(file = "chromiumlogo.gif")
b12 = Button(root, text="Chromium", image=photo12, command=openChromium)
b12.grid(row=4, column=1)


root.mainloop()
