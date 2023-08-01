from tkinter import *                               #type:ignore
from tkinter.ttk import*;                           #type:ignore
from PIL import ImageTk, Image
import qrgenerator
import busseats


k = 59
i = 1
def bookings():
    global i
    global seatsnumber
    pht = phtext.get(1.0,"end-1c")
    if(k-i > 10):
        seatsnumber["text"] = "%d"%(k-i)
        seatsnos["text"] = "%d"%(k-i)
        busseats.savefiles(pht)
        
        i+=1
        img2=ImageTk.PhotoImage(Image.open("qr-img1.jpg"))       #type: ignore
        noqr.configure(image=img2)
        noqr.image=img2                                 # type: ignore


    
    else:
        seatsnumber["text"] = "0"
        seatsnos['text'] = "0"

# clear phone number from text box
def cleartext():
    phtext.delete(1.0,"end")

root = Tk()
root1 = Tk()
root.title("DRIVER MONITOR")
root1.title("BUS MONITOR")

#style for buttons
style1 = Style()
style1.configure('B1.TButton',  font =('calibri', 30, 'bold'),
                    borderwidth = '4')
style1.map('B1.TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])
style2 = Style()
style2.configure('B2.TButton', font =('calibri', 30, 'bold'),
                 borderwidth = '4')
style2.map('B2.TButton', foreground = [('active', '!disabled', 'red')],
                     background = [('active', 'black')])
root.configure(bg="light green")
style3 = Style()
style3.map('B3.TButton', foreground = [('active', '!disabled', 'blue')],
                     background = [('active', 'black')])
root.configure(bg="light green")

#No QR Code
img= Image.open("Screenshot (57).png")
img = img.resize((325,325),Image.ANTIALIAS)               #type: ignore
img= ImageTk.PhotoImage(img)
noqr= Label(root,image= img)
noqr.place(x='45',y='350')

#total architecture of the GUI
phtext = Text(root, height = 1, width = 25,font=("Helvetica",30))
heading = Label(root,foreground='green',text = "ENTER PASSENGER PHONE NUMBER",font=("Helvetica",25,'bold'))
heading.config(background="light green")
l = Label(root,foreground='blue', text = "Phone Number : ",font=("Helvetica",20,'bold'))
heading.place(x='25',y='30')
l.configure(background="light green")
l.place(x='25',y='100')
phtext.place(x='25',y='150')
seatsnumber = Label(root,text=59,font=("Helvetica",80,'bold','italic'))
totalseatsnumber=Label(root, text="of 59\nSEATS LEFT", font=("Helvetica",30,'bold','italic'))
totalseatsnumber.configure(background="light green")
seatsnumber.configure(background="light green")
seatsnumber.place(x='1200',y='350')
totalseatsnumber.place(x='1200',y = '500')
model = Label(root,text="BUS MODEL : ",font=("Arial",15))
model.place(x='1200',y='0')
regno = Label(root,text="BUS REGISTERED NUMBER : ",font=("Arial",15))
regno.place(x='1055',y='25')
btn1 = Button(root, text = 'Book now',command = bookings,style="B1.TButton")
btn1.place(x='40',y='230')
btn2 = Button(root, text="Clear",command=cleartext,style="B2.TButton")
btn2.place(x='350',y='230')

seatsnos = Label(root1,text=59,font=("Helvetica",80,'bold','italic'),foreground="white")
totalseatsnos=Label(root1, text="of 59\nSEATS LEFT", font=("Helvetica",30,'bold','italic'),foreground="white")

seatsnos.place(x='650',y='300')
totalseatsnos.place(x='800',y='300')

root1.configure(background="red")
seatsnos.configure(background="red")
totalseatsnos.configure(background="red")

root1.mainloop()
root.mainloop()