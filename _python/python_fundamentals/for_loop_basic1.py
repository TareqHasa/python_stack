for i in range(1,151,1) :
    print (i)


for i in range(5,1001,5):
    print(i)


for i in range(1,101,1):
    if i%5 and i%10 !=0 :
        print(i)
    elif i%5==0 :
            print("Coding")  
    elif i%10==0 :
            print ("Coding Dojo")      

x=0
for i in range (0,500001,1):
    if i%2!=0:
        x+=i
print(x)

for i in range (2018,0,-4):
    print(i)

lowNum=2
highNum=9
mult =3
for i in range (lowNum,highNum+1) :
    if i % mult ==0:
        print(i)
