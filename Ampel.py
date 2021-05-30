from tkinter import *

# Ereignisbehandlung
def buttonWeiterClick():
    if canvas.itemcget(id_rot, 'fill') == 'red' and \
       canvas.itemcget(id_gelb, 'fill') == 'gray' and \
       canvas.itemcget(id_gruen, 'fill') == 'gray':
        # aktueller Zustand: rot
        # naechster Zustand: rotgelb
        canvas.itemconfigure(id_gelb, fill='yellow')
    elif canvas.itemcget(id_rot, 'fill') == 'red' and \
       canvas.itemcget(id_gelb, 'fill') == 'yellow' and \
       canvas.itemcget(id_gruen, 'fill') == 'gray':
        # aktueller Zustand: rotgelb
        # naechster Zustand: grün
        canvas.itemconfigure(id_rot, fill='gray')
        canvas.itemconfigure(id_gelb, fill='gray')
        canvas.itemconfigure(id_gruen, fill='green')
    elif canvas.itemcget(id_rot, 'fill') == 'gray' and \
       canvas.itemcget(id_gelb, 'fill') == 'gray' and \
       canvas.itemcget(id_gruen, 'fill') == 'green':
        # aktueller Zustand: grün
        # naechster Zustand: gelb
        canvas.itemconfigure(id_rot, fill='gray')
        canvas.itemconfigure(id_gelb, fill='yellow')
        canvas.itemconfigure(id_gruen, fill='gray')
    elif canvas.itemcget(id_rot, 'fill') == 'gray' and \
       canvas.itemcget(id_gelb, 'fill') == 'yellow' and \
       canvas.itemcget(id_gruen, 'fill') == 'gray':
        # aktueller Zustand: gelb
        # naechster Zustand: rot
        canvas.itemconfigure(id_rot, fill='red')
        canvas.itemconfigure(id_gelb, fill='gray')
        canvas.itemconfigure(id_gruen, fill='gray')

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Ampel')
tkFenster.geometry('170x240')
# Zeichenfläche
canvas = Canvas(master=tkFenster, bg='blue')
canvas.place(x=5, y=5, width=160, height=190)
# Ampelkasten
canvas.create_rectangle(65, 10, 95, 110, fill='black')
# Stange
canvas.create_rectangle(78, 110, 82, 180, fill='black')
# Rot-Licht
id_rot = canvas.create_oval(70, 20, 90, 40, fill='red')
# Gelb-Licht
id_gelb = canvas.create_oval(70, 50, 90, 70, fill='gray')
# Grün-Licht
id_gruen = canvas.create_oval(70, 80, 90, 100, fill='gray')
# Button zum Weiterschalten
buttonWeiter = Button(master=tkFenster, text='weiter', command=buttonWeiterClick)
buttonWeiter.place(x=5, y=210, width=160, height=20)
# Ereignisschleife starten
tkFenster.mainloop()