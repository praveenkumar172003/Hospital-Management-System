from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.NameofTabelts=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.Storage=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #===========Dataframe============#
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1366,height=357)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                                     font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=876,height=313)
        DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                                     font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=886,y=5,width=410,height=313)

        #===========buttons frame============#

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=487,width=1366,height=70)
        #===========Details frame============#

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=557,width=1366,height=190)

        #===========DataframeLeft============#

        lblNameTablet=Label(DataframeLeft,text="Names of Tablet",font=("arial",12,"bold"),padx=1,pady=3)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataframeLeft,textvariable=self.NameofTabelts,state="readonly",font=("arial",12,"bold"),
                                                                     width=33)
        comNameTablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        ldlref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refrence No:",padx=1,pady=3)
        ldlref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=1,pady=3)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=1,pady=3)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Numberoftablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=1,pady=3)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=1,pady=3)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=1,pady=3)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Expdate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=1,pady=3)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)


        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=1,pady=3)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Info:",padx=1,pady=3)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFutherInfo=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFutherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=1,pady=3)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=1,pady=3)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=1,pady=3)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient ID:",padx=1,pady=3)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=1,pady=3)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=1,pady=3)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateofBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=1,pady=3)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DateofBirth,width=35)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="PatientAddress:",padx=1,pady=3)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)



        #===========Dataframeright============#

        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=38,height=14,padx=1,pady=3)
        self.txtPrescription.grid(row=0,column=0)

        #===========Buttons============#
        btnPrescription = Button(Buttonframe, text="Prescription",bg="green",fg="white",font=("arial", 13, "bold"), width=20, bd=4)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="PrescriptionData",bg="green",fg="white",font=("arial", 13, "bold"), width=20, bd=4)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", font=("arial", 13, "bold"),bg="green",fg="white", width=20, bd=4)
        btnUpdate .grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", font=("arial", 13, "bold"),bg="green",fg="white", width=20, bd=4)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", font=("arial", 13, "bold"),bg="green",fg="white", width=20, bd=4)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", font=("arial", 13, "bold"),bg="green",fg="white", width=20, bd=4)
        btnExit.grid(row=0, column=5)


        #===========Table============#
        #===========Scrollbar============#
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate",
                                    "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="Number of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dosage")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

       

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

        #===========Functionalitydeclaration============#
        def iPrescription(self):
            if self.Nameoftablets.get()==""or self.ref.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                con=mysql.connector.connect(host = "localhost", user="root", password = "Praveen@123", database = "Mydata",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
                my_cursor.execute("Insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(
                                                                                                   self.Nameoftabelts.get(),
                                                                                                   self.ref.get(),
                                                                                                   self.Dose.get(),
                                                                                                   self.Numberoftablets.get(),
                                                                                                   self.Lot.get(),
                                                                                                   self.Issuedate.get(),
                                                                                                   self.ExpDate.get(),
                                                                                                   self.DailyDose.get(),
                                                                                                   self.Storageadvice.get(),
                                                                                                   self.nhsNumber.get(),
                                                                                                   self.PatientName.get(),
                                                                                                   self.DateofBirth.get(),
                                                                                                   self.PatientAddress.get(),
                                                                                                    ))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=mysql.connector.connect(host = "localhost", user="root", password = "Praveen@123", database = "Mydata",auth_plugin='mysql_native_password')
        my_cursor=con.cursor()
        my_cursor.execute("select * from new_table")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
                con.commit()
            con.close()












    
        

        


                                               
                                                                       




root=Tk()
ob=hospital(root)
root.mainloop()  