def GreaterThan10():
    total = 0
    for i in range(10):
        user_no = int(input(f"Enter number {i+1}: "))
        total += user_no
    print("The sum of numbers greater than 10 is:", total)

GreaterThan10()
