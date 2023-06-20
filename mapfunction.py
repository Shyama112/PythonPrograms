newList=[10,20,30,40,50]
def lisa(n):
    return n*5
val= map(lisa,newList)
print (list(val))

myList=[2,4,6,8,10,12,18]
def myfun(n):
    if n>5:
        return True
    else:
        return False
    
vale=filter(myfun,myList)
print(list(vale))


##def try(n):
##    newEle=input("Enter the number: ")
##    if newEle>30:
##        newElem=input("Enter the number: ")
##    elif newElem>40:
##        return newElem
##valeri=try()
##print(valeri)

def do(n):
    if n>=30:
        return True
    else:
        return False
valerie=filter(do,newList)
print(list(valerie))

def ore(n):
    if n%4==0 or n%3==0:
        return True
    else:
        return False
valeriee=filter(ore,newList)
print(list(valeriee))

def donot(n):
    value=n+10
    value1=value%5
    return value1
valerieee=
        

        

