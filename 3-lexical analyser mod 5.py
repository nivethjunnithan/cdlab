ss=0
fs=0
pos=0
str=input("Enter the string ")
for i in str:
    
    
    if i=='0' or i=='1':
        if pos==0:
            if i=='0':pos=0
            else:pos=1
        elif pos==1:
            if i=='0':pos=2
            else:pos=3
        elif pos==2:
            if i=='0':pos=4
            else:pos=0
        elif pos==3:
            if i=='0':pos=1
            else:pos=2
        elif pos==4:
            if i=='0':pos=3
            else:pos=4
if pos==fs:
    print("string accepted")
else:
    print("string rejected")