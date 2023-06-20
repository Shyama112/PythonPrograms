#### PRINT A WORD FOR SIX TIMES ####
##for i in range(6):
##   print ("hi" , i)

##for i in range(10,20,5):
##    print ("diff", i)

#### MARK AND IT'S AVERAGE ####
##Total=0
##tab=int(input("Enter the number:"))
##for x in range(Sub):
##    Mark=int(input("Enter the mark: "))
##    Total=Mark+Total
##print ("Average of your mark is ,",Total//Sub)

##   
##while(condition):
##    statement
##No=0
##
##while (No<10):
##    No+=1
##    print (No,"*",tab, "=", No*tab)
##factorial number using while loop
##No=int(input("Enter the number:"))
##Num=1
##fac=1
##while (Num<No+1):
##    
##    fac=fac*Num
##    Num+=1
##print("factorial of" , No, "is" , fac)

## prime number finding in for loop
##number=int(input("Enter the number: "))
##count=0
##for i in range(2,number-1):
##    temp=number%i
##    if(temp==0):
##        count+=1
##
##if(count==0):
##    print ("the number", number," is a prime number")
##else:
##    print ("the number",number, "is not a prime number")
##swapping
##fibonacci
##Times=int(input("Enter the number of times :"))
##a=0
##b=1
##for x in range(0,Times):
##   print(a) 
##   c=a+b
##   b=a
##   a=c
##Num=int(input("Enter the number: "))
##var=0
##for i in range(2,Num):
##   if(Num%i==0):
##      var=+1
##      break
##if(var!=0):
##   print("the no is not prime no")
##else:
##   print ("the no is a prime no")

##for i in range(0,10):
##   if (i==7):
##      continue
##   print(i)
##
##for i in range(0,15):
##   if (i==16):
##      print(8)
##      pass
####NUMBER DIVISIBLE BY 11 but not 2 BETWEEN 100-500####
##x=0
##for i in range (100,500):
##   x+=1
##   if x%11==0 :
##      if x%2!=0:
##         print (x)
#### KEEP ACCEPTING NUMBER UNTIL USER ENTERS 0 ####
##Total=0
##x=1
##while (x!=0):
##   num=int(input("Enter the number: "))
##   Total=Total+num
##   print(Total)
##   if num==0:
##      break
####ADDING THE NUMBER OF DIGITS####?????
##Digit=0
##Digit2=0
##Num=int(input("Enter the number: "))

##while (Num!=0):
##   Digit=Num%10
##   Digit2=Digit+Digit2
##   Num=Num//10
##print (Digit2)

#### FIRST 10 INTEGER'S AND THEIR SQUARE ####

##for i in range (0,11):
##   print ("(", i ,",", i*i ,")")

####PATTERN ####

##for i in range (4):
##   for j in range (4):
##      if i<=j:
##         print ("*", end="")
##   print("")
####

##for i in range (7):
##   for j in range (7):
##      if i<=j:
##         print (" ",end="")
##      elif i>=j:
##         print ("*" , end="")
##   print ("")     

####

##for i in range (7):
##   for j in range (7):
##      if i>=j:
##         print ("", end="")
##      else:
##         print ((i,j))

####
##rows= int (input("Enter the row number: "))
##columns= int (input("Enter the column number: "))
##for rows in range (7):
##   for columns in range (7):
##      if rows<=columns:
##         print (" ",end="")
##      elif rows>=columns:
##         print ("*" , end="")
##   print ("")    

####

for i in range(5,0,-1):
   for j in range(5,0,-1):
      if i>=j:
##         print ("", end="")
##      if i<=j:
         print (j, end="")
   print ("")

for i in range(1,6):#2
   for j in range(1,6):
      if i>=j:
         print ("", end="")
      if i<=j:
         print (j, end="")
   print ("")

for i in range(1,6): #5
   for j in range(1,6):
      if i<=j:
         print ("", end="")
      if i>=j:
         print (j, end="")
   print ("")

for i in range(1,6):#10
   for j in range(1,6):
      if i<=j:
         print ("", end="")
      if i>=j:
         print (i, end="")
   print ("")

for i in range(5,0,-1):#9
   for j in range(5,0,-1):
      if i>=j:
         print ("", end="")
      if i<=j:
         print (j, end="")
   print ("")

for i in range(5,0,-1):#3
   for j in range(5,0,-1):
      if i<=j:
         print ("", end="")
      if i>=j:
         print (j, end="")
   print ("")

for i in range(5,0,-1):#11
   for j in range(5,0,-1):
      if i>=j:
         print ("", end="")
      if i<=j:
         print (i, end="")
   print ("")

for i in range(5,0,-1):#12
   for j in range(5,0,-1):
      if i<=j:
         print ("", end="")
      if i>=j:
         print (i, end="")
   print ("")


      



        
   




































