delimiters=[' ','+','-','*','/',',',';','>','<','=','{','}','[',']','(',')','\n']
keywords=['int','char','float','string','if','else',
          'elif','break','for','in','while','range','def','return','and','or','not']
operators=['+','-','=','/','*']
sub=''
current=0
lines=[]
                
def check(i,sub,current):
    if current==1 and sub!='':
            if sub in keywords:
                print(sub," : keyword")
            else:
                print(sub," : identifier")
            sub=''
            
            current=0
    elif current==2 and sub!='':
        print(sub," : number ")
        current=0
        sub=''
    if i in operators:
        if i=='+':
            print(i," : operator PLUS")
        elif i=='-':
            print(i," : operator MINUS")
        elif i=='*':
            print(i," : operator MULTIPLICATION")
        elif i=='/':
            print(i," : operator DIVISION")
        elif i=='=':
            print(i," : operator EQ")
        current=0
    return(sub,current)

print("Enter the input")
while True:
    try:
        
        line = input()
        if line:
            lines.append(line)
        else:
            break
    except EOFError:
        break
str= '\n'.join(lines)

for i in str:
    if i not in delimiters:
        if current==0:
            if i.isalpha():
                current=1
                sub=sub+i
                
            elif i.isdecimal():
                current=2
                sub=sub+i
                
        elif current==1:
            if i.isalnum():
                
                sub=sub+i
                
                current=1
        elif current==2:
            if i.isdecimal():
                sub=sub+i
                current=2
    else:
        sub,current=check(i,sub,current)
sub,current=check(i,sub,current)