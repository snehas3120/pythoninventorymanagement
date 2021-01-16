from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class Main:
    def __init__(self):
      self.splashminw=Tk()
      self.splashminw.title("Welcome to Aanoj's Saloon")
      width = 1000
      height = 700
      self.splashminw.config(bg="#0000ff")
      screen_width = self.splashminw.winfo_screenwidth()
      screen_height = self.splashminw.winfo_screenheight()
      x = (screen_width / 2) - (width / 2)
      y = (screen_height / 2) - (height / 2)
      self.splashminw.geometry("%dx%d+%d+%d" % (width, height, x, y))
      self.splashminw.resizable(0,0)
      self.signin = Button(self.loginframe,width=20, text="Sign in",bg="white",fg="blue",command=self.checkuser,font="Roboto 14")
      self.signin.place(x=190,y=10)
      self.register = Button(self.loginframe,width=20, text = "Register",bg="white",fg="blue",command = self.reguser,font="Roboto")
      self.register.place(x=200,y=10) 
      path = "images/my.jpg"
      img = ImageTk.PhotoImage(Image.open(path))
      main=LabelFrame(self.splashminw, width=890, height=560,bg="snow",relief="sunken")
      main.place(x=55,y=70)
      photoframe = LabelFrame(main, width=420, height=444, bg="snow", relief="raised")
      pic=Label(photoframe, image=img)
      pic.place(x=6, y=6)
      photoframe.place(x=10, y=100)
     # Label(main, text="Sales And Inventory Management System",font="roboto 32 bold underline",bg="snow").place(x=45, y=10)
      #Label(main, text="Aanojs",font="roboto 32 bold",bg="snow").place(x=450, y=160)
      #Label(main, text="Enroll No-: 171B174",font="roboto 16 bold",bg="snow").place(x=445+5, y=260)
      #Label(main, text="Batch-: B5", font="roboto 16 bold", bg="snow").place(x=450, y=310)
      #Label(main, text="Email Id-: piyushjain6369@gmail.com",font="roboto 16 bold",bg="snow").place(x=445+5, y=360)
      #Label(main, text="Ph.no:- Deleted",font="roboto 16 bold",bg="snow").place(x=445+5, y=410)
      pic.bind('<Motion>', lambda event: self.splashminw.destroy())
      self.splashminw.after(10000,lambda :self.splashminw.destroy())
      self.splashminw.mainloop()


