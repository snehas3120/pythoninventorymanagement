
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Addtional_features import mycombobox,myentry


# ADMIN MENU
class Admin:

    def __init__(self,mainw):
        self.mainw=mainw

    # ADD ADMIN MAIN MENU TO WINDOW,ALL FRAMES AND ADD IMAGE BUTTONS
    def admin_mainmenu(self,a,b):
         print("admin")
         self.mainframe = LabelFrame(self.mainw, width=1200, height=145,bg="#f7f7f7")
         self.mainframe.place(x=100, y=100)
         mi = PhotoImage(file="images/accounts.png")
         mi = mi.subsample(a,b)
         self.accounts = Button(self.mainframe, text="Users",font="roboto 11 bold",bd=5, image=mi, compound=TOP,command=self.buildusertable)
         self.accounts.image = mi
         self.accounts.place(x=1000, y=27)
         mi = PhotoImage(file="images/Door_Out-512.png")
         mi = mi.subsample(a,b)
         self.logout = Button(self.mainframe, text="Quit",bd=5,font="roboto 11 bold", image=mi, compound=TOP)
         self.logout.image = mi
         self.logout.place(x=1100, y=27)
         self.changeuser = Button(self.mainframe, text="Sign out",bd=5,bg="cyan",font="roboto 11 bold", image=mi, compound=TOP)
         self.changeuser.image = mi
         self.changeuser.place(x=1300, y=27)
         mi = PhotoImage(file="images/items.png")
         mi = mi.subsample(a,b)
         self.items = Button(self.mainframe, text="Add new Product",bd=5, image=mi,font="roboto 11 bold", compound=TOP,command=self.additems)
         self.items.image = mi
         self.items.place(x=30, y=27)
         mi = PhotoImage(file="images/inventory.png")
         mi = mi.subsample(a,b)
         self.stocks = Button(self.mainframe, text="Product Inventory",bd=5, image=mi,font="roboto 11 bold", compound=TOP,command=self.buildprodtable)
         self.stocks.image = mi
         self.stocks.place(x=190, y=27)
         mi = PhotoImage(file="images/sales.png")
         mi=mi.subsample(a,b)
         self.sales = Button(self.mainframe, text="Sales",bd=5,font="roboto 11 bold", image=mi, compound=TOP,command=self.buildsalestable)
         self.sales.image = mi
         self.sales.place(x=350, y=27)
         mi = PhotoImage(file="images/accounts.png")
         mi = mi.subsample(a,b)
         self.staff = Button(self.mainframe, text="Staff",bd=5,font="roboto 11 bold", image=mi, compound=TOP,command=self.buildstafftable)
        
         self.staff.image = mi
         self.staff.place(x=480, y=27)
         mi = PhotoImage(file="images/accounts.png")
         mi = mi.subsample(a,b)
         self.staff = Button(self.mainframe, text="Customers",bd=5,font="roboto 11 bold", image=mi, compound=TOP,command=self.buildcustomerstable)
         
         self.staff.image = mi
         self.staff.place(x=600, y=27)
         mi = PhotoImage(file="images/accounts.png")
         mi = mi.subsample(a,b)
         self.staff = Button(self.mainframe, text=" Add Customers",bd=5,font="roboto 11 bold", image=mi, compound=TOP,command=self.addcustomer)
         
         self.staff.image = mi
         self.staff.place(x=750, y=27)
         mi = PhotoImage(file="images/accounts.png")
         mi = mi.subsample(a,b)
         self.staff = Button(self.mainframe, text=" Add Staff",bd=5,font="roboto 11 bold", image=mi, compound=TOP,command=self.addstaff)
         
         self.staff.image = mi
         self.staff.place(x=900, y=27)
         self.formframe = Frame(self.mainw, width=500, height=550, bg="#FFFFFF")
         self.formframe.place(x=100, y=315)
         self.formframeinfo = self.formframe.place_info()
         self.tableframe1 = LabelFrame(self.mainw, width=350, height=700)
         self.tableframe1.place(x=1200, y=315, anchor=NE)
         self.tableframe1info = self.tableframe1.place_info()
         self.tableframe = LabelFrame(self.mainw, width=350, height=700)
         self.tableframe.place(x=1300, y=315, anchor=NE)
         self.tableframeinfo=self.tableframe.place_info()
         self.itemframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=300)
         self.itemframe.place(x=420, y=280, anchor=NW)
         self.itemframeinfo=self.itemframe.place_info()
         self.formframe1 = Frame(self.mainw, width=500, height=445, bg="#FFFFFF")
         self.formframe1.place(x=100,y=275)
         self.formframe1info = self.formframe1.place_info()
         self.searchframe = Frame(self.mainw, width=720, height=70, bg="#FFFFFF")
         self.searchframe.place(x=575, y=260)
         self.searchframeinfo = self.searchframe.place_info()
         self.searchbut = Button(self.searchframe, text="Search Description", font="roboto 14", bg="#FFFFFF", bd=5, command=self.searchprod)
         self.searchbut.place(x=0, y=20, height=40)
         self.searchvar=StringVar()
         self.searchentry = myentry(self.searchframe, textvariable=self.searchvar, font="roboto 14", width=25, bg="#FFFFFF")
         self.searchentry.place(x=210, y=20, height=40)
         self.cur.execute("select product_desc from products")
         li = self.cur.fetchall()
         a = []
         for i in range(0, len(li)):
             a.append(li[i][0])
         self.searchentry.set_completion_list(a)
         self.resetbut = Button(self.searchframe, text="Reset", font="roboto 14", bd=5, width=8, bg="#FFFFFF", command=self.resetprodtabel)
         self.resetbut.place(x=510, y=18, height=40)
         self.removebut = Button(self.searchframe, text="Remove", font="roboto 14", bd=5,width = 8, bg="#FFFFFF")
         self.removebut1 = Button(self.searchframe, text="Remove", font="roboto 14", bd=5,width = 8, bg="#FFFFFF")
        
         self.cond=0
         self.buildprodtable()

    # ADMIN MAIN MENU ENDS

    #BUILD PRODUCT TABLE AT INVENTORY
    def buildprodtable(self):
         self.searchframe.place_forget()
         self.tableframe.place(self.tableframeinfo)
         self.formframe.place(self.formframeinfo)
         self.tableframe1.place_forget()
         self.formframe1.place_forget()
         self.itemframe.place_forget()
         if(self.cond==1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
         scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
         scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
         self.tree = ttk.Treeview(self.tableframe, columns=("Product ID", "Product Name", "Description", "Category",
         'Price', 'Stocks'), selectmode="browse", height=18,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=100)
         self.tree.column('#2', stretch=NO, minwidth=0, width=100)
         self.tree.column('#3', stretch=NO, minwidth=0, width=150)
         self.tree.column('#4', stretch=NO, minwidth=0, width=150)
         self.tree.column('#5', stretch=NO, minwidth=0, width=100)
         self.tree.column('#6', stretch=NO, minwidth=0, width=100)
         self.tree.heading('Product ID', text="Product ID", anchor=W)
         self.tree.heading('Product Name', text="Product Name", anchor=W)
         self.tree.heading('Description', text="Description", anchor=W)
         self.tree.heading('Category', text="Category", anchor=W)
         self.tree.heading('Price', text="Price", anchor=W)
         self.tree.heading('Stocks', text="Stocks", anchor=W)
         self.tree.grid(row=1, column=0, sticky="W")
         scrollbary.config(command=self.tree.yview)
         scrollbarx.grid(row=2, column=0, sticky="we")
         scrollbarx.config(command=self.tree.xview)
         scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
         self.getproducts()
         self.tree.bind("<<TreeviewSelect>>", self.clickprodtable)
         self.formframe.focus_set()
         self.itemeditv = StringVar()
         self.itemeditdescv = StringVar()
         self.itemeditcatv = StringVar()
         self.itemeditpricev = StringVar()
         self.itemeditstockv = StringVar()
         self.addstock = StringVar()
         va = 5
         l1 = ['Product Name', 'Description', 'Category', 'Price', 'Current Stock', 'Add Stock']
         for i in range(0,6):
             Label(self.formframe, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=va)
             va += 60
         Entry(self.formframe, textvariable=self.itemeditv, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=0, height=40)
         Entry(self.formframe, textvariable=self.itemeditdescv, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=60, height=40)
         x=myentry(self.formframe, textvariable=self.itemeditcatv, font="roboto 14",bg="#FFFFFF", width=20)
         x.place(x=142, y=120, height=40)
         self.cur.execute("select product_cat from products")
         li = self.cur.fetchall()
         a = []
         self.desc_name = []
         for i in range(0, len(li)):
             if (a.count(li[i][0]) == 0):
                 a.append(li[i][0])
         x.set_completion_list(a)
         Entry(self.formframe, textvariable=self.itemeditpricev, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=180, height=40)
         Entry(self.formframe, textvariable=self.itemeditstockv, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=240, height=40)
         Entry(self.formframe, textvariable=self.addstock, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=300, height=40)
         Button(self.formframe, text="Update", font="robot 11 bold",bg="#FFFFFF", bd=5, width=10, height=2,
         command=self.changeprodtable).place(x=105, y=361)
         Button(self.formframe, text="Remove", font="robot 11 bold",bg="#FFFFFF", bd=5, width=10, height=2,
         command=self.delproduct).place(x=305, y=361)
         self.cond=1
         self.mainsearch(1)

    #SEARCH FRAME FOR BOTH USER AND PRODUCT TABLE
    def mainsearch(self, f):
        self.searchvar.set('')
        if (f==1):
            self.searchframe.config(width=720)
            self.searchframe.place(x=575, y=245)
            self.searchbut.config(text="Search Description",command=self.searchprod)
            self.searchbut.place(x=0, y=23, height=37)
            self.searchentry.config(textvariable=self.searchvar,width=20)
            self.searchentry.place(x=210, y=25, height=35)
            self.cur.execute("select product_desc from products")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
            self.resetbut.config(command=self.resetprodtabel)
            self.resetbut.place(x=460, y=22, height=37)
        elif(f==0):
            self.searchframe.place(x=661, y=245)
            self.searchframe.config(width=520)
            self.searchbut.config(command=self.searchuser)
            self.searchbut.config(text="Search Username")
            self.searchbut.place(x=0,y=23)
            self.searchentry.config(width=18,textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.resetusertable)
            self.resetbut.place(x=415,y=23)
            self.cur.execute("select username from users")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
        elif(f==2):
            self.searchframe.place(x=138, y=245)
            self.searchframe.config(width=520)
            self.searchbut.config(command=self.searchinvoice)
            self.searchbut.config(text="Search Invoice No.")
            self.searchbut.place(x=0, y=23)
            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=190, y=25, height=35)
            self.resetbut.config(command=self.buildsalestable)
            self.resetbut.place(x=415, y=23)
            
            self.cur.execute("select invoice from sales")
            li = self.cur.fetchall()
            a = []
           # print(li)
            for i in range(0, len(li)):
                if(a.count(str(li[i][0]))==0):
                    a.append(str(li[i][0]))
            self.searchentry.set_completion_list(a)
        
        elif(f==4):
            self.searchframe.place(x=138, y=245)
            self.searchframe.config(width=650)
            self.searchbut.config(command=self.searchstaff)
            self.searchbut.config(text="Search Name.")
            self.searchbut.place(x=0, y=23)
            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.buildstafftable)
            self.resetbut.place(x=410, y=23)
            self.removebut.config(command=self.delstaff)
            self.removebut.place(x=520, y=20,height = 40)
            self.cur.execute("select name from staff")
            li = self.cur.fetchall()
            a = []
           # print(li)
            for i in range(0, len(li)):
                if(a.count(str(li[i][0]))==0):
                    a.append(str(li[i][0]))
            self.searchentry.set_completion_list(a)

        elif(f==5):
            print("inside customer")
            self.searchframe.place(x=138, y=245)
            self.searchframe.config(width=650)
            self.searchbut.config(command=self.searchcustomer)
            self.searchbut.config(text="Search Name.")
            self.searchbut.place(x=0, y=23)
            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.buildcustomerstable)
            self.resetbut.place(x=415, y=23)
            self.removebut1.config(command=self.delcustomer)
            self.removebut1.place(x=520, y=20,height = 40)
            self.cur.execute("select name from customerss")
            li = self.cur.fetchall()
            a = []
           # print(li)
            for i in range(0, len(li)):
                if(a.count(str(li[i][0]))==0):
                    a.append(str(li[i][0]))
            self.searchentry.set_completion_list(a)
        
        

    # FETCH PRODUCTS FROM PRODUCTS TABLE
    def getproducts(self,x=0):
         ans=''
         self.cur.execute("select * from products")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans

    # MODIFIES RECORD OF PRODUCT TABLE
    def changeprodtable(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.itemeditv.set((self.itemeditv.get()).upper())
        self.itemeditcatv.set((self.itemeditcatv.get()).upper())
        self.itemeditdescv.set((self.itemeditdescv.get()).upper())
        if(len(li) == 6):
            if self.itemeditv.get() == '' or self.itemeditdescv.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            elif self.itemeditcatv.get() == '' or self.itemeditstockv.get() == '' or self.itemeditpricev.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            else:
                l = [self.itemeditpricev.get(), self.itemeditstockv.get()]
                for i in range(0, len(l)):
                    if (not l[i].isdigit()):
                        messagebox.showerror("Error", "Invalid Data Provided")
                        return
                    elif (int(l[i]) < 0):
                        messagebox.showerror("Error", "Invalid Data Provided")
                        return
            if(self.addstock.get()== ''):
                self.addstock.set('0')

            self.cur.execute("update products set product_name=?,product_desc=?,product_cat=?,product_price = ?,stocks = ? where product_id = ?;",(self.itemeditv.get(),self.itemeditdescv.get(),self.itemeditcatv.get(),int(self.itemeditpricev.get()),(int(self.itemeditstockv.get())+int(self.addstock.get())),li[0]))
            self.base.commit()
            self.addstock.set('')
            self.tree.delete(*self.tree.get_children())
            cur=self.getproducts(li[0])
            self.tree.selection_set(cur)

    def delproduct(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if messagebox.askyesno('Alert!','Do you want to remove product from inventory?') == True and len(li) ==6:
            self.cur.execute("delete from products where product_id = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getproducts()
            self.itemeditv.set('')
            self.itemeditdescv.set('')
            self.itemeditcatv.set('')
            self.itemeditstockv.set('')
            self.itemeditpricev.set('')

    def searchprod(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from products")
        li=self.cur.fetchall()
        for i in li:
            if(i[2]==self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def resetprodtabel(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getproducts()

    # ONCLICK EVENT FOR PRODUCT TABLE
    def clickprodtable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 6):
            self.itemeditv.set((li[1]))
            self.itemeditdescv.set((li[2]))
            self.itemeditcatv.set((li[3]))
            self.itemeditpricev.set(str(li[4]))
            self.itemeditstockv.set(str(li[5]))
            self.addstock.set('')

    # FUNCTION FOR ITEM BUTTON
    def additems(self):
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemframe.place(self.itemframeinfo)
        self.newitem = StringVar()
        self.newitemdesc = StringVar()
        self.newitemcode = StringVar()
        self.newitemcat = StringVar()
        self.newitemprice = StringVar()
        self.newitemstock  = StringVar()
        l=['Product Id',"Product Name","Description","Category","Price","Stock"]
        for i in range(0,len(l)):
            Label(self.itemframe,text=l[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i,column=0,pady=15,sticky="w")
        Entry(self.itemframe, width=40, textvariable=self.newitemcode,font="roboto 11",bg="#ffffff").grid(row=0, column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe,width=40,textvariable=self.newitem,font="roboto 11",bg="#ffffff").grid(row=1,column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe,width=40,textvariable=self.newitemdesc,font="roboto 11",bg="#ffffff").grid(row=2,column=1,pady=15,padx=8,ipady=3)
        cat=myentry(self.itemframe,width=40,textvariable=self.newitemcat,font="roboto 11",bg="#ffffff")
        cat.grid(row=3,column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemprice,font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=15, padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemstock,font="roboto 11",bg="#ffffff").grid(row=5, column=1, pady=15, padx=10,ipady=3)
        self.cur.execute("select product_cat,product_name,product_desc from products")
        li=self.cur.fetchall()
        a=[]
        self.desc_name=[]
        for i in range(0,len(li)):
            if(a.count(li[i][0])==0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
        cat.set_completion_list(a)
        Button(self.itemframe,text="Add item",height=3,width = 12,bd=6,command=self.insertitem,bg="#FFFFFF").grid(row=7,column=1,pady=10,padx=12,sticky="w",ipadx=10)
        Button(self.itemframe, text="Back", height=3,width=8, bd=6,command=self.buildprodtable,bg="#FFFFFF").grid(row=7, column=1,padx=16, pady=10,sticky="e",ipadx=10)

    # PERFOMS CHECK AND ADD'S ITEMS
    def insertitem(self):
        self.newitem.set((self.newitem.get()).upper())
        self.newitemdesc.set((self.newitemdesc.get()).upper())
        self.newitemcat.set((self.newitemcat.get()).upper())
        if self.newitemcode.get() == '' or self.newitem.get() == '' or self.newitemdesc.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        elif self.newitemcat.get() == '' or self.newitemprice.get() == '' or self.newitemstock.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        else:
            l=[self.newitemcode.get(),self.newitemprice.get(),self.newitemstock.get()]
            for i in range(0,len(l)):
                if(not l[i].isdigit()):
                    if(i==0):
                        messagebox.showerror("Error", "Product ID should be in numeral")
                    else:
                        messagebox.showerror("Error", "Invalid Data Provided")
                    return
                elif(int(l[i])<0):
                    messagebox.showerror("Error", "Invalid Data Provided")
                    return
        self.cur.execute('select * from products where product_id = ?',(int(self.newitemcode.get()),))
        l=self.cur.fetchall()
        if(len(l)>0):
            messagebox.showerror("Error", "Product ID Should Be Unique")
            return
        if(self.desc_name.count(self.newitemdesc.get())!=0):
            messagebox.showerror('Error','Product with same description exsits!')
            return
        x=int(self.newitemcode.get())
        y=int(self.newitemprice.get())
        z=int(self.newitemstock.get())
        self.cur.execute("insert into products values(?,?,?,?,?,?)",(x,self.newitem.get(),self.newitemdesc.get(),
        self.newitemcat.get(),y,z))
        self.newitem.set('')
        self.newitemstock.set('')
        self.newitemprice.set('')
        self.newitemdesc.set('')
        self.newitemcode.set('')
        self.newitemcat.set('')
        messagebox.showinfo('Success','Item Added Successfully')
        self.base.commit()

    #BUILD USER TABLE
    def buildusertable(self):
         self.searchframe.place_forget()
         self.formframe.place_forget()
         self.tableframe.place_forget()
         self.itemframe.place_forget()
         self.formframe1.place(self.formframe1info)
         self.tableframe1.place(self.tableframe1info)
         self.tree.delete(*self.tree.get_children())
         self.tree.grid_remove()
         self.tree.destroy()
         scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
         scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
         self.tree = ttk.Treeview(self.tableframe1, columns=("Username", "Password", "Account Type"),
         selectmode="browse", height=17,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=170)
         self.tree.column('#2', stretch=NO, minwidth=0, width=170)
         self.tree.column('#3', stretch=NO, minwidth=0, width=170)
         self.tree.heading('Username', text="Username", anchor=W)
         self.tree.heading('Password', text="Password", anchor=W)
         self.tree.heading('Account Type', text="Account Type", anchor=W)
         self.tree.grid(row=1, column=0, sticky="W")
         scrollbary.config(command=self.tree.yview)
         scrollbarx.grid(row=2, column=0, sticky="we")
         scrollbarx.config(command=self.tree.xview)
         scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
         self.getusers()
         self.tree.bind("<<TreeviewSelect>>", self.clickusertable)
         self.formframe1.focus_set()
         self.usernamedit = StringVar()
         self.passwordedit = StringVar()
         self.accedit = StringVar()
         va = 110
         l1 = ['Username', 'Password','Profile Type']
         for i in range(0,3):
             Label(self.formframe1, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=va)
             va += 70
         Entry(self.formframe1, textvariable=self.usernamedit, font="roboto 14", bg="#FFFFFF", width=25,state='readonly').place(x=162, y=105, height=40)
         Entry(self.formframe1, textvariable=self.passwordedit, font="roboto 14", bg="#FFFFFF", width=25).place(x=162, y=175, height=40)
         profiles=mycombobox(self.formframe1, font="robot 14", width=23, textvariable=self.accedit)
         profiles.place(x=162,y=245,height=40)
         profiles.set_completion_list(['ADMIN','USER'])
         Button(self.formframe1, text="Create a User", font="robot 12 bold", bg="#FFFFFF", bd=5, width=12, height=2,
                command=self.adduser).place(x=0, y=10)
         Button(self.formframe1, text="Update", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
                command=self.changeusertable).place(x=145, y=381)
         Button(self.formframe1, text="Remove", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
                command=self.deluser).place(x=345, y=381)

         self.mainsearch(0)

    # FETCH USERS FROM USERS TABLE
    def getusers(self,x=0):
         ans=''
         self.cur.execute("select * from users")
         userslist = self.cur.fetchall()
         for i in userslist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a = self.tree.get_children()
                  ans = a[len(a) - 1]

         return ans

    def changeusertable(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.usernamedit.set((self.usernamedit.get()).upper())
        self.passwordedit.set((self.passwordedit.get()).upper())
        self.accedit.set((self.accedit.get()).upper())
        if (len(li) == 3):
            if self.usernamedit.get() == '' or self.accedit.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            if(self.accedit.get()!='ADMIN' and self.accedit.get()!='USER' ):
                messagebox.showerror("Error", "Unknown account type!")
                return
            self.cur.execute(
            "update users set password = ?,account_type = ? where username = ?;", (
            self.passwordedit.get(), self.accedit.get(),self.usernamedit.get()))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            cur = self.getusers(li[0])
            self.tree.selection_set(cur)

    def deluser(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        fa=0
        if(self.username.get()==li[0]):
            if(messagebox.askyesno("Alert!","Remove Current User?")==True):
                fa=1
            else:
                return
        if messagebox.askyesno('Alert!', 'Do you want to remove this profile?') == True and len(li) == 3:
            self.cur.execute("delete from users where username = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getusers()
            self.usernamedit.set('')
            self.passwordedit.set('')
            self.accedit.set('')
        if(fa==1):
            self.change_user()

    def adduser(self):
        self.reguser()
        self.loginw.state('normal')  # LOGIN WINDOW ENTERS

    def searchuser(self):
        if(self.searchvar.get()==''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from users")
        li=self.cur.fetchall()
        for i in li:
            if(i[0]==self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def resetusertable(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getusers()

    def clickusertable(self,event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 3):
            self.usernamedit.set((li[0]))
            self.passwordedit.set((li[1]))
            self.accedit.set((li[2]))

    # BUILD SALES TABLE
    def buildsalestable(self):
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe1.place(x=1280, y=315, anchor=NE)
        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Transaction ID","Invoice No.", "Product ID", "Description",
                                                            'Quantity', 'Price', 'CGST','SGST','Total Amount','salesperson','Date', 'Time'), selectmode="browse", height=16,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=140)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=170)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        self.tree.column('#8', stretch=NO, minwidth=0, width=130)
        self.tree.column('#9', stretch=NO, minwidth=0, width=130)
        self.tree.column('#10', stretch=NO, minwidth=0, width=130)
        self.tree.column('#11', stretch=NO, minwidth=0, width=130)
        self.tree.column('#12', stretch=NO, minwidth=0, width=130)
        self.tree.heading('Transaction ID', text="Transaction ID", anchor=W)
        self.tree.heading('Invoice No.', text="Invoice No.", anchor=W)
        self.tree.heading('Product ID', text="Product ID", anchor=W)
        self.tree.heading('Description', text="Description", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Price', text="Price", anchor=W)
        self.tree.heading('CGST', text="CGST", anchor=W)
        self.tree.heading('SGST', text="SGST", anchor=W)
        self.tree.heading('Total Amount', text="Total Amount", anchor=W)
        self.tree.heading('salesperson', text="salesperson", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.getsales()
        self.mainsearch(2)
        self.totalsales=Label(self.tableframe1,text="Total Sales",font="roboto 14 bold").place(x=0,y=400)

    def getsales(self):
        self.cur.execute("select * from saless")
        saleslist = self.cur.fetchall()
        for i in range(0,len(saleslist)):
            saleslist[i] = list(saleslist[i])
            self.cur.execute("select invoice from saless where invoice =?",(int(saleslist[i][2]),))
            l=self.cur.fetchall()
            s=(str(saleslist[i][4])).split('-')
          #  print(saleslist[i])
            saleslist[i][4]=s[2]+" - "+s[1]+" - "+s[0]
            saleslist[i]=[saleslist[i][0],saleslist[i][1],saleslist[i][2],l[0][0],saleslist[i][3],l[0][1]*(int(saleslist[i][3])),saleslist[i][4],saleslist[i][5]]
            saleslist[i]=tuple(saleslist[i])
        for i in saleslist:
            self.tree.insert('', 'end', values=(i))

    def searchinvoice(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from saless")
        saleslist = self.cur.fetchall()
        for i in range(0, len(saleslist)):
                saleslist[i] = list(saleslist[i])
                self.cur.execute("select invoice from saless where invoice =?", (int(saleslist[i][2]),))
                l = self.cur.fetchall()
                s = (str(saleslist[i][4])).split('-')
                saleslist[i][4] = s[2] + " - " + s[1] + " - " + s[0]
                saleslist[i] = [saleslist[i][0], saleslist[i][1], saleslist[i][2], l[0][0], saleslist[i][3], l[0][1] * (int(saleslist[i][3])),
                            saleslist[i][4], saleslist[i][5]]
                saleslist[i] = tuple(saleslist[i])
        for j in saleslist:
            if (str(j[1]) == str(self.searchvar.get())):
                self.tree.insert('', 'end', values=(j))
    def searchstaff(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from staffs")
        saleslist = self.cur.fetchall()
        for i in range(0, len(saleslist)):
                saleslist[i] = list(saleslist[i])
                self.cur.execute("select name from staffs where name=?", (int(saleslist[i][2]),))
                l = self.cur.fetchall()
                s = (str(saleslist[i][4])).split('-')
                saleslist[i][4] = s[2] + " - " + s[1] + " - " + s[0]
                saleslist[i] = [saleslist[i][0], saleslist[i][1], saleslist[i][2], l[0][0], saleslist[i][3], l[0][1] * (int(saleslist[i][3])),
                            saleslist[i][4], saleslist[i][5]]
                saleslist[i] = tuple(saleslist[i])
        for j in saleslist:
            if (str(j[1]) == str(self.searchvar.get())):
                self.tree.insert('', 'end', values=(j))

    def searchcustomer(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from customerss")
        saleslist = self.cur.fetchall()
        for i in range(0, len(saleslist)):
                saleslist[i] = list(saleslist[i])
                self.cur.execute("select name from customerss where name=?", (int(saleslist[i][2]),))
                l = self.cur.fetchall()
                s = (str(saleslist[i][4])).split('-')
                saleslist[i][4] = s[2] + " - " + s[1] + " - " + s[0]
                saleslist[i] = [saleslist[i][0], saleslist[i][1], saleslist[i][2], l[0][0], saleslist[i][3], l[0][1] * (int(saleslist[i][3])),
                            saleslist[i][4], saleslist[i][5]]
                saleslist[i] = tuple(saleslist[i])
        for j in saleslist:
            if (str(j[1]) == str(self.searchvar.get())):
                self.tree.insert('', 'end', values=(j))

     # BUILD SALES TABLE
    def buildstafftable(self):
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe1.place(x=1280, y=315, anchor=NE)
        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Sr. no","Name", "Gender", "Age",
                                                            'Address', 'Contact', 'Email-Id','Total sales'), selectmode="browse", height=16,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=140)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=170)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        self.tree.column('#8', stretch=NO, minwidth=0, width=130)
        self.tree.heading('Sr. no', text="Sr. no", anchor=W)
        self.tree.heading('Name', text="Name", anchor=W)
        self.tree.heading('Gender', text="Gender", anchor=W)
        self.tree.heading('Age', text="Age", anchor=W)
        self.tree.heading('Address', text="Address", anchor=W)
        self.tree.heading('Contact', text="Contact", anchor=W)
        self.tree.heading('Email-Id', text="Email-Id", anchor=W)
        self.tree.heading('Total sales', text="Total sales", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.getstaff()
        self.mainsearch(4)
        
        self.totalstaff=Label(self.tableframe1,text="Staff Details",font="roboto 14 bold").place(x=0,y=400)
        
         
     # BUILD SALES TABLE
    def buildcustomerstable(self):
        print("inside customer")
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.tableframe1.place(x=1280, y=315, anchor=NE)
        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        
        self.tree = ttk.Treeview(self.tableframe1, columns=("Sr. no","Name", "Gender", "Age",
                                                            'Address', 'Contact', 'Email-Id'), selectmode="browse", height=16,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=140)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=170)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        
        self.tree.heading('Sr. no', text="Sr. no", anchor=W)
        self.tree.heading('Name', text="Name", anchor=W)
        self.tree.heading('Gender', text="Gender", anchor=W)
        self.tree.heading('Age', text="Age", anchor=W)
        self.tree.heading('Address', text="Address", anchor=W)
        self.tree.heading('Contact', text="Contact", anchor=W)
        self.tree.heading('Email-Id', text="Email-Id", anchor=W)
        
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.getcustomers()
        self.mainsearch(5)
        self.totalcustomers=Label(self.tableframe1,text="Customer Details",font="roboto 14 bold").place(x=0,y=400)
        

    def delstaff(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if messagebox.askyesno('Alert!','Do you want to remove staff from database?') == True and len(li) ==7:
            self.cur.execute("delete from staff where name = ?;", (li[1],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
    def delcustomer(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if messagebox.askyesno('Alert!','Do you want to remove customer from database?') == True and len(li) ==7:
            self.cur.execute("delete from customerss where name = ?;", (li[1],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
               
    def addstaff(self):
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemframe.place(self.itemframeinfo)
        self.newsrno = StringVar()
        self.newstaffname = StringVar()
        self.newstaffg = StringVar()
        self.newstaffage = StringVar()
        self.newaddress = StringVar()
        self.newstaffcontact  = StringVar()
        self.newmailid = StringVar()
        l=['Sr. no',"Name","Gender","Age","Address","Contact","Email-Id"]
        for i in range(0,len(l)):
            Label(self.itemframe,text=l[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i,column=0,pady=15,sticky="w")
        Entry(self.itemframe, width=40, textvariable=self.newsrno,font="roboto 11",bg="#ffffff").grid(row=0, column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe,width=40,textvariable=self.newstaffname,font="roboto 11",bg="#ffffff").grid(row=1,column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe,width=40,textvariable=self.newstaffg,font="roboto 11",bg="#ffffff").grid(row=2,column=1,pady=15,padx=8,ipady=3)
        cat=myentry(self.itemframe,width=40,textvariable=self.newstaffage,font="roboto 11",bg="#ffffff")
        cat.grid(row=3,column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newaddress,font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=15, padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newstaffcontact,font="roboto 11",bg="#ffffff").grid(row=5, column=1, pady=15, padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newmailid,font="roboto 11",bg="#ffffff").grid(row=6, column=1, pady=15, padx=10,ipady=3)
        Button(self.itemframe,text="Add staff",height=3,bd=6,width = 12,command=self.insertstaff,bg="#FFFFFF").grid(row=7,column=1,pady=10,padx=12,sticky="w",ipadx=10)
        Button(self.itemframe, text="Back", height=3,width=8, bd=6,command=self.buildstafftable,bg="#FFFFFF").grid(row=7, column=1,padx=16, pady=10,sticky="e",ipadx=10)


        self.cur.execute("select srno,name,gender,age,address,contact,emailid from staff")
        li=self.cur.fetchall()
        a=[]
        self.desc_name=[]
        for i in range(0,len(li)):
            if(a.count(li[i][0])==0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
        cat.set_completion_list(a)
    def addcustomer(self):
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemframe.place(self.itemframeinfo)
        self.newsrno = StringVar()
        self.newcustname = StringVar()
        self.newcustg = StringVar()
        self.newcustage = StringVar()
        self.newaddress = StringVar()
        self.newcustcontact  = StringVar()
        self.newmailid = StringVar()
        l=['Sr. no',"Name","Gender","Age","Address","Contact","Email-Id"]
        for i in range(0,len(l)):
            Label(self.itemframe,text=l[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i,column=0,pady=15,sticky="w")
        Entry(self.itemframe, width=40, textvariable=self.newsrno,font="roboto 11",bg="#ffffff").grid(row=0, column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe,width=40,textvariable=self.newcustname,font="roboto 11",bg="#ffffff").grid(row=1,column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe,width=40,textvariable=self.newcustg,font="roboto 11",bg="#ffffff").grid(row=2,column=1,pady=15,padx=8,ipady=3)
        cat=myentry(self.itemframe,width=40,textvariable=self.newcustage,font="roboto 11",bg="#ffffff")
        cat.grid(row=3,column=1,pady=15,padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newaddress,font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=15, padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newcustcontact,font="roboto 11",bg="#ffffff").grid(row=5, column=1, pady=15, padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newmailid,font="roboto 11",bg="#ffffff").grid(row=6, column=1, pady=15, padx=10,ipady=3)
        Button(self.itemframe,text="Add customer",height=3,bd=6,width = 12,command=self.insertcustomer,bg="#FFFFFF").grid(row=7,column=1,pady=10,padx=12,sticky="w",ipadx=10)
        Button(self.itemframe, text="Back", height=3,width=8, bd=6,command=self.buildstafftable,bg="#FFFFFF").grid(row=7, column=1,padx=16, pady=10,sticky="e",ipadx=10)


        self.cur.execute("select * from customerss")
        li=self.cur.fetchall()
        a=[]
        self.desc_name=[]
        for i in range(0,len(li)):
            if(a.count(li[i][0])==0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
        cat.set_completion_list(a)
    def getstaff(self):
        self.cur.execute("select * from staffs")
        saleslist = self.cur.fetchall()
##        for i in range(0,len(saleslist)):
##            saleslist[i] = list(saleslist[i])
##            self.cur.execute("select name from staff where name=?",((saleslist[i][2]),))
##            l=self.cur.fetchall()
##            s=(str(saleslist[i][4])).split('-')
##            print(saleslist[i])
##            saleslist[i][4]=s[2]+" - "+s[1]+" - "+s[0]
##            saleslist[i]=[saleslist[i][0],saleslist[i][1],saleslist[i][2],l[0][0],saleslist[i][3],l[0][1]*(int(saleslist[i][3])),saleslist[i][4],saleslist[i][5]]
##            saleslist[i]=tuple(saleslist[i])
        for i in saleslist:
            self.tree.insert('', 'end', values=(i))

    def getcustomers(self):
        self.cur.execute("select * from customerss")
        saleslist = self.cur.fetchall()
##        for i in range(0,len(saleslist)):
##            saleslist[i] = list(saleslist[i])
##            self.cur.execute("select name from customerss where name=?",((saleslist[i][2]),))
##            l=self.cur.fetchall()
##            s=(str(saleslist[i][4])).split('-')
##          #  print(saleslist[i])
##            saleslist[i][4]=s[2]+" - "+s[1]+" - "+s[0]
##            saleslist[i]=[saleslist[i][0],saleslist[i][1],saleslist[i][2],l[0][0],saleslist[i][3],l[0][1]*(int(saleslist[i][3])),saleslist[i][4],saleslist[i][5]]
##            saleslist[i]=tuple(saleslist[i])
        for i in saleslist:
            self.tree.insert('', 'end', values=(i))

    def insertcustomer(self):
        self.newsrno.set((self.newsrno.get()).upper())
        self.newcustname.set((self.newcustname.get()).upper())
        self.newcustg.set((self.newcustg.get()).upper())
        if self.newcustname.get() == '' or self.newcustg.get() == '' or self.newcustage.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        elif self.newcustcontact.get() == '' or self.newaddress.get() == '' or self.newmailid.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
##        else:
##            l=[self.newitemcode.get(),self.newitemprice.get(),self.newitemstock.get()]
##            for i in range(0,len(l)):
##                if(not l[i].isdigit()):
##                    if(i==0):
##                        messagebox.showerror("Error", "Product ID should be in numeral")
##                    else:
##                        messagebox.showerror("Error", "Invalid Data Provided")
##                    return
##                elif(int(l[i])<0):
##                    messagebox.showerror("Error", "Invalid Data Provided")
##                    return
        self.cur.execute('select * from  customerss where name = ?',((self.newcustname.get()),))
        l=self.cur.fetchall()
        if(len(l)>0):
            messagebox.showerror("Error", "name Should Be Unique")
            return
        
        x=int(self.newsrno.get())
        y=int(self.newcustcontact.get())
        z=int(self.newcustage.get())
        self.cur.execute("insert into customerss values(?,?,?,?,?,?,?)",(x,self.newcustname.get(),
        self.newcustg.get(),z,self.newaddress.get(),y,self.newmailid.get()))
        self.newsrno.set('')
        self.newcustname.set('')
        self.newcustg.set('')
        self.newcustage.set('')
        self.newaddress.set('')
        self.newcustcontact.set('')
        self.newmailid.set('')
        
        messagebox.showinfo('Success','Item Added Successfully')
        self.base.commit()
    def insertstaff(self):
        self.newsrno.set((self.newsrno.get()).upper())
        self.newstaffname.set((self.newstaffname.get()).upper())
        self.newstaffg.set((self.newstaffg.get()).upper())
        if self.newstaffname.get() == '' or self.newstaffg.get() == '' or self.newstaffage.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        elif self.newstaffcontact.get() == '' or self.newaddress.get() == '' or self.newmailid.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
##        else:
##            l=[self.newitemcode.get(),self.newitemprice.get(),self.newitemstock.get()]
##            for i in range(0,len(l)):
##                if(not l[i].isdigit()):
##                    if(i==0):
##                        messagebox.showerror("Error", "Product ID should be in numeral")
##                    else:
##                        messagebox.showerror("Error", "Invalid Data Provided")
##                    return
##                elif(int(l[i])<0):
##                    messagebox.showerror("Error", "Invalid Data Provided")
##                    return
        self.cur.execute('select * from  staffs where name = ?',((self.newstaffname.get()),))
        l=self.cur.fetchall()
        if(len(l)>0):
            messagebox.showerror("Error", "name Should Be Unique")
            return
        
        x=int(self.newsrno.get())
        y=int(self.newstaffcontact.get())
        z=int(self.newstaffage.get())
        totamnt = 0
        self.cur.execute("insert into staffs values(?,?,?,?,?,?,?,?)",(x,self.newstaffname.get(),
        self.newstaffg.get(),z,self.newaddress.get(),y,self.newmailid.get(),totamnt))
        self.newsrno.set('')
        self.newstaffname.set('')
        self.newstaffg.set('')
        self.newstaffage.set('')
        self.newaddress.set('')
        self.newstaffcontact.set('')
        self.newmailid.set('')
        
        messagebox.showinfo('Success','Item Added Successfully')
        self.base.commit()


    
    
