while True:
    
    number = input("Enter an integer number :    ")
    
    if number.isdigit()==False:
        print("Don't enter string. Please try again!   ")
        continue
    elif not 0<int(number)<4000:
        print("Your number is not between 1 and 3999. Please enter again!   ")
        continue
    else:
        L100 = {"1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"CM"}
        L10 = {"1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}
        L1 = {"1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}

        if len(number)==4:
            print(int(number[0])*"M", end="")
            print(L100[number[1]], end="")
            print(L10[number[2]], end="")
            print(L1[number[3]], end="\n")
        elif len(number)==3:
            print(L100[number[0]], end="")
            print(L10[number[1]], end="")
            print(L1[number[2]], end="\n")
        elif len(number)==2:
            print(L10[number[0]], end="")
            print(L1[number[1]], end="\n")
        else :
            print(L1[number[0]], end="\n")
        
    answer=input("If you want to exit, please type exit?   ")
    if answer != "exit":
        continue
    else:
        break