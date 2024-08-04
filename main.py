from tkinter import *
import qrcode
from PIL import ImageTk, Image

def create_and_save_qr( data, filename ='test.png'):
    img = qrcode.make( str(data) )
    img.save( filename )

def clicked():
    """
    click event on the button. validates inputs and calls image creator function.
    """
    text = txt.get()
    if len(text) == 0:
        error = Label(window, text="text is empty")
        error.grid(column=1, row=5)
        return
    filename = txt2.get()
    if len(filename) == 0:
        filename = 'test.png'
    create_and_save_qr( txt.get(), filename )


if __name__ == '__main__':
    window = Tk()

    window.title("QR Code Generator")
    window.geometry('500x100')

    lbl = Label(window, text="insert text:")
    lbl.grid(column=0, row=0)

    txt = Entry(window,width=50)
    txt.grid(column=1, row=0)

    lbl2 = Label(window, text="insert filename:")
    lbl2.grid(column=0, row=1)

    txt2 = Entry(window,width=50)
    txt2.insert(0, 'test.png') 
    txt2.grid(column=1, row=1)


    btn = Button(window, text="Create image", command=clicked)
    btn.grid(column=1, row=4, columnspan=2)

    window.mainloop()