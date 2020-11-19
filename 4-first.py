def First(key,value,length=0):
    f.update({key:[]})
    value=value.split('|')
    for i in value:
        terminal=False
        epsilon=True
        for j in i:
            if j is '~':
                f[key].append(j)
            elif j.islower() and terminal is False:
                f[key].append(j)
                terminal=True
            elif j.isupper():
                p=key
                temp=[]
                temp=(First(j,dict[j]))
                for k in temp:
                    if k not in f[p] and epsilon:
                        f[p].append(k)
                if '~' not in temp:
                    epsilon=False
                
    if len(f)==length:
        for x in f:
            print('FIRST (',x,') = { ',end='')
            for y in f[x]:
                print(y,end=' , ')
            print('\b\b }')
        
    return(f[key])




lines=[];ret_val={};dict={};f={}
print("Enter the input ~ for epsilon")
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

productions=(str.split('\n'))       
for i in productions:
    seperate=i.split('-->')
    dict[seperate[0]]=seperate[1]
ret_val=First('S',dict['S'],len(dict))