##newList=[]
##value=[]
##for i in range(10):
##    myList=int(input("Enter 10 values of the list: "))
##    newList.append(myList)
##findValue=int(input("Which value do you want to find? "))
##if findValue in newList:
##        print( "the value is present in the list")
##else:
##        print("the value is not present in the list") ###1
##    
##newList1=[]
##newList2=[]
##for i in range(10):
##    myList1=int(input("Enter 10 values of the list: "))
##    newList1.append(myList1)
##    newList2=newList1.copy()
##    newList2.reverse()
##print (newList2)###2

##numList=[20,30,40,50,60,70]
##sumOf=0
##for i in numList:
##    sumOf=sumOf+i
##print(sumOf)
##productOf=1
##for i in range(len(numList)):
##    productOf=productOf*numList[i]
##print(productOf)

##listed=[]
##listed1=[]
##listed2=[]
##totalNo=int(input("Enter the total no of values: "))
##totalNo1=int(input("Enter the total no of values: "))
##for i in range(totalNo):
##    values=int(input("Enter your values: "))
##    listed1.append(values)
##for i in range(totalNo1):
##    values1=int(input("Enter your values: "))
##    listed2.append(values1)
##listed.append(listed1)
##listed.append(listed2)
##print(listed)

parent=[]
result=[]

row=int(input("Enter the row number: "))
column=int(input("Enter the coloumn number: "))
result=[]
for i in range(row):
    layerNum=[]
    for j in range(column):
        numbers=int(input("Enter the inner layer number: "))
        layerNum.append(numbers)
    parent.append(layerNum)
for i in parent:
    for j in i:
        print("",j, end="")
    print("")
parent1=[]
for i in range(row):
    layerNum1=[]
    for j in range(column):
        numbers1=int(input("Enter the inner layer number: "))
        layerNum1.append(numbers)
    parent1.append(layerNum1)
for i in parent1:
    for j in i:
        print("",j, end="")
    print("")

##for r in row:
##    row[i][j]=row1[i][j]
##print (r)
##

for i in range(row):
    laynum=[]
    for j in range(column):
        laynum.append(parent[i][j]+parent1[i][j])
    result.append(laynum)
for i in result:
    for j in i:
        print("",j, end="")
    print("")





        
            




        
    

