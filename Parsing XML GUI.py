from Tkinter import *
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
import tkMessageBox,tkFileDialog
from ScrolledText import ScrolledText

def open_command():
    filename = tkFileDialog.askopenfile(parent=mainframe,title='Select a file',filetypes=[('Defaut', '.*'),('WebFile', '.xml'),('WebFile', '.html')])
    if filename != None:
        fn.insert(0,filename.name)
        filename.close()
def deleteent():
    fn.delete(0,END)

windows = Tk()
userentry= StringVar()
userentry2= StringVar()
#__________________________________________________________________________________________#
load = ImageTk.PhotoImage(Image.open("C:\Users\ONTAP_DVM\XML_Parsing\img\openf_but.PNG"))
rs =ImageTk.PhotoImage(Image.open("C:\Users\ONTAP_DVM\XML_Parsing\img\clear_but.PNG"))
sr =ImageTk.PhotoImage(Image.open("C:\Users\ONTAP_DVM\XML_Parsing\img\search_but.PNG"))
#__________________________________________________________________________________________#
windows.geometry('450x450+500+300')
windows.title ("XML Parser V1 By HoangPhuc-View Contents XML Tag in HTML Page")
mainframe = Frame(windows,bd=2, relief=SUNKEN)
clear = Button(mainframe, image=rs, command=deleteent,font = "Arial 8 bold ",activebackground="turquoise").pack(side=RIGHT, pady=5,padx=5,anchor=W)
openfile = Button (mainframe, image=load,command=open_command,font = "Arial 8 bold ",activebackground="turquoise").pack(side=RIGHT, pady=5,padx=5,anchor=W)
lbel= Label(mainframe,text ="File name:").pack(side=LEFT)
fn = Entry (mainframe, textvariable= userentry,width = 500)
fn.pack(side = LEFT)
mainframe.pack(fill=X, pady=10, padx=5)
#================================================================#
def get_data_from_entry():
    value = userentry.get()
    value2= userentry2.get()
    Source = BeautifulSoup(open(value),'xml')
    channels = Source.findAll(value2)
    for x in channels:
        textPad.insert(1.0,(x.find('name').string,':=>',x.description.string))



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
mainframe2 = Frame(windows,bd=2, relief=SUNKEN)
search = Button(mainframe2, image=sr,command=get_data_from_entry,bd =5,font = "Arial 8 bold ",activebackground="turquoise").pack(side=RIGHT, pady=5,padx=5,anchor=W)
lbel2= Label(mainframe2,text ="Tag name:").pack(side=LEFT)
searchtag = Entry (mainframe2, textvariable= userentry2,width = 500)
searchtag.pack(side = LEFT)
mainframe2.pack(fill=X, pady=10, padx=5)
#================================================================#
mainframe3 = Frame(windows,bd=2, relief=SUNKEN)

lbel3= Label(mainframe3,text ="Tag Contents>>>").pack(side=LEFT)

textPad = ScrolledText(mainframe3, width=100, height=80)
textPad.pack()

mainframe3.pack(fill=X, pady=10, padx=5)

windows.mainloop()

