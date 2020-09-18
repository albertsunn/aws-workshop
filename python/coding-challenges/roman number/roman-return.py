while True:
    
    number = input("Enter an integer number :    ")
    
    if number.isdigit()==False:
        print("Don't enter string. Please try again!   ")
        continue
    elif not 0<int(number)<4000:
        print("Your number is not between 1 and 3999. Please enter again!   ")
        continue
    else:
        L100 = {"0":"","1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"CM"}
        L10 = {"0":"","1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}
        L1 = {"0":"","1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}
        
        def conv(num):
            if len(num)==4:
                roman = int(num[0])*"M" + L100[num[1]] + L10[num[2]] + L1[num[3]]
                 
            elif len(number)==3:
                roman = L100[num[0]] + L10[num[1]] + L1[num[2]]
                
            elif len(number)==2:
                roman = L10[num[0]] + L1[num[1]]
                
            else :
                roman = L1[num[0]]
            return roman
        print(conv(number))
        
    answer=input("If you want to exit, please type exit?   ")
    if answer != "exit":
        continue
    else:
        break