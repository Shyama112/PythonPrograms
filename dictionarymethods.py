my_Dict= {3:"apple","character":"Raiden_shogun",4:"16",6:"fav"}

#KEY WORD
print(my_Dict[4])

#GET
print(my_Dict.get("character"))

#GETTING KEYS
print(my_Dict.keys())

#GETTING VALUES
print(my_Dict.values())

#GETTING ITEMS
print(my_Dict.items())

#UPDATING ELEMENTS// ADDING NEW ONE
my_Dict.update({7:"Dhoni"})
print(my_Dict)

#POP ITEMS
my_Dict.popitem()
print(my_Dict)

#DELETE
del my_Dict[4]
print(my_Dict)

#WORD COUNT
word="Grogu"
newDict={}
for i in word:
    x=word.count(i)
    newDict.update({i:x})
print(newDict)

#NUMBER AND IT'S SQUARE
value=int(input("Enter the n number"))
dictionary={}
for i in range(1,+value+1):
    dictionary.update({i:i*i})
print (dictionary)

#IF THE KEY IS PRESENT OR NOT
myDict={1:20,2:40,3:30,4:50}
if 3 in myDict:
    print("it is present in the dictionary")
    

    





