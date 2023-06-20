##myList=[45,34,"Sham",46.5,[2,3,4],89]
##print (myList)
##
######2
##
##for i in range(len(myList)):
##    print(myList[i], end="")
##print("")
##
########3
##count=0
##for i in range(len(myList)):
##    count=count+1
##print(count)
##
########4
##
##print(myList[::-1])
##
##########5 
##
##newList= [12,11,13,15]
##square=[]
##for i in range(len(newList)):
##    ans=newList[i]*newList[i]
##    square.append(ans)
##print(square)
##
########6
##
##newList.remove(13)
##print (newList)
##
########7
##
##newList.append(20)
##print(newList)
##
##newList.insert(2,30)
##print(newList)
##
########8
##
##for i in range(len(newList)):
##    if newList[i]%5==0:
##        print(newList[i], end="")

######9
##for i in range(len(newList)):

##firList=["kite","frog","fly"]#EXTEND
##firList.extend("value")
##print(firList)
##
##
##secList=firList.copy()#COPY
##print(secList)
##
##firList.pop(1)#POP
##print(firList)
##
##firList.remove("a")#REMOVE
##print(firList)
##
##firList.append("frog")#APPEND
##print(firList)
##
##x=firList.count("l")#COUNT
##print(x)
##
##print(len(firList))#LEN
##
##x=0
####numList=[]
##lenList=int(input("Enter the length of your list: "))
##for i in range(lenList):
##    valueList=int(input("Enter your values: "))
####    numList.append(valueList)
##for i in range(lenList):
##    if 

options={1:"Add element",2:"Modify Element",3:"Delete Element",4:"Sort element",5:"Display Element",6:"Exit"}
print (options)
option=int(input("Enter the option you want to perform: "))
myList=['a','r','b','c','k','d','e','f']
if option == 1:
    noOfEle=int(input("How many element do you want to add: "))
    for i in range (noOfEle):
        addElement=input("Enter the element you want to add: ")
        myList.append(addElement)
if option == 2:
    modEle=input("Which element do you want to change? ")
    if modEle in myList:
        modEle1=input("Identify the element")
        x=myList.index(modEle)
        myList[x]=modEle1
        print("Changes have been made")
    else:
        print("The Element is not present in the list")
if option == 3:
    deleteEle=input("Which element do you want to delete? ")
    if deleteEle in myList:
        myList.remove(deleteEle)
    else:
        print("The Element is not present in the list")
if option == 4:
    sortEle=int(input("Do you want to sort in ascending or descending order? "))
    if sortEle==1:
        myList.sort()
        print (myList)
    if sortEle==2:
        myList.sort(reverse=True)
        print(myList)
if option == 5:
    displayEle=int(input("Enter the index no of the element: "))
    print(myList[displayEle])
if option==6:
    print("You've exited from the page")

    

                  




    
    
