##newList=[]
##totalNo=int(input("enter the total value:" ))
##for i in range(totalNo):
##    value=input("Enter the value:" )
##    newList.append(value)
##maxValue=newList[0]
##for i in newList:
##    if i>maxValue:
##        maxValue=i
##print(maxValue)
##
##myList=[]
##totalTimes=int(input("How many values? "))
##positive=[]
##negative=[]
##odd=[]
##even=[]
##for i in range(totalTimes):
##    values=int(input("Enter your values: "))
##    myList.append(values)
##for i in myList:
##    if i>0:
##        positive.append([i])
##    if i<0:
##        negative.append([i])
##    if i%2!=0:
##        odd.append([i])
##    if i%2==0:
##        even.append([i])
##print(positive)
##print(negative)
##print(odd)
##print(even)
##codesdope


myList=[12,34,53,24,76,22,8]
for i in range (len(myList)):
    for j in range(i+1,len(myList)):
        if myList[i]<myList[j]:
            myList[i],myList[j]=myList[j],myList[i]
print (myList[1])

##myList=[12,34,53,24,76,22,8]
##for i in range (len(myList)):
##    for j in range(i+1,len(myList)):
##        if myList[i]>myList[j]:
##            myList[i],myList[j]=myList[j],myList[i]
##print (myList)
            
        



    
