while True:
    
    number = input("Enter an integer number :    ")
    
    if number.isdigit()==False:
        print("Not valid input!!! Please try again!   ")
        continue
    elif int(number)<1:
        print("Not valid input!!! Please enter again!  ")
        continue
    else:
        def convert(num):
            word = ""
            a = num // 3600000
            if a != 0:
                word = str(a) + " hour/s  "
            num %= 3600000
            b = num // 60000
            if b!=0:
                word += str(b) + " minute/s  "
            num %= 60000
            c = num // 1000
            if c != 0:
                word += str(c) + " second/s"
            if word == "":
                word = "just " + str(num) + " milisecond/s"
                return word
            else:
                return word
            
    print(convert(int(number)))

    answer=input("If you want to exit, please type exit?   ")
    if answer != "exit":
        continue
    else:
        break