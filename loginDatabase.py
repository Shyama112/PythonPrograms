import pymongo
login_details=pymongo.MongoClient("mongodb://localhost:27017")
login_storage=login_details["ids"]
login_path=login_storage["details"]
id1={"gmailid":"finn@gmail.com","password":"12345"}
id2={"gmailid":"jake@gmail.com","password":"12345"}
id3={"gmailid":"bmo@gmail.com","password":"12345"}
id4={"gmailid":"bubblegum@gmail.com","password":"12345"}
id5={"gmailid":"marceline@gmail.com","password":"12345"}
id_data=[id1,id2,id3,id4,id5]
##login_path.insert_many(id_data)
print("Welcome to the data base")
action=input("signin or signup? ")

def signup():
    gmail=input("Enter the email address: ")
    password=input("Enter the password: ")
    signupWord={"gmailid":gmail,"password":password}
    login_path.insert_one(signupWord)
    for i in login_path.find():
        print (i)

def signin():
    idNo=input("Enter the id: ")
    passNo=input("Enter the password: ")
    
    for x in login_path.find():
       
        if x.get("gmailid")==idNo and x.get("password")==passNo:
            print("loged in successfully")
            return
    else:
        print("couldn't login, try signing up")
        signup()

if action=="signin":
    signin()
if action=="signup":
    signup()





