#### DIVISIBLE BY 7 OR NOT ####

##a=int(input("enter the number: "))
##b =a%7
##if b==0:
##    print ( "the number is divisible by 7")
##else:
##    print("the number is not divisible by 7")

#### WHICH NUMBER IS LARGER ####

##x= int(input("Enter the number: "))
##y= int(input("Enter the number2: "))
##if x>y:
##    print (x , "is larger than" , y)
##else:
##    print (y , "is larger than" , x)

#### LEAP YEAR OR NOT ####

##yourYear = int(input("Enter your year: "))
##b=yourYear%100
##if b==0:
## if yourYear%400==0:
##   print (" Your year is a Leap year")
## else:
##     print (" Your year is century year")  
##else:
##    if yourYear%4==0:
##        print (" Your year is a leap year")
##    else:
##        print (" Your year is not a leap year")

#### CALCULATOR ####

##No1= int(input("Enter the number: "))
##No2= int(input("Enter the number2: "))
##Operator=(input("Enter the operator: "))
##if Operator=="+":
##    print(No1+No2)
##elif Operator =="-":
##    print(No1-No2)
##elif Operator== "*":
##    print(No1*No2)
##elif Operator=="/":
##    print (No1/No2)

#### PLACES and MONUMENTS ####

##Place=input("Enter the place:")
##if Place=="Agra":
##    print("Taj Mahal")
##elif Place=="Delhi":
##    print("Red fort")
##elif Place=="Jaipur":
##    print("Jal Mahal")

#### POSITIVE OR NEGATIVE NUMBER ####

##No=int(input("Enter the number: "))
##if No>=0:
##    print(No, "is a positive number")
##else:
##    print(No, "is a negative number")

#### WHETHER IT'S DIVISIBLLE BY 2&3 ####

##x=int(input("Enter the number: "))
##if x%2==0 and x%3==0:
##      print (x, "is divisible by 2 & 3")
##else:
##    print (x, "is not divisible by 2 & 3")

#### BIKE PRICE AND IT'S ROAD TAX % ####

##bikePrice=int(input("Enter the price: "))
##if bikePrice>100000:
##    print (15/100*bikePrice, " is the road tax for you")
##elif bikePrice >50000 and bikePrice<=100000:
##    print (10/100*bikePrice, " is the road tax for you")
##elif bikePrice<=50000:
##    print (5/100*bikePrice, "is the road tax for you")

#### PIZZA ORDER ####

##pizSize=input("Size of the pizza: ")
##Topping=input("Do you want toppings? ")
##extraCheese=input("Do you want extra cheese? ")
##if pizSize=="small" and Topping=="yes" and extraCheese=="yes":
##    print (120+(5/100*120)+20 , "is the cost of your pizza")
##elif pizSize=="medium" and Topping=="yes" and extraCheese=="yes":
##    print (130+(5/100*130)+30 , "is the cost of your pizza")
##elif pizSize=="large" and Topping=="yes" and extraCheese=="yes":
##    print (150+(5/100*150)+50 , "is the cost of your pizza")
##elif pizSize=="small" and Topping=="no" and extraCheese=="yes":
##    print (120+20 , "is the cost of your pizza")
##elif pizSize=="small" and Topping=="no" and extraCheese=="no":
##    print (120 , "is the cost of your pizza")
##elif pizSize=="small" and Topping=="yes" and extraCheese=="no":
##    print (120+(5/100*120) , "is the cost of your pizza")
##elif pizSize=="medium" and Topping=="no" and extraCheese=="yes":
##    print (130+30 , "is the cost of your pizza")
##elif pizSize=="medium" and Topping=="yes" and extraCheese=="no":
##    print (130+(5/100*130) , "is the cost of your pizza")
##elif pizSize=="medium" and Topping=="no" and extraCheese=="no":
##    print (130 , "is the cost of your pizza")
##elif pizSize=="large" and Topping=="yes" and extraCheese=="no":
##    print (150+(5/100*150) , "is the cost of your pizza")
##elif pizSize=="large" and Topping=="no" and extraCheese=="yes":
##    print (150+50 , "is the cost of your pizza")
##elif pizSize=="large" and Topping=="no" and extraCheese=="no":
##    print (150 , "is the cost of your pizza")
