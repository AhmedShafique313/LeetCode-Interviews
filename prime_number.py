def PrimeNumber(user_no):
    if user_no < 2:
        print(user_no, "is not a Prime Number")
        return
    
    for i in range(2, int(user_no ** 0.5) + 1):
        if user_no % i == 0:
            print(user_no, "is not a Prime Number")
            return
    print(user_no, "is a Prime Number")


user = int(input("Enter the number: "))
PrimeNumber(user)
