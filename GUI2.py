from tkinter import*

def main():
    # calling upon a constructor to create a window object
    window = TK()

    window.title("Label Example")

    label = Label( window, text="Hello World")
    label.pack(  padx = 200, pady  =  50)

    Window.mainloop()

main() 

