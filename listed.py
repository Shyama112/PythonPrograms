parent=[]
row=int(input("Enter the row number: "))
coloumn=int(input("Enter the coloumn number: "))

for i in range(row):
    layerNum=[]
    for j in range(coloumn):
        numbers=int(input("Enter the numbers inside: "))
        layerNum.append(numbers)
    parent.append(layerNum)
for i in parent:
    for j in i:
        print("",j, end="")
    print("")



