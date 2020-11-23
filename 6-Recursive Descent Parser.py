i = None
inputLine = None

def match(value):
    global i
    if i is value:
        try:
            i = next(inputLine)
        except StopIteration:
        # print("Input is empty and last charctor is :- ",i)
            pass
    else:
        print("Error on the Value :- ", i)
    

def S():
    if 'c' is i:
        match('c')
        A()
        match('d')
        print("--- Accepted ---")
    else:
        B()
        D()
        print("--- Accepted ---")


def A():
    global i
    if i is 'a':
        match('a')
        if i is 'b':
            match('b')
        elif not any(inputLine):
            pass
        else:
            print("error on A")
            raise Exception()
    else:
        print("error on A")
        raise Exception()
        


def B():
    global i
    if i is 'b':
        match('b')
        if i is 'm':
            match('m')
        elif not any(inputLine):
            pass
        else:
            print("error on B")
            raise Exception()
    else:
        print("error on B")
        raise Exception()


def D():
    global i
    if 'd' is i:
        match('d')
        if i is 'n':
            match('n')
        elif not any(inputLine):
            pass
        else:
            print("error on D")
            raise Exception()
    else:
        print("error on D")
        raise Exception()

if __name__ == "__main__":
    inputLine=iter(input("Enter a line :-"))
    print("Execting :- \n")
    i=next(inputLine)
    try:
        S()
    except Exception:
        pass
    print("Exection is stoped")
        
    