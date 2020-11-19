inputLine = []
num = input("Number of lines :- ")
temp = {}
newLines = []
for _ in range(int(num)):
    inputLine.append(input())
for line in inputLine:
    if '=' in line:
        mid = line.find('=')
        variable = None
        value = None
        if ' ' not in line[mid-1]:
            variable = line[mid-1]
        else:
            variable = line[mid-2]
        if ' ' not in line[mid+1]:
            try:
                int(line[mid+1])
                value = line[mid+1]
            except:
                pass
        else:
            if ' ' not in line[mid+2]:
                try:
                    int(line[mid+2])
                    value = line[mid+2]
                except:
                    pass
        if value is not None:
            temp[variable] = int(value)
            # print(variable, " ", value)

for line in inputLine:
    if 'int' not in line:
        flag=line
        for constant in temp:
            if constant in line:
                line=line.replace(constant,str(temp[constant]))
                # line[line.find(constant)] = temp[constant]
                # print(line)
                flag=line
        newLines.append(flag)
    else:
        newLines.append(line)
print("\nOutPut:-\n")
for line in newLines:
    print(line)