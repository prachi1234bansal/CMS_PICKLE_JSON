#BLL(BUSINESS LOGIC LAYER):
import pickle
import json
class Customer:
    cuslist=[]
    def addCustomer(self):
        Customer.cuslist.append(self)
    def searchCustomer(self):
        for e in Customer.cuslist:
            if self.id==e.id:
                return e
    def deleteCustomer(id):
        for e in Customer.cuslist:
            if id==e.id:
                Customer.cuslist.remove(e)

    def modifyCustomer(self):
        for e in Customer.cuslist:
            if e.id==self.id:
                e.name=self.name;
                e.id=self.id
                e.age=self.age
                e.mobile_no=self.mobile_no
    @staticmethod
    def sortCriteria(obj):
        return obj.id
    def sortById():
        return Customer.cuslist.sort(key=Customer.sortCriteria)
    def sortCriteria1(obj):
        return obj.name;
    def sortByName():
        return Customer.cuslist.sort(key=Customer.sortCriteria1)
    def savetoPickle():
        f=open("pickle2.pkl","wb")
        pickle.dump(Customer.cuslist,f)
        f.close()
    def loadfromPickle():
        f=open("pickle2.pkl","rb")
        Customer.cuslist=pickle.load(f)
        f.close()
    def convtoDic(obj):
        return obj.__dict__
    def savetoJson():
        f=open("e://customerjs.txt","w")
        json.dump(Customer.cuslist,f,default=Customer.convtoDic)
        f.close()
    def convtoObj(d):
        cus=Customer()
        for k,v in d.items():
            cus.__setattr__(k,v)
        return cus

    def loadfromJson():
        f=open("e://customerjs.txt","r")
        Customer.cuslist=json.load(f,object_hook=Customer.convtoObj)




#PL(PRESENTATION LAYER):
while True:
    def showCustomer(i):
        print(i.id,i.name,i.age,i.mobile_no)

    print("Welcome to Prachi Customer Management System")
    print("1 for add,2 for search,3 for delete,4 for modify,5 for display,6 for exit,7 for sort by id,8 for sort by name,9 for save data to pickle ,10 for load data from pickle")
    choice =int(input("Enter your choice according to above conditions ::"))
    if choice==1:
        obj=Customer();
        obj.name=input("Enter Customer Name:")
        obj.age=int(input("Enter Customer Age:"))
        obj.id=int(input("Enter Customer Id:"))
        obj.mobile_no=input("Enter Customer Mobile No:")
        if (obj.mobile_no.isdecimal()):
            if len(obj.mobile_no)==10:
                obj.addCustomer()
            else:
                print("Please enter valid mobile no!")
    elif choice==2:
        obj=Customer()
        obj.id=int(input("Enter Customer Id which u want to search::"))
        t=obj.searchCustomer()
        showCustomer(t)
    elif choice==3:
        id=int(input("Enter Customer Id which u want to delete:"))
        Customer.deleteCustomer(id)
    elif choice==4:
        cus=Customer()
        cus.id=int(input("Enter the id which u want to modify:"))
        cus.name = input("Enter the name which u want to modify:")
        cus.age = int(input("Enter the age which u want to modify:"))
        cus.mobile_no= input("Enter the mobile_no which u want to modify:")
        if cus.mobile_no.isdecimal():
            if len(cus.mobile_no)==10:
                cus.modifyCustomer()

    elif choice==5 :
        for i in Customer.cuslist:
            showCustomer(i)
    elif choice==7:
        Customer.sortById()
    elif choice==8:
        Customer.sortByName()
    elif choice==9:
        Customer.savetoPickle()
        print("Data saved in Pickle Format Successfully")
    elif choice==10:
        Customer.loadfromPickle()
        print("Data loaded Successfully from Pickle")
    elif choice==11:
        Customer.savetoJson()
        print("Data is successfully saved in json format")
    elif choice==12:
        Customer.loadfromJson()
        print("Data is loaded Successfully from json")
    elif choice==6:
        print("Thanku for using Prachi Customer Management System!!")
        break;
    else:
        print("INCORRECT CHOICE")