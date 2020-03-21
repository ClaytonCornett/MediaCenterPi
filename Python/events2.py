from Tkinter import *
import webbrowser
import subprocess

root = Tk()

def openNetflix():
	webbrowser.open('http://netflix.com')

def openHulu():
	webbrowser.open('http://hulu.com')

def openKodi():
	subprocess.call("/home/pi/Desktop/Kodi.sh")

def openTorrentSites():
        webbrowser.open('http://192.168.1.82:8112')
        webbrowser.open('https://torrentfreak.com/top-10-most-popular-torrent-sites-of-2019/')
        subprocess.call("/home/pi/Desktop/Deluge.sh")
        
        
def openSurfShark():
        subprocess.call("/home/pi/Desktop/SeattleVPN.sh")
        
def openAmazon():
        webbrowser.open('amazon.com')

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

photo2 = PhotoImage(file = "netflixlogo.gif")
b2 = Button(root, text="Netflix", image=photo2, command=openNetflix)
b2.grid(row=0, column=1)

photo3 = PhotoImage(file = "hululogo.gif")
b3 = Button(root, text="Hulu",image=photo3, command=openHulu)
b3.grid(row=1, column=0)

photo4 = PhotoImage(file = "amazonlogo.gif")
b4 = Button(root, text="Amazon Video", image=photo4, command=openAmazon)
b4.grid(row=1, column=1)

photo5 = PhotoImage(file = "surfsharklogo.gif")
b5 = Button(root, text="VPN", image=photo5, command=openSurfShark)
b5.grid(row=2, column=0)

photo6 = PhotoImage(file = "tpblogo.gif")
b6 = Button(root, text="Torrent", image=photo6, command=openTorrentSites)
b6.grid(row=2, column=1)

photo7 = PhotoImage(file = "blueslogo.gif")
b7 = Button(root, text="Hockey", image=photo7, command=openHockey)
b7.grid(row=3, column=0)

photo8 = PhotoImage(file = "kclogo.gif")
b8 = Button(root, text="Football", image=photo8, command=openFootball)
b8.grid(row=3, column=1)

photo9 = PhotoImage(file = "cardslogo.gif")
b9 = Button(root, text="Baseball", image=photo9, command=openBaseball)
b9.grid(row=4, column=0)

photo10 = PhotoImage(file = "celticslogo.gif")
b10 = Button(root, text="Basketball", image=photo10, command=openBasketball)
b10.grid(row=4, column=1)

photo11 = PhotoImage(file = "ytlogo.gif")
b11 = Button(root, text="Youtube", image=photo11, command=openYoutube)
b11.grid(row=5, column=0)

photo12 = PhotoImage(file = "chromiumlogo.gif")
b12 = Button(root, text="Chromium", image=photo12, command=openChromium)
b12.grid(row=5, column=1)


root.mainloop()
