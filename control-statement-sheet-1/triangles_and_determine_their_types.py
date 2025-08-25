a=int(input("Enter the fist degree  :"))
b =int(input("Enter the second degree :"))
c =int(input("Enter the third  degree :"))
if(a+b+c==90):
    print("the tringle is right angle")
elif(a+b+c>90):
    print("the tringle is obtuse angle")
else:
    print("the tringle is acute angle")
