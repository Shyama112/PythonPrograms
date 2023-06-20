##name=["a","b","c"]
##def module():
##
##    name.append("f")
##    print(name)
####    name=["e","d","f"]
##    print("local name", name)
##    
##module()
##print("global name", name)
##num=2
##def invert():
##    global num
##    num=num*2
##    print (num)
##invert()
##print(num)
myList=['a','r','b','c','k','d','e','f']


def addElement():
    noOfEle=int(input("How many element do you want to add: "))
    for i in range (noOfEle):
        addElement=input("Enter the element you want to add: ")
        myList.append(addElement)
    print("Changes have been made")
    yesOr=input("Do you want to check the list? ")
    if yesOr =="yes" or yesOr=="Yes":
        print(myList)
    elif yesOr=="no" or yesOr== "No":
        print("Thank you for visiting")
def ModEle():
     modEle=input("Which element do you want to change? ")
     if modEle in myList:
         modEle1=input("Identify the element")
         x=myList.index(modEle)
         myList[x]=modEle1
         print("Changes have been made")
     else:
        print("The Element is not present in the list")

while True:
    options={1:"Add element",2:"Modify Element",3:"Delete Element",4:"Sort element",5:"Display Element",6:"Exit"}
    print (options)
    print()
    option=int(input("Enter the option you want to perform: "))
    
    if option == 1:
        addElement()
    elif option == 2:
        ModEle()
       
    elif option == 3:
        deleteEle=input("Which element do you want to delete? ")
        if deleteEle in myList:
            myList.remove(deleteEle)
        else:
            print("The Element is not present in the list")
    elif option == 4:
        sortEle=int(input("Do you want to sort in ascending or descending order? "))
        if sortEle==1:
            myList.sort()
            print (myList)
        elif sortEle==2:
            myList.sort(reverse=True)
            print(myList)
    elif option == 5:
        displayEle=int(input("Enter the index no of the element: "))
        print(myList[displayEle])
    elif option==6:
        print("You've exited from the page", )
        break
        
    
                   

        

        
            
        
