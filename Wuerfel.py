from tkinter import *
from random import randint

# Ereignisverarbeitung
def buttonWuerfelnClick():
    # Verwaltung und Verarbeitung der Daten
    augen = randint(1,6)
    # Anzeige der Daten
    labelWuerfel.config(image=imageListe[augen-1])

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Test')
tkFenster.geometry('120x110')

# Rahmen Würfel
frameWuerfel = Frame(master=tkFenster, bg='#FFFFFF')
frameWuerfel.place(x=5, y=5, width=110, height=100)

# Bilder
imageListe = [
    PhotoImage(file='w1.gif'),
    PhotoImage(file='w2.gif'),
    PhotoImage(file='w3.gif'),
    PhotoImage(file='w4.gif'),
    PhotoImage(file='w5.gif'),
    PhotoImage(file='w6.gif')
    ]

# Label Würfel mit Bild
labelWuerfel = Label(master=frameWuerfel, image=imageListe[0])
labelWuerfel.place(x=40, y=25, width=30, height=30)

# Button zum Würfeln
buttonWuerfel = Button(master=frameWuerfel, text='würfeln', command=buttonWuerfelnClick)
buttonWuerfel.place(x=5, y=75, width=100, height=20)

# Aktivierung des Fensters
tkFenster.mainloop()