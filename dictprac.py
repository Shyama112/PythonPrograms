##myDict={1:20,2:40,3:30,4:50}
##if 3 in myDict:
##    print("it is present in the dictionary")
##
##myDict1= {1:20,2:20,3:30,4:40,5:50} 

##value=int(input("Enter the n number"))
##dictionary={}
##for i in range(1,+value+1):
##    dictionary.update({i:i*i})
##print (dictionary)
##    

newDict={"Kashmir@gmail.com":"123456","Karnataka@gmail.com":"12345","Tamilnadu@gmail.com":"34567"}
firstOne= input("Are you here to Sign in or Sign up?")
if firstOne=="Signup" or firstOne=="signup":
    print("Welcome to the website")
    firstId=input("Enter your emailID: ")
    firstPass=input("Enter your password: ")
    reFirstPass=input("Re-enter your password: ")
    if firstPass==reFirstPass:
        newDict.update({firstId:reFirstPass})
        print("You've successfully signed up")
    else:
        print("Re-check your password")
else:
    print("Welcome back to the website")
    value=input("Enter your emailID: ")
    while value in newDict:
        password=input("Enter the password: ")
        if password==newDict[value]:
            print("You have successfully signed in")
            break
        else:
            print("Password is wrong")
            forgotPass=input("Forgot password? Do you wanna add new one?")
            break
        if forgotPass=="Yes" or "yes":
                newPass=input("Enter the new password: ")
                renewPass=input("Enter the new password: ")
                if newPass==renewPass:
                    print("Your password is successfully changed")

    
        
        
        
    




