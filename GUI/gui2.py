from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("GUI DEMO")
root.geometry("400x400+500+200")


def show():
    city = comboCity.get()
    print(F"you belongs to {city}.")
    return

lb1 = Label(root,text="Select City",font ="Arial 20",packdx = 10, pady= 15)
cities = ["-->Select<--","Pune","Mumbai","Kolhapur","Satara"]
comboCity = Combobox(root,font ="Arial 20",values=cities)
comboCity.current(0)
btnShow = Button(root,text = "Show",font="Arial 20",command = show)
btnExit = Button(root,text="Exit",font="Arial 20", command = root.desktop)
lb1.grind(row = 1)