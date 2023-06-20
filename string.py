##var="First word"
##print(len(var))
##for i in range(0,len(var)):
##    print(var[i], end="")
##print("")
##
##varWord="Second word"
##for i in varWord:
##    print(i)
##
##value=int(input("Enter the value:"))
##word="Word of the day"
##print(word[value])

##wordOne= "Mandalorian"
##for i in range(0,len(wordOne)):
##    if wordOne[i]=="z":
##        print(" the letter l is present in the word")
##        break
##else:
##    print(" the letter is not present in the word")
##wordTwo= "Order66"
##print(wordTwo[:5])

##str="Welcome to the blog"
##print(str[3:18])
##print(str[2::2])
##print(str[:7])
##print(str[8:-1:1])
##print(str[-9:-15])
##print(str[0:9:3])
##print(str[9:29:2])
##print(str[-6:-9:-3])
##print(str[-9:-9:-1])
##print(str[8:25:3])

#### PYTHON STRING METHODS ####

##captitalize

##sen= "may the force be with you"
##print(sen.capitalize())
##
####Upper
##
##sen2= "may the force be with you"
##print(sen2.upper())
##
####Lower
##
##sen3= "May THE foRce Be wItH yOU"
##print (sen3.lower())
##
####count
##
##sen4= "May the force be with you"
##print(sen4.count("y"))
##
####split
##
##sen5= "May the force be with you"
##print(sen5.split())
##
####partition
##
##sen6= "May the force be with you"
##print(sen6.partition("force"))

####find
##
##sen7= "may the force be with you"
##print(sen7.find("force"))
##
####swapcase
##
##sen8= "MAy the Force be wIth yoU"
##print(sen8.swapcase())
##
####center
##
##sen9= "May the force be with you"
##print(sen9.center(50))
##
####join
##
##sen10= "May the force be with you"
##print(sen10.join("123456"))

#### EXERCISE ####

##tempSen="The orange juice"
##if "orange" in tempSen:
##    print (" the word orange is present in the variable")
##else:
##    print(" the word orange is not present in the variable")

##word= "Hello world"
##first=0
##last=0
##for i in word:
##    if i=="o":
##        first=word.index(i)
##        break
##    
##for i in range(len(word)-1,-1,-1):
##    if(word[i]=="o"):
##        last=i
##        break
##print(first)
##print(last)
####REVERSE THE 
##value= "rebels"
##print(value[::-1])
##
##for i in value[::-1]:
##    reverseValue=i
##    print(reverseValue , end="")
##print("")
##                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
##reverseValue2=""
##name=input("Enter the word: ")
##for i in name[::-1]:
##    reverseValue2=reverseValue2+i 
##    
##print(reverseValue2)
####VOWELS AND CONSONANTS COUNT ####

##value=input("Enter the name: ")
##vowel=0
##consonant=0
##for i in value:
##    if i in ["a","e","i","o","u"]:
##        vowel=vowel+1
##    else:
##        consonant=consonant+1
##print("No of vowels in the word is",vowel)
##print("No of consonants in the word is",consonant)
##
######COUNT NUMBER OF LETTERS####
##
##value2=input("Enter the value: ")
##count=0
##for i in value2:
##    count=count+1
##print("No of letters in the word is",count)
##
###### TO REMOVE DUPLICATED LETTERS ####
##
##string="AshokaTano"
##empty=""
##for i in string:
##    if i in empty:
##        pass
##    else:
##        empty=empty+i
##print (empty)

#### COUNT THE OCCURANCE #### ????
##
##value4="Do or do not there is no try"
##print(value4.count("o"))
##test="o"
##occur=""
##count=0
##for i in value4:
##    if test in value4:
##        count=count+1
##print(count)

######Swapcase ####
##
##name= " Ezra Bridger"
##print(name.swapcase())


#### METHODS ####

####slice
##name1= "This is the way"
##print(name1[0:8:])
##
####pow
##
##num= pow(12,2)
##print (num)
##
####reversed
##
##list1=["skywalker","ashoka","kenobi","r2D2","yoda"]
##sort=sorted(list1)
##print(sort)
##
####isalpha
##
##name2="ObiwanKenobi"
##print(name2.isalpha())
##
####isalnum
##
##name3="Icebear42"
##print(name3.isalnum())
####OCCURENCE####
##theValue= "Order66Com@nderReX$"
##numeric=0
##alpha=0
##lower=0
##upper=0
##special=0
##for i in theValue:
##    boolean=i.isnumeric()
##    boolean2=i.isalpha()
##    boolean3=i.islower()
##    boolean4=i.isupper()
##    if boolean==True:
##        numeric=numeric+1
##    elif boolean3==True:
##       lower=lower+1
##    
##    elif boolean4==True:
##       upper=upper+1
##    else:
##        special=special+1
##    if( boolean2==True):
##        alpha=alpha+1
##print ("The number of numeric value is",numeric)
##print ("The number of alphabetic value is",alpha)
##print("The number of lowercase value is",lower)
##print("The number of uppercasevalue value is",upper)
##print("The number of specialcharacter value is",special)

myCharaters=["Yanfei","Raiden","Childe","Kaeyaa",[0,5,"str

    



    
        


        

    





