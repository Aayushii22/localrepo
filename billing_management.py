from tkinter import *
import random
import tkinter.scrolledtext as s
from datetime import datetime
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageGrab
from PIL import Image, ImageTk
# Establish the connection to your MySQL server
bg_color='#008080'



class LoginPage:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1280x700+0+0')
        self.root.title("Billing Software")
        
        title=Label(self.root,text="Billing Software",bd=7,font=('times new roman',22,'bold'),pady=2,relief=SUNKEN,bg=bg_color,fg='White')
        title.pack(fill=X)

        self.F1=LabelFrame(self.root,bg='lightgrey',relief=GROOVE)
        self.F1.place(x=270,y=130,width=710,height=350)

        self.login=Label(self.F1,text="Login",bd=6,anchor=CENTER,relief=GROOVE,font=('sans-serif',22))
        self.login.pack(side=TOP,fill=X)

        self.title=LabelFrame(self.F1,text="Enter Details",bd=6,relief=GROOVE,bg='Lightgrey',font=('sans-serif',14))
        self.title.pack(fill=BOTH,expand=True)
        
        self.lbl=Label(self.title,text="Enter Username: ",bg='Lightgrey',font=('sans-serif',15),anchor=CENTER)
        self.lbl.grid(row=3,column=0)

        username = StringVar()
        password = StringVar()

        self.text=Entry(self.title,font=('sans-serif',17),bd=6,textvariable=username)
        self.text.grid(row=3,column=1,padx=2,pady=2)

        self.pswrd=Label(self.title,text="Enter Password:",bg='Lightgrey',font=('sans-serif',15,),anchor=CENTER)
        self.pswrd.grid(row=8,column=0)

        self.text1=Entry(self.title,font=('sans-serif',17),bd=6,textvariable=password,show="*")
        self.text1.grid(row=8,column=1,padx=2,pady=2)
        

        #Functions
        def check_login():
            '''this function will check login'''
            if username.get()=="forum1" and password.get()=="forum":
                 self.newwindow=Toplevel(self.root)
                 self.app=window2(self.newwindow)
            
            else:
                 pass

        def reset():
            username.set("")
            password.set("")
            messagebox.showinfo("Forget Password", "Please check your email or phone for password reset instructions.")
   
    



        #BUTTONS
        self.button=LabelFrame(self.title ,font=('Ariel',12),relief=GROOVE)
        self.button.place(x=100,y=120,width=480,height=50)

        
        self.b1=Button(self.button,text="Login",font=('Ariel',12,'bold'),width=16,height=1,command=check_login)
        self.b1.grid(row=0,column=1,padx=40,pady=4)

    

        self.b3=Button(self.button,text="Reset",font=('Ariel',12,'bold'),width=16,height=1,command=reset)
        self.b3.grid(row=0,column=2,padx=10,pady=4)

def validate_phone_number(action, value_if_allowed):
    # Check if the action is an insertion or deletion
     if action == '1':  # Insertion
        # Check if the input is a digit and the length is not exceeding 10
        return value_if_allowed.isdigit() and len(value_if_allowed) <= 10
     else:  # Deletion
        return True
class window2():
    def __init__(self,win):
        self.win=win
        self.win.geometry=('500x500+0+0')
        self.win.title('Billing Management System')

        self.title=Label(self.win,text="Billing Software",bd=7,font=('times new roman',22,'bold'),pady=2,relief=SUNKEN,bg='#008080',fg='White')
        self.title.pack(fill=X)
        #===========Variable===========#
       
        Bill_number = random.randint(100,9999)
        Bill_number_tk=IntVar()
        Bill_number_tk.set(Bill_number)

        
        cust=StringVar()
        contact=StringVar()
        date=StringVar()
        item=StringVar()
        quantity=StringVar()
        cost=StringVar()

        validate_phone = self.win.register(validate_phone_number)
        date.set(datetime.now())

        total_list=[]
        self.grand_total=0

        item_costs = {
            "Tshirt": 599,
            "Denim": 1899,
            "Shoe": 1299,
            "Shirt": 899,
            "Jackets": 999,
            "Watch": 1499,
            "Perfumes": 699,
            "Home Accessories": 499
            # Add more items and their costs as needed
        }

        

       

    
        #===========Entry===========#
          

        self.frame=LabelFrame(self.win,text="Enter Details",bg='light grey',font=('Ariel',14),bd=7,relief=GROOVE)
        self.frame.place(x=40,y=70,width=540,height=550)

        self.bill=Label(self.frame,text="Bill number :",font=('Ariel',15),bg='light grey')
        self.bill.grid(row=0,column=4,padx=3,pady=4)

        self.bill=Entry(self.frame,textvariable=Bill_number_tk,font=('Ariel',12),relief='groove',bd=6,width=27)
        self.bill.grid(row=0,column=10,padx=3,pady=8)
        self.bill.config(state='disabled')

        self.Customer=Label(self.frame,text="Customer Name :",font=('Ariel',15),bg='light grey')
        self.Customer.grid(row=3,column=4,padx=3,pady=4)

        self.Customer=Entry(self.frame,textvariable=cust,font=('Ariel',12),relief='groove',bd=6,width=27,)
        self.Customer.grid(row=3,column=10,padx=3,pady=4)

        self.Contact=Label(self.frame,text="Contact :",font=('Ariel',15),bg='light grey')
        self.Contact.grid(row=6,column=4,padx=3,pady=4)

        self.Contact=Entry(self.frame,textvariable=contact,font=('Ariel',12),relief='groove',bd=6,width=27)
        self.Contact.grid(row=6,column=10,padx=3,pady=4)
        self.Contact.config(validate="key", validatecommand=(validate_phone, '%d', '%P'))

        self.Date=Label(self.frame,text="Date :",font=('Ariel',15),bg='light grey')
        self.Date.grid(row=9,column=4,padx=3,pady=4)

        self.Date=Entry(self.frame,textvariable=date,font=('Ariel',12),relief='groove',bd=6,width=27)
        self.Date.grid(row=9,column=10,padx=3,pady=4)
        self.Date.config(state='disabled')

        self.Item=Label(self.frame,text="Item Purchased :" ,font=('Ariel',15),bg='light grey')
        self.Item.grid(row=12,column=4,padx=3,pady=4)
    
        self.Quantity=Label(self.frame,text="Quantity :", font=('Ariel',15),bg='light grey')
        self.Quantity.grid(row=15,column=4,padx=3,pady=4)
        
        self.Cost=Label(self.frame,text="Cost :",font=('Ariel',15),bg='light grey')
        self.Cost.grid(row=18,column=4,padx=3,pady=4)

        self.Cost=Entry(self.frame,font=('Ariel',12),relief='groove',bd=6,width=27,textvariable=cost)
        self.Cost.grid(row=18,column=10,padx=3,pady=4)

       #=============Function===============#
        
    
        def default():
            self.text_area.insert(END,"\t\t\t           FROSTICKS")
            self.text_area.insert(END,"\n\t\t\t         FORUM MALL")
            self.text_area.insert(END,"\n\t\t                   AMB Nutrients Pvt.Ltd.")
            self.text_area.insert(END,"\n\t\t              GSTIN:36AANCA1901C1Z6 ")
            self.text_area.insert(END,"\n ==========================================================")
            self.text_area.insert(END,f'Bill No:  {Bill_number_tk.get()}')

        def genbill():
            self.text_area.insert(END,f'\nCustomer Name : {cust.get()}')
            self.text_area.insert(END,f'\nContact : {contact.get()}')
            self.text_area.insert(END,f'\nDate : {date.get()}')
            self.text_area.insert(END,"\n ==========================================================")
            self.text_area.insert(END,F'\nProduct Name\t\t\t     Quantity\t\t\t     Per Cost\t\t\t    ')
            self.text_area.insert(END,"\n ==========================================================")

            self.bt1.config(state='normal')
            self.bt4.config(state='normal')
            self.bt6.config(state='normal')

        def clear():
            cust.set("")
            contact.set("")
            item.set("")
            quantity.set("")
            cost.set("")

        def reset():
            total_list.clear()
            self.grand_total=0
            self.bt1.config(state='disabled')
            self.bt4.config(state='disabled')
            self.bt6.config(state='disabled')
            self.text_area.delete("1.0",END)  
            default()

        def add_func():
            qt=int(selected_quantity.get())
            cost_1=int(cost.get())
            total=qt*cost_1
            total_list.append(total)
            self.text_area.insert(END,F'\n  {selected_item.get()}\t\t\t         {selected_quantity.get()}\t\t\t      Rs.{cost.get()}\t\t\t    ')
        
        def total_func():
            for item in total_list:
                self.grand_total=self.grand_total+item
            self.text_area.insert(END,"\n ==========================================================")
            self.text_area.insert(END,f'\t\t\t\t\t      Total :  {self.grand_total}')
            self.text_area.insert(END,"\n ==========================================================")

        
            # Add more items and their costs as needed
     

        
  

        #============BUTTON========#

        self.button=LabelFrame(self.frame,bd=5,bg='light grey',font=('Ariel',15,'bold'))
        self.button.place(x=27,y=350,width=464,height=155)

        self.bt1=Button(self.button,text="ADD",font=("arial",11,'bold'),width=15,height=3,command=add_func)
        self.bt1.grid(row=0,column=0,padx=3,pady=2)
        self.bt1.config(state='disabled')
        

        self.bt2=Button(self.button,text="Generate Bill",font=("arial",11,'bold'),width=15,height=3,command=genbill)
        self.bt2.grid(row=0,column=1,padx=3,pady=2)

        self.bt3=Button(self.button,text="Clear",font=("arial",11,'bold'),width=15,height=3,command=clear)
        self.bt3.grid(row=0,column=2,padx=3,pady=2)

        self.bt4=Button(self.button,text="Total",font=("arial",11,'bold'),width=15,height=3,command=total_func)
        self.bt4.grid(row=1,column=0,padx=3,pady=2)
        self.bt4.config(state='disabled')

        self.bt5=Button(self.button,text="Reset",font=("arial",11,'bold'),width=15,height=3,command=reset)
        self.bt5.grid(row=1,column=1,padx=3,pady=2)

        self.bt6=Button(self.button,text="Print",font=("arial",11,'bold'),width=15,height=3)
        self.bt6.grid(row=1,column=2,padx=3,pady=2)
        self.bt6.config(state='disabled')
        
        F2_bill=LabelFrame(self.win,bd=6,font=('ariel',18))
        F2_bill.place(x=690,y=90,height=500,width=565)

        F2_label=Label(F2_bill,text='Bill Area',font=('times new roman',18,'bold'),bg='#008080',pady=2,relief=SUNKEN,bd=7,fg='White')
        F2_label.pack(fill=X)

    

        #self.scroll=Scrollbar(F2_bill,orient='vertical')
        #self.scroll.pack(side=RIGHT,fill=Y)
        self.text_area=s.ScrolledText(F2_bill,width=100,height=40,font=('Times new roman',12))
        self.text_area.pack()
         
        default()

        items = ["TSHIRT", "DENIM", "SHOE", "SHIRT","JACKETS","WATCH","PERFUME","HOME ACCESSORIES"]  # Example list of items
        selected_item = Combobox(self.win, values=items)
        selected_item.place(x=216, y=268, height=28 , width=255) 


        quantities = ["1", "2", "3", "4"]  # Example list of quantities
        selected_quantity = Combobox(self.win, values=quantities)
        selected_quantity.place(x=216, y=303,height=28,width=255) 

        def print_bill():
            bill_content = self.text_area.get("1.0", END)
            if bill_content.strip():
                self.win.update()
                self.text_area.update_idletasks()

                # Coordinates of the bill area frame
                x = self.win.winfo_rootx() + F2_bill.winfo_rootx()
                y = self.win.winfo_rooty() + F2_bill.winfo_rooty()
                x1 = x + F2_bill.winfo_width()
                y1 = y + F2_bill.winfo_height()

                # Capture the bill area as an image
                bill_image = ImageGrab.grab(bbox=(x, y, x1, y1))

                # Show the captured image (optional, for preview)
                bill_image.show()

                # Print the captured image using the default printer
                # To print directly without preview, use: bill_image.print()
            else:
                messagebox.showinfo("Empty Bill", "Nothing to print. Generate a bill first.")

        # ... (Existing code remains unchanged)
        self.bt6=Button(self.button, text="Print", font=("arial", 11, 'bold'), width=15, height=3, command=print_bill)
        self.bt6.grid(row=1, column=2, padx=3, pady=2)
        self.bt6.config(state='disabled') 


 
       

       
        

        
        

        
        

root=Tk()
obj=LoginPage(root)
root.mainloop()