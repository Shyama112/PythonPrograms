##mySet={"yanfei","raiden",3,"qiqi",88,"Childe"}
##
###ACCESS SET VALUES
##for i in mySet:
##    print(i)
##
###ADD
##mySet.add("Traveller")
##print(mySet)
##
###UPDATE
##newList=["Eula","Razor"]
##mySet.update(newList)
##print(mySet)
##
###REMOVE/DISCARD
##mySet.discard("Eula")
##print(mySet)
##
### REMOVE REPEATED ELEMENT
##repeatedList=[3,8,"fox","fish","cat","fox",3,"pineapple","cat"]
##newSet=set(repeatedList)
##print(newSet)
##
###CREATING COMMON NUMBERS AS SET
##
##listOne=[1,22,3,44,22,5,67,78,3,1,78,24]
##listTwo=[46,68,96,85,22,54,13,12,91,6,44]
##listThree=[89,95,22,45,27,48,33,73,92,44]
##emptySet=set()
##for i in listOne:
##    if i in listTwo and i in listTwo:
##        emptySet.add(i)
##for j in listTwo:
##    if j in listThree:
##        emptySet.add(j)
##print(emptySet)
##
###COPY
##
##a={"black","white","yellow"}
##b=a.copy()
##a.add("red")
##print(a)
##print(b)

#DIFFERENCE

colour={"Red","Yellow","Blue"}
colour1={"Black","Purple","White","Yellow"}

colourD=colour.difference(colour1)
print(colourD)

#INTERSECTION

colourI=colour.intersection(colour1)
print(colourI)

#ISDisJOINT

print(colour.isdisjoint(colour1))

#UPDATE
    
