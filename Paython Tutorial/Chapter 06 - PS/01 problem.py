a = int(input("Enter number :"))
b = int(input("Enter number :"))
c = int(input("Enter number :"))
d = int(input("Enter number :"))

if(a>b and a>c and a>d):
    print("Greatest number is:" ,a)

elif (b>a and b>c and b>d):
    print("Greatest number is:" ,b)

elif (c>a and c>b and c>d):
    print("Greatest number is:" ,c)

elif (d>a and d>b and d>c):
    print("Greatest number is:" ,d)