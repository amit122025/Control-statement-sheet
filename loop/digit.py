n=int(input("Enter  a number :"))
count =1
while(n>0):
    digit =n%10
    print(digit)
    n=n//10
    count +=1
    print("total digits:", count-1)