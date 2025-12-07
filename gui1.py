from tkinter import*

root = Tk()
root.title("GUI Demo")
root.geometry("400x400+500+200")


def show():
    status = gender.get()
    if status == 1:
        print("You are Male")
    elif status == 2:
        print("You are female")
    elif status == 3:
        print("You are TG")
    return
    
gender = IntVar()
radioMale = Radiobutton(root,text="Male",font="Arial 20",var = gender , value = 1,command = show,action =LEFT)
radioFemale = Radiobutton(root,text="Female",font="Arial 20",var = gender , value = 2,command = show)
radioTG = Radiobutton(root,text="TG",font="Arial 20",var = gender , value = 3,command = show)
radioMale.pack()
radioFemale.pack()
radioTG.pack()

mainloop()


# def showStatus():
#     status = checkState.get()
#     print("Value of Status =",status)
#     print("Type of Status =",type(status))
#     return

# checkState = IntVar()
# # checkState = BooleanVar()

# chk1 = Checkbutton(root,text="Cricket",font = "verdana 15",var= checkState, command =showStatus, onvalue= 100,offvalue = 999)
# checkState.set(100)
# # checkState.set(1)

# chk1.pack()
# mainloop()