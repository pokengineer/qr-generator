from tkinter import *
import qrcode

def create_and_save_qr( data, filename ='test.png'):
    img = qrcode.make( str(data) )
    img.save( filename )

def clicked():
    create_and_save_qr( txt.get(), txt2.get())


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
    txt2.grid(column=1, row=1)


    btn = Button(window, text="Create image", command=clicked)
    btn.grid(column=1, row=4, columnspan=2)

    window.mainloop()