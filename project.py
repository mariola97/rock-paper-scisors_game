from tkinter import *
from tkinter import messagebox
import random

izbor = ["Rock" , "Paper" , "Scissors"]


root=Tk()
#root.geometry("700x500")#prozor
root.title("Rock, Paper, Scissors")
igraj = Button(root, width = 20, height = 3, text = "Igraj", font = ("arial", 24, "bold"), fg = "red" , bg="grey" , command=lambda : nasumicni_izbor())
igraj.grid( row = 1, column=1)
label_igrac1 = Label(root, text="Igrač 1", font = ("arial", 30))
label_igrac2 = Label(root, text="Igrač 2", font = ("arial", 30))
label_igrac1.grid(row = 0, column=0)
label_igrac2.grid(row = 0, column= 2)
label_rezultat1 = Label(root, text=0, font = ("arial", 50))
label_rezultat2 = Label(root, text=0, font = ("arial", 50))
label_rezultat1.grid(row = 1, column=0 )
label_rezultat2.grid(row = 1, column= 2 )
def dodavanje_poena1():
    rezultat1 = int(label_rezultat1["text"])
    rezultat1 += 1;
    label_rezultat1["text"] = str(rezultat1)

def dodavanje_poena2():
    rezultat2 = int(label_rezultat2["text"])
    rezultat2 += 1;
    label_rezultat2["text"] = str(rezultat2)

label_rezultat_poruka = Label(root,font = ("arial", 17))
label_rezultat_poruka.grid(row=2, column=1)

def rezultat_poruka_update(poruka):
    label_rezultat_poruka["text"] = poruka


def provjera_pobjednika(igrac1 , igrac2):
    if (igrac1 == igrac2):
        rezultat_poruka_update("Neriješeno")
        return 0
    if (igrac1 == "Rock"):
        if(igrac2 == "Paper"):
            rezultat_poruka_update("Igrač 2 dobija bod")
            dodavanje_poena2()
        else:
            rezultat_poruka_update("Igrač 1 dobija bod")
            dodavanje_poena1()
    if (igrac1 == "Paper"):
        if (igrac2== "Scissors"):
            rezultat_poruka_update("Igrač 2 dobija bod")
            dodavanje_poena2()
        else:
            rezultat_poruka_update("Igrač 1 dobija bod")
            dodavanje_poena1()
    if (igrac1 == "Scissors"):
        if (igrac2 == "Rock"):
            rezultat_poruka_update("Igrač 2 dobija bod")
            dodavanje_poena2()
        else:
            rezultat_poruka_update("Igrač 1 dobija bod")
            dodavanje_poena1()



def nasumicni_izbor():
    global izbor_igrac1
    global izbor_igrac2
    izbor_igrac1 = random.choice(izbor)
    izbor_igrac2 = random.choice(izbor)
    label_izbor_igrac1["text"] = izbor_igrac1
    label_izbor_igrac2["text"] = izbor_igrac2
    provjera_pobjednika(izbor_igrac1, izbor_igrac2)

label_izbor_igrac1 = Label(root, font =("arial", 18, "bold"))
label_izbor_igrac1.grid(row=2, column=0 )
label_izbor_igrac2 = Label(root, font =("arial", 18, "bold"))
label_izbor_igrac2.grid(row=2, column=2 )
mainloop()
