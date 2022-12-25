from tkinter import*
import random
root=Tk()
root.title("Colour Changing Wallpaper")
root.geometry('600x400')

dictionary = {"Colours" : ["maroon1" , "lawn green" , "magenta2" , "purple1" , "springgreen2" , "chocolate1" , "deep pink" ,"cyan"]}

def changeColor():
    random_color = random.randint(0, len(dictionary["Colours"])-1)
    print(dictionary["Colours"][random_color])
    root.configure(background=dictionary["Colours"][random_color])
button = Button(text="Click Me!" , bg="cyan" , command=changeColor)
button.place(relx=0.5 , rely=0.5 , anchor=CENTER)

root.mainloop()