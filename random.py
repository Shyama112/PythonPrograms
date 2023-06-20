import random

##print(random.randrange(8,20))
##
##random.seed(8)
##print (random.random())
##
##print(random.getstate())

while True:
    ran=random.randint(1,5)
    ans=int(input("Enter the answer: "))
    if ran==ans:
        print ("You won")
        break
    
        



