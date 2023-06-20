####f=open("think.txt","w")
####f.write("Think before you speak")
####f.close()
##f=open("think.txt","a+")
##print(f.read())
##f.write("Think before you speak")
##f.write(" Thinking without action is moo point")
####f.close()
####o=open("think.txt","rt")
##
##print(f.read())
##f.close()
##
##word="Do or do not there is no try"
##
##red=open("think.txt","w")
##red.writelines(word)
##red.close()
##
##red=open("think.txt","r")
##print (red.readlines(   ))
##red.close()

##yoda=open("think.txt","a+")
##yoda.write(" a great teacher failure is")
##yoda.seek(0)
##print(yoda.read())
##print(yoda.tell())
##yoda.close()
##
##yoda=open("think.txt","a+")
##yoda.writelines(["do or do not there is no try","let go of everything you fear to lose"])
##yoda.seek(0)
##print(yoda.readline())
##yoda.close()

##try:
##        a= int(input("Enter the number: "))
##except ValueError as b:
##    print("Enter integer like 0,1,2,3,..n")
##    a= int(input("Enter the number: "))
##    c =a+10
##else:
##    c =a+10
##
##finally:
##        print("finally block is running")
##print(c)
    
        
##raise TypeError
##print("program completed")

val=int(input("Enter a odd number: "))
if val%2==0:
        try:
                raise TypeError("Enter a odd number")
        except:
                val=int(input("Enter a odd number: "))
                raise TypeError("Enter a odd number")
        finally:
                print("a number is executed")                
else:
        print(val ,"is a odd number")






        














