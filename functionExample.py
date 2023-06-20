def display():
    a=10
    b=90
    print(a+b)
    print("hello python")

##display()
##display()
##display()

def factor(number):
##    number=int(input("Enter the number: "))
    answer=1
    for i in range(1,number+1):
        answer=answer*i
    print("program completed")
    return answer

value=int(input("Enter a number"))
####number=value
result=factor(value)+10
print("factor function return value=",result)


##def numbers(a,b):
##    print(a+b)
##    print(a-b)
##    print(a*b)
##    print(a%b)
##    print(a//b)
##    print(a/b)   
##numbers(5,6)

##def new(a,b):
##    answer=a+b
##    return answer
##new(3,4)
##variable=new(3,4)
##print(variable)

##def var(str,n):
##    result=str
##    for i in range(n):
##        print (result, end="")
##    print("")
##var("nvm",4)

##def var(str):
##    ans=""
##    for i in range(len(str)):
##        for j in range(i+1):
##            ans=ans+str[j]
##        print(ans)
##var("code")

##def monkey(a_smile,b_smile):
##    if a_smile and b_smile:
##        print (True)
##        if not a_smile and not b_smile:
##            print (True)
##    else:
##        print (False)
##
##monkey(True,False)


        
        
    


