n  =int(input("Enter the number:"))
if(n<25):
    print("D grade")
elif(n==25 and n>45):
    print("C grade")
elif(n==45 and n>65):
    print("B grade")
elif(n==65 and n<85):
    print("A grade")
else:
    print("A+ grade")