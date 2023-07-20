import pymongo

student_Info=pymongo.MongoClient("mongodb+srv://shyamasivam:Shyama#24@cluster0.xuxp8bt.mongodb.net/?retryWrites=true&w=majority")
info_Student=student_Info["studentData"]
info_Of_Student=info_Student["collectionData"]
##stuOne={"Name":"Ayaka","RollNo":1,"Address":"Kamaraj Street"}
##stuTwo={"Name":"Balladeer","RollNo":2,"Address":"Ambedkar Street"}
##stuThree={"Name":"Collei","RollNo":3,"Address":"Periyar Street"}
##stuFour={"Name":"Diona","RollNo":4,"Address":"Barathiyar Street"}
##stuFive={"Name":"Enchantress","RollNo":5,"Address":"Theresa Street"}
##Class8=[stuOne,stuTwo,stuThree,stuFour,stuFive]
##info_Of_Student.insert_many(Class8)

print("Welcome to the database! 1)Display 2) Update 3) Add 4)Delete")

answer=int(input("Enter the number: "))
def display():
    value=info_Of_Student.find({},{"_id":0,"Name":1,"RollNo":1,"Address":1})
    for eachData in value:
        key=eachData.keys()
        for eachKey in key:
            print(eachKey,":",eachData.get(eachKey),end="")
        print("")
    
def update():
    stuNo=input("Enter the name of the student: ")

    keyChange=input("Enter the key you want to update: ")
    valChange=input("Enter the value you want to change: ")
    info_Of_Student.update_one({"Name": stuNo},{"$set":{keyChange:valChange}})
    for x in info_Of_Student.find():
        print(x)
def add():
    name=input("Enter the name of the student: ")
    rollNo=input("Enter the roll no of the student: ")
    address=input("Enter the address of the student: ")
    newDict={"Name":name,"RollNo":rollNo,"Address":address}

    info_Of_Student.insert_one(newDict)
    for x in info_Of_Student.find():
        print(x)

def delete():
    removeStu=input("Enter the name of the student: ")
    info_Of_Student.delete_one({"Name":removeStu})
                                                       
if answer==1:
    display()
elif answer==2:
    update()
elif answer==3:
    add()
elif answer==4:
    delete()
    
    
