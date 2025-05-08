import sqlite3
from tkinter import *
from tkinter import ttk , messagebox
from datetime import datetime
####################################
f=("B Titr",12)
btnbg="blue"
btnfg="white"
bg = "lightblue"

def Gui():
    global win,personal,treep , treepr , Product,Customers,treec,Accounting,treef , lbmemberq , Thb , main , Reporting , Setting , lbcustomerq , lbbalanceq , lbproductq
    db()
    win = Tk()
    win.geometry("700x500")
    win.title("Business Management")
    win.resizable(0,0)
    win.iconphoto(True,PhotoImage(file="download.png"))
    win.columnconfigure(0,weight=1)
    win.rowconfigure(0,weight=1)
####################################
    main = Frame(win,bg=bg)
    main.grid(row=0,column=0,sticky='nsew')
    current= datetime.now().strftime("%H:%M:%S")
    lb=Label(main,text=f"!سلام خوش آمدید \n {current}",font=("B Titr",12),bg=btnbg,fg=btnfg)
    lb.pack(fill=X)
    update_time(lb)
    btnPersonal=Button(main,text='پرسنل',width=20,command=lambda:personal.tkraise(),border=0,bg=btnbg,fg=btnfg,font=f)
    btnPersonal.place(x=50,y=100)
    btnProduct=Button(main,text='محصولات',width=20,command=lambda:Product.tkraise(),border=0,bg=btnbg,fg=btnfg,font=f)
    btnProduct.place(x=50,y=200)
    btnCustomer=Button(main,text='مشتریان ',width=20,command=lambda:Customers.tkraise(),border=0,bg=btnbg,fg=btnfg,font=f)
    btnCustomer.place(x=50,y=300)
    btnAccounting=Button(main,text='حسابداری',width=20,command=lambda:Accounting.tkraise(),border=0,bg=btnbg,fg=btnfg,font=f)
    btnAccounting.place(x=400,y=100)
    btnReporting=Button(main,text='گزارش گیری',width=20,command=lambda:Reporting.tkraise() ,border=0,bg=btnbg,fg=btnfg,font=f)
    btnReporting.place(x=400,y=200)
    btnSetting=Button(main,text='تنظیمات',width=20,command=lambda:Setting.tkraise(),border=0,bg=btnbg,fg=btnfg,font=f)
    btnSetting.place(x=400,y=300)
    btnclose=Button(main,text='خروج',width=20,command=close,border=0,bg=btnbg,fg=btnfg,font=f)
    btnclose.place(x=230,y=400)
##################################
    personal = Frame(win,bg=bg)
    personal.grid(row=0,column=0,sticky='nsew')
    btnadd = Button(personal,text='ثبت پرسنل جدید',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=add_personal)
    btnadd.place(x=30,y=20)
    btnadd = Button(personal,text='فیش حقوقی',width=10,border=0,bg=btnbg,fg=btnfg,font=f)
    btnadd.place(x=30,y=120)
    btnedit = Button(personal,text='ویرایش اطلاعات',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=EditPersonal)
    btnedit.place(x=30,y=220)
    btnadd = Button(personal,text='حذف',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=DeletePersonal)
    btnadd.place(x=30,y=320)
    btnback=Button(personal,text='برگشت به خانه',command=lambda:main.tkraise(),width=10,border=0,bg=btnbg,fg=btnfg,font=f)
    btnback.place(x=30,y=420)
    treep=ttk.Treeview(personal,columns=('id','fname','lname','position','salary'),show='headings')
    treep.column("#0",width=0,stretch=NO)
    treep.column("id",width=30,anchor=CENTER,stretch=NO)
    treep.column("fname",width=100,anchor=CENTER,stretch=NO)
    treep.column('lname',width=130,anchor=CENTER,stretch=NO)
    treep.column('position',width=100,anchor=CENTER,stretch=NO)
    treep.column('salary',width=120,anchor=CENTER,stretch=NO)
    treep.heading("id", text="کد")
    treep.heading("fname", text="نام")
    treep.heading('lname', text="نام خانوادگی")
    treep.heading('position', text="موقعیت")
    treep.heading('salary', text="حقوق")
    treep.bind("<<TreeviewSelect>>",lambda event: get_selected_data(event, treep))
    treep.place(x=190,y=20)
    showpersonal()
##################################
    Product = Frame(win,bg=bg)
    Product.grid(row=0,column=0,sticky='nsew')
    btnadd = Button(Product,text='ثبت محصول جدید',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=add_product)
    btnadd.place(x=30,y=20)
    btnedit = Button(Product,text='ویرایش اطلاعات',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=EditProduct)
    btnedit.place(x=30,y=145)
    btnadd = Button(Product,text='حذف',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=DeleteProduct)
    btnadd.place(x=30,y=270)
    btnback=Button(Product,text='برگشت به خانه',command=lambda:main.tkraise(),width=10,border=0,bg=btnbg,fg=btnfg,font=f)
    btnback.place(x=30,y=395)
    treepr=ttk.Treeview(Product,columns=('id','product','bprice','sprice','qnt'),show='headings')
    treepr.column("#0",width=0,stretch=NO)
    treepr.column("id",width=40,anchor=CENTER,stretch=NO)
    treepr.column("product",width=150,anchor=CENTER,stretch=NO)
    treepr.column('bprice',width=90,anchor=CENTER,stretch=NO)
    treepr.column('sprice',width=90,anchor=CENTER,stretch=NO)
    treepr.column('qnt',width=100,anchor=CENTER,stretch=NO)
    treepr.heading("id", text="کد")
    treepr.heading("product", text=" نام محصول")
    treepr.heading('bprice', text="قیمت خرید")
    treepr.heading('sprice', text="قیمت فروش")
    treepr.heading('qnt', text="موجودی")
    treepr.bind("<<TreeviewSelect>>",lambda event: get_selected_data(event, treepr))
    treepr.place(x=190,y=20)
    showproduct()
#################################
    Customers = Frame(win,bg=bg)
    Customers.grid(row=0,column=0,sticky='nsew')
    btnadd = Button(Customers,text='ثبت مشتری جدید',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=add_customer)
    btnadd.place(x=30,y=20)
    btnedit = Button(Customers,text='ویرایش اطلاعات',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=EditCustomer)
    btnedit.place(x=30,y=145)
    btnadd = Button(Customers,text='حذف',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=DeleteCustomer)
    btnadd.place(x=30,y=270)
    btnback=Button(Customers,text='برگشت به خانه',command=lambda:main.tkraise(),width=10,border=0,bg=btnbg,fg=btnfg,font=f)
    btnback.place(x=30,y=395)
    treec=ttk.Treeview(Customers,columns=('id','fname','lname','phone'),show='headings')
    treec.column("#0",width=0,stretch=NO)
    treec.column("id",width=35,anchor=CENTER,stretch=NO)
    treec.column("fname",width=130,anchor=CENTER,stretch=NO)
    treec.column('lname',width=150,anchor=CENTER,stretch=NO)
    treec.column('phone',width=170,anchor=CENTER,stretch=NO)
    treec.heading("id", text="کد")
    treec.heading("fname", text="نام")
    treec.heading('lname', text="نام خانوادگی")
    treec.heading('phone', text="تلفن")
    treec.bind("<<TreeviewSelect>>",lambda event: get_selected_data(event, treec))
    treec.place(x=190,y=20)
    showcustomer()
##########################################################
    Accounting = Frame(win,bg=bg)
    Accounting.grid(row=0,column=0,sticky='nsew')
    btnadd = Button(Accounting,text='ثبت تراکنش',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=add_financial)
    btnadd.place(x=30,y=20)
    btnedit = Button(Accounting,text='ویرایش تراکنش',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=EditFinance)
    btnedit.place(x=30,y=145)
    btnadd = Button(Accounting,text='حذف',width=10,border=0,bg=btnbg,fg=btnfg,font=f,command=DeleteFinance)
    btnadd.place(x=30,y=270)
    btnback=Button(Accounting,text='برگشت به خانه',command=lambda:main.tkraise(),width=10,border=0,bg=btnbg,fg=btnfg,font=f)
    btnback.place(x=30,y=395)
    treef=ttk.Treeview(Accounting,columns=('id','type','amount','date','status'),show='headings')
    treef.column("#0",width=0,stretch=NO)
    treef.column("id",width=30,anchor=CENTER,stretch=NO)
    treef.column("type",width=85,anchor=CENTER,stretch=NO)
    treef.column('amount',width=110,anchor=CENTER,stretch=NO)
    treef.column('date',width=150,anchor=CENTER,stretch=NO)
    treef.column('status',width=100,anchor=CENTER,stretch=NO)
    treef.heading("id", text="کد")
    treef.heading("type", text="نوع")
    treef.heading('amount', text="مقدار")
    treef.heading('date', text="تاریخ")
    treef.heading('status', text="وضعیت")
    treef.bind("<<TreeviewSelect>>",lambda event: get_selected_data(event, treef))
    treef.place(x=190,y=20)
    showfinancial()
##################################
    Reporting = Frame(win,bg=bg)
    Reporting.grid(row=0,column=0,sticky='nsew')
    lbmember=Label(Reporting,text="تعداد پرسنل  :",font=f,bg=bg)
    lbmember.place(x=50,y=30)
    lbmemberq=Label(Reporting,text="0",font=f,bg=bg)
    lbmemberq.place(x=200,y=30)
    lbcustomer=Label(Reporting,text="تعداد مشتریان  :",font=f,bg=bg)
    lbcustomer.place(x=50,y=100)
    lbcustomerq=Label(Reporting,text="0",font=f,bg=bg)
    lbcustomerq.place(x=200,y=100)
    lbproduct=Label(Reporting,text="تعداد محصول  :",font=f,bg=bg)
    lbproduct.place(x=50,y=170)
    lbproductq=Label(Reporting,text="0",font=f,bg=bg)
    lbproductq.place(x=200,y=170)
    lbbalance=Label(Reporting,text=" موجودی حساب :",font=f,bg=bg)
    lbbalance.place(x=50,y=240)
    lbbalanceq=Label(Reporting,text="0",font=f,bg=bg)
    lbbalanceq.place(x=200,y=240)
    btnupdatereport=Button(Reporting,text="بروزرسانی گزارش",font=f,command=Reporter,border=0,bg=btnbg,fg=btnfg,width=25)
    btnupdatereport.place(x=30,y=400)
    btnback=Button(Reporting,text='برگشت به خانه',command=lambda:main.tkraise(),width=25,border=0,bg=btnbg,fg=btnfg,font=f)
    btnback.place(x=375,y=400)
#################################
    Setting = Frame(win,bg=bg)
    Setting.grid(row=0,column=0,sticky='nsew')
    Label(Setting,text="رنگ پس زمینه :",bg=bg,font=f).place(x=20,y=20)
    Thb=ttk.Combobox(Setting,values=[bg,"pink","red","black","white"])
    Thb.current(0)
    Thb.place(x=130,y=25)
    btnapply=Button(Setting,text="اعمال تغییرات",font=f,bg=btnbg,fg=btnfg,width=20,border=0,command=Settingg)
    btnapply.place(x=50,y=400)
    btnback=Button(Setting,text='برگشت به خانه',command=lambda:main.tkraise(),width=20,border=0,bg=btnbg,fg=btnfg,font=f)
    btnback.place(x=400,y=400)
#################################
    main.tkraise()
    win.mainloop()






def add_personal():
    global en_fname,en_lname,en_position,en_salary,add
    add=Toplevel(personal,bg="lightblue")
    add.title("پرسنل جدید")
    add.geometry("300x350")
    showpersonal()
    lbb=Label(add,text="لطفا مشخصات زیر را به درستی وارد کنید",font=btnfg,bg=btnbg,fg=btnfg)
    lbb.pack(fill=X)
    lbb=Label(add,text="نام ",font=f,bg="lightblue",fg=btnbg)
    lbb.pack(fill=X)
    en_fname=Entry(add,width=12,font=f,border=0)
    en_fname.pack(fill=X)
    lbb=Label(add,text=" نام خانوادگی ",font=f,bg="lightblue",fg=btnbg)
    lbb.pack(fill=X)
    en_lname=Entry(add,width=12,font=f,border=0)
    en_lname.pack(fill=X)
    lbb=Label(add,text="موقعیت",font=f,bg="lightblue",fg=btnbg)
    lbb.pack(fill=X)
    en_position=Entry(add,width=12,font=f,border=0)
    en_position.pack(fill=X)
    lbb=Label(add,text=" حقوق",font=f,bg="lightblue",fg=btnbg)
    lbb.pack(fill=X)
    en_salary=Entry(add,width=12,font=f,border=0)
    en_salary.pack(fill=X)
    btnadd=Button(add,font=("B Titr",12),width=10,height=1,border=0,bg=btnbg,fg=btnfg,text="ثبت",command=add_ps_db)
    btnadd.pack(fill=X)

def add_ps_db():
    fname=en_fname.get()
    lname=en_lname.get()
    position=en_position.get()
    salary=en_salary.get()
    db()
    curs.execute('INSERT INTO personal (fname,lname,position,salary) VALUES (?, ?, ?, ?)',[fname,lname,position,salary])
    cnn.commit()
    cnn.close()
    add.destroy()
    messagebox.showinfo("شخص مورد نظر با موفقیت افزوده شد.","ثبت موفق")
    showpersonal()

def EditPersonal():
    global en_fnamen,en_lnamen,en_positionn,en_salaryn,edit
    edit=Toplevel(personal,bg="lightblue")
    edit.title("ویرایش پرسنل")
    edit.geometry("500x500")
    showpersonal()
    lbb=Label(edit,text="لطفا مشخصات زیر را به درستی وارد کنید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=100,y=10)
    lbb=Label(edit,text="نام ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=100)
    en_fnamen=Entry(edit,width=35,font=f,border=0)
    en_fnamen.place(x=20,y=100)
    en_fnamen.insert(0,item_data[1])
    lbb=Label(edit,text=" نام خانوادگی ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=200)
    en_lnamen=Entry(edit,width=35,font=f,border=0)
    en_lnamen.place(x=20,y=200)
    en_lnamen.insert(0,item_data[2])
    lbb=Label(edit,text="موقعیت",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=300)
    en_positionn=Entry(edit,width=35,font=f,border=0)
    en_positionn.place(x=20,y=300)
    en_positionn.insert(0,item_data[3])
    lbb=Label(edit,text=" حقوق",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=400)
    en_salaryn=Entry(edit,width=35,font=f,border=0)
    en_salaryn.place(x=20,y=400)
    en_salaryn.insert(0,item_data[4])
    btnadd=Button(edit,font=("B Titr",12),width=10,height=1,border=0,bg=btnbg,fg=btnfg,text="ویرایش",command=editpersonal)
    btnadd.place(x=140,y=440)

def editpersonal():
    newfname=en_fnamen.get()
    newlname=en_lnamen.get()
    newposition=en_positionn.get()
    newsalary=en_salaryn.get()

    db()
    curs.execute('UPDATE personal SET fname= ? , lname= ? , position = ? , salary = ? WHERE id = ? ', (newfname , newlname,newposition, newsalary ,selected_id))
    cnn.commit()
    cnn.close()
    edit.destroy()
    messagebox.showinfo("شخص مورد نظر با موفقیت افزوده شد.","ثبت موفق")
    showpersonal()    
    
def showpersonal():
    global lpers
    db()
    curs.execute('SELECT * FROM personal')
    rows=curs.fetchall()
    treep.delete(*treep.get_children())
    lpers=len(rows)
    treep.config(height=lpers)
    for row in rows:
        treep.insert("",END,values=row)

def DeletePersonal():
    db()
    curs.execute('DELETE FROM personal where id = ?', (selected_id,))
    cnn.commit()
    cnn.close()
    showpersonal()


def add_product():
    global en_product,en_bprice,en_sprice,en_qnt,add
    add=Toplevel(Product,bg="lightblue")
    add.title("محصول جدید")
    add.geometry("500x500")
    showproduct()
    lbb=Label(add,text="لطفا مشخصات زیر را به درستی وارد کنید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=100,y=10)
    lbb=Label(add,text="نام محصول ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=100)
    en_product=Entry(add,width=35,font=f,border=0)
    en_product.place(x=20,y=100)
    lbb=Label(add,text="قیمت خرید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=200)
    en_bprice=Entry(add,width=35,font=f,border=0)
    en_bprice.place(x=20,y=200)
    lbb=Label(add,text="قیمت فروش",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=300)
    en_sprice=Entry(add,width=35,font=f,border=0)
    en_sprice.place(x=20,y=300)
    lbb=Label(add,text="تعداد",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=400)
    en_qnt=Entry(add,width=35,font=f,border=0)
    en_qnt.place(x=20,y=400)
    btnadd=Button(add,font=("B Titr",12),width=10,height=1,border=0,bg=btnbg,fg=btnfg,text="ثبت",command=add_pr_db)
    btnadd.place(x=140,y=440)

def add_pr_db():
    product=en_product.get()
    bprice=en_bprice.get()
    sprice=en_sprice.get()
    qnt=en_qnt.get()
    db()
    curs.execute('INSERT INTO products (product,bprice,sprice,qnt) VALUES (?,?, ?, ?)',[product,bprice,sprice,qnt])
    cnn.commit()
    cnn.close()
    messagebox.showinfo("شخص مورد نظر با موفقیت افزوده شد.","ثبت موفق")
    en_product.config()
    en_bprice.config()
    en_sprice.config()
    en_qnt.config()
    add.destroy()
    showproduct()

def EditProduct():
    global en_productn,en_bpricen,en_spricen,en_qntn,edit
    edit=Toplevel(Product,bg="lightblue")
    edit.title("ویرایش محصول ")
    edit.geometry("500x500")
    showproduct()
    lbb=Label(edit,text="لطفا مشخصات زیر را به درستی وارد کنید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=100,y=10)
    lbb=Label(edit,text="نام محصول ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=100)
    en_productn=Entry(edit,width=35,font=f,border=0)
    en_productn.place(x=20,y=100)
    en_productn.insert(0,item_data[1])
    lbb=Label(edit,text="قیمت خرید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=200)
    en_bpricen=Entry(edit,width=35,font=f,border=0)
    en_bpricen.place(x=20,y=200)
    en_bpricen.insert(0,item_data[2])
    lbb=Label(edit,text="قیمت فروش",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=300)
    en_spricen=Entry(edit,width=35,font=f,border=0)
    en_spricen.place(x=20,y=300)
    en_spricen.insert(0,item_data[3])
    lbb=Label(edit,text="تعداد",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=400)
    en_qntn=Entry(edit,width=35,font=f,border=0)
    en_qntn.place(x=20,y=400)
    en_qntn.insert(0,item_data[4])
    btnadd=Button(edit,font=("B Titr",12),width=10,height=1,border=0,bg=btnbg,fg=btnfg,text="ویرایش",command=editproduct)
    btnadd.place(x=140,y=440)

def editproduct():
    en_productnn=en_productn.get()
    en_bpricenn=en_bpricen.get()
    en_spricenn=en_spricen.get()
    en_qntnn=en_qntn.get()
    db()
    curs.execute('UPDATE products SET product= ? , bprice= ? , sprice= ? , qnt = ? WHERE id = ? ', (en_productnn,en_bpricenn,en_spricenn,en_qntnn ,selected_id))
    cnn.commit()
    cnn.close()
    edit.destroy()
    messagebox.showinfo("شخص مورد نظر با موفقیت افزوده شد.","ثبت موفق")
    showproduct()    
    
def showproduct():
    db()
    curs.execute('SELECT * FROM products')
    rows=curs.fetchall()
    treepr.delete(*treepr.get_children())
    lpers=len(rows)
    treepr.config(height=lpers)
    for row in rows:
        treepr.insert("",END,values=row)

def DeleteProduct():
    db()
    curs.execute('DELETE FROM products where id = ?', (selected_id,))
    cnn.commit()
    cnn.close()
    showproduct()


def add_customer():
    global en_fnamec,en_lnamec,en_phonec,addc
    addc=Toplevel(Customers,bg="lightblue")
    addc.title("مشتری جدید")
    addc.geometry("500x500")
    showcustomer()
    lbb=Label(addc,text="لطفا مشخصات زیر را به درستی وارد کنید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=100,y=10)
    lbb=Label(addc,text="نام ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=100)
    en_fnamec=Entry(addc,width=35,font=f,border=0)
    en_fnamec.place(x=20,y=100)
    lbb=Label(addc,text=" نام خانوادگی ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=200)
    en_lnamec=Entry(addc,width=35,font=f,border=0)
    en_lnamec.place(x=20,y=200)
    lbb=Label(addc,text="تلفن",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=300)
    en_phonec=Entry(addc,width=35,font=f,border=0)
    en_phonec.place(x=20,y=300)
    btnadd=Button(addc,font=("B Titr",12),width=10,height=1,border=0,bg=btnbg,fg=btnfg,text="ثبت",command=add_cs_db)
    btnadd.place(x=140,y=440)

def add_cs_db():
    fnamec=en_fnamec.get()
    lnamec=en_lnamec.get()
    phonec=en_phonec.get()
    db()
    curs.execute('INSERT INTO customers (fname,lname,phone) VALUES (?, ?, ?)',[fnamec,lnamec,phonec])
    cnn.commit()
    cnn.close()
    en_fnamec.delete(0,END)
    en_lnamec.config()
    en_phonec.config()
    addc.destroy()
    showcustomer()
    messagebox.showinfo("شخص مورد نظر با موفقیت افزوده شد.","ثبت موفق")

def EditCustomer():
    global en_fnamecn,en_lnamecn,en_phonecn,edit
    edit=Toplevel(Customers,bg="lightblue")
    edit.title("مشتری جدید")
    edit.geometry("500x500")
    showcustomer()
    lbb=Label(edit,text="لطفا مشخصات زیر را به درستی وارد کنید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=100,y=10)
    lbb=Label(edit,text="نام ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=100)
    en_fnamecn=Entry(edit,width=35,font=f,border=0)
    en_fnamecn.place(x=20,y=100)
    en_fnamecn.insert(0,item_data[1])
    lbb=Label(edit,text=" نام خانوادگی ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=200)
    en_lnamecn=Entry(edit,width=35,font=f,border=0)
    en_lnamecn.place(x=20,y=200)
    en_lnamecn.insert(0,item_data[2])
    lbb=Label(edit,text="تلفن",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=300)
    en_phonecn=Entry(edit,width=35,font=f,border=0)
    en_phonecn.place(x=20,y=300)
    en_phonecn.insert(0,item_data[3])
    btnadd=Button(edit,font=("B Titr",12),width=10,height=1,border=0,bg=btnbg,fg=btnfg,text="ویرایش",command=editcustomer)
    btnadd.place(x=140,y=440)

def editcustomer():
    en_fnamecnn=en_fnamecn.get()
    en_lnamecnn=en_lnamecn.get()
    en_phonecnn=en_phonecn.get()
    db()
    curs.execute('UPDATE customers SET fname= ? , lname= ? , phone = ?  WHERE id = ? ', (en_fnamecnn,en_lnamecnn,en_phonecnn ,selected_id))
    cnn.commit()
    cnn.close()
    edit.destroy()
    showcustomer() 
    messagebox.showinfo("شخص مورد نظر با موفقیت افزوده شد.","ثبت موفق")
    showcustomer()    

def showcustomer():
    db()
    curs.execute('SELECT * FROM customers')
    rows=curs.fetchall()
    treec.delete(*treec.get_children())
    lpers=len(rows)
    treec.config(height=lpers)
    for row in rows:
        treec.insert("",END,values=row)

def DeleteCustomer():
    db()
    curs.execute('DELETE FROM customers where id = ?', (selected_id,))
    cnn.commit()
    cnn.close()
    showcustomer()


def add_financial():
    global en_type,en_amount,en_date,en_status,add
    add=Toplevel(Accounting,bg="lightblue")
    add.title("پرسنل جدید")
    add.geometry("500x500")
    showfinancial()
    lbb=Label(add,text="لطفا مشخصات زیر را به درستی وارد کنید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=100,y=10)
    lbb=Label(add,text="نوع",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=100)
    en_type=Entry(add,width=35,font=f,border=0)
    en_type.place(x=20,y=100)
    lbb=Label(add,text=" مقدار",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=200)
    en_amount=Entry(add,width=35,font=f,border=0)
    en_amount.place(x=20,y=200)
    lbb=Label(add,text="تاریخ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=300)
    en_date=Entry(add,width=35,font=f,border=0)
    en_date.place(x=20,y=300)
    lbb=Label(add,text="وضعیت",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=400)
    en_status=Entry(add,width=35,font=f,border=0)
    en_status.place(x=20,y=400)
    btnadd=Button(add,font=("B Titr",12),width=10,height=1,border=0,bg=btnbg,fg=btnfg,text="ثبت",command=add_fn_db)
    btnadd.place(x=140,y=440)

def add_fn_db():
    typee=en_type.get()
    amount=en_amount.get()
    date=en_date.get()
    status=en_status.get()
    db()
    curs.execute('INSERT INTO financial (type,Amount,date,status) VALUES (?, ?, ?, ?)',[typee,amount,date,status])
    cnn.commit()
    cnn.close()
    messagebox.showinfo("شخص مورد نظر با موفقیت افزوده شد.","ثبت موفق")
    en_type.config()
    en_amount.config()
    en_date.config()
    en_status.config()
    add.destroy()
    showfinancial()

def EditFinance():
    global en_typen,en_amountn,en_daten,en_statusn, edit
    edit=Toplevel(Accounting,bg="lightblue")
    edit.title("پرسنل جدید")
    edit.geometry("500x500")
    showfinancial()
    lbb=Label(edit,text="لطفا مشخصات زیر را به درستی وارد کنید",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=100,y=10)
    lbb=Label(edit,text="نوع",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=100)
    en_typen=Entry(edit,width=35,font=f,border=0)
    en_typen.place(x=20,y=100)
    en_typen.insert(0,item_data[1])
    lbb=Label(edit,text=" مقدار",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=200)
    en_amountn=Entry(edit,width=35,font=f,border=0)
    en_amountn.place(x=20,y=200)
    en_amountn.insert(0,item_data[2])
    lbb=Label(edit,text="تاریخ",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=300)
    en_daten=Entry(edit,width=35,font=f,border=0)
    en_daten.place(x=20,y=300)
    en_daten.insert(0,item_data[3])
    lbb=Label(edit,text="وضعیت",font=f,bg="lightblue",fg=btnfg)
    lbb.place(x=350,y=400)
    en_statusn=Entry(edit,width=35,font=f,border=0)
    en_statusn.place(x=20,y=400)
    en_statusn.insert(0,item_data[4])
    btnadd=Button(edit,font=("B Titr",12),width=10,height=1,border=0,bg=btnbg,fg=btnfg,text="ویرایش",command=editfinance)
    btnadd.place(x=140,y=440)

def editfinance():
    en_typenn=en_typen.get()
    en_amountnn=en_amountn.get()
    en_datenn=en_daten.get()
    en_statusnn=en_statusn.get()
    db()
    curs.execute('UPDATE financial SET type= ? , amount= ? , date = ? , status = ? WHERE id = ? ', (en_typenn,en_amountnn,en_datenn,en_statusnn ,selected_id))
    cnn.commit()
    cnn.close()
    edit.destroy()
    showfinancial() 
    messagebox.showinfo("شخص مورد نظر با موفقیت افزوده شد.","ثبت موفق")   

def showfinancial():
    global lpers
    db()
    curs.execute('SELECT * FROM financial')
    rows=curs.fetchall()
    treef.delete(*treef.get_children())
    lpers=len(rows)
    treef.config(height=lpers)
    for row in rows:
        treef.insert("",END,values=row)

def DeleteFinance():
    db()
    curs.execute('DELETE FROM financial where id = ?', (selected_id,))
    cnn.commit()
    cnn.close()
    showfinancial()


def Settingg():
    global bg 
    THB = Thb.get()
    bg = THB
    main.config(bg=bg)
    personal.config(bg=bg)
    Product.config(bg=bg)
    Customers.config(bg=bg)
    Accounting.config(bg=bg)
    Reporting.config(bg=bg)
    Setting.config(bg=bg)

def get_selected_data(event,tree):
    global selected_id , item_data
    db()
    selected_item = tree.selection()
    if selected_item:
        item_data=tree.item(selected_item[0])["values"]

    selected_id=int(item_data[0])

def Reporter():
    updateReportmember()
    reportcustomer()
    reportbalance()
    reportproduct()

def reportproduct():
    db()
    curs.execute('SELECT id FROM products')
    rows=curs.fetchall()
    l=len(rows)
    lbproductq.config(text=f"{l}")

def reportbalance():
    db()
    curs.execute('SELECT amount FROM financial')
    rows=curs.fetchall()
    total = 0
    for i in rows:
        total += i[0]
    lbbalanceq.config(text=f"{total}")

def reportcustomer():
    db()
    curs.execute('SELECT id FROM customers')
    rows=curs.fetchall()
    l=len(rows)
    lbcustomerq.config(text=f"{l}")

def updateReportmember():
    db()
    curs.execute('SELECT id FROM personal')
    rows=curs.fetchall()
    l=len(rows)
    lbmemberq.config(text=f"{l}")

def update_time(lb):
    current = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y/%m/%d")
    lb.config(text=f"!سلام به سیستم مدیریت کسب و کار خوش آمدید \n {current} - {current_date}")
    lb.after(1000, lambda: update_time(lb))

def close():
    win.destroy()

def db():
    global cnn,curs
    with open("mydb.db",mode="a"):
        cnn=sqlite3.connect("mydb.db")
        curs=cnn.cursor()


        curs.execute('''
        CREATE TABLE IF NOT EXISTS personal(
                    id INTEGER PRIMARY KEY,
                    fname TEXT NOT NULL,
                    lname TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary REAL NOT NULL
                    )
    ''')
        
        curs.execute('''
        CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY,
                    product TEXT NOT NULL,
                    bprice INTEGER NOT NULL,
                    sprice INTEGER NOT NULL,
                    qnt INTEGER NOT NULL
                    )
    ''')
        
        curs.execute('''
        CREATE TABLE IF NOT EXISTS customers(
                    id INTEGER PRIMARY KEY,
                    fname TEXT NOT NULL,
                    lname TEXT NOT NULL,
                    phone INTEGER NOT NULL
                    )
    ''')
        
        curs.execute('''
        CREATE TABLE IF NOT EXISTS financial(
                    id INTEGER PRIMARY KEY,
                    type TEXT NOT NULL,
                    Amount INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    status Text NOT NULL
                    )
    ''')
        
        cnn.commit()


Gui()

