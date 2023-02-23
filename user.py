import csv
class home:
  def __init__(self):
        pass
  def login(self,name,password):
     success = False
     file = open("user_detail.csv","r")
     for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             success = True
             break
     file.close()
     if(success):
        print("\n##### Login Successful #####")
        
     else:
        print("\n##### Wrong User Name Or Password #####")
        c.begin()
        
  def register(self,name,password):
    file = open("user_detail.csv","a")
    file.write("\n"+name+","+password)
   
  def log(self):
    
    print("##### LOGIN #####")
    name = input("\nEnter your name: ")
    password = input("Enter your password: ")
    c.login(name,password)

  def reg(self):
      print("###### REGISTRATION #####")
      name = input("Enter your name: ")
      password = input("Enter your password: ")
      c.register(name,password)

  def begin(self): 
    print("##### ADMIN #####")
    print("1.LOGIN\n2.REGISTRATION")
    option = input("")
    if(option=="1"):
      c.log()
    elif(option=="2"):
      c.reg()
    else:
      c.begin()
c=home()