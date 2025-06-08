def factorial(user_no):
    fact_no = 1
    for i in range(1, user_no + 1):
        fact_no = fact_no * i
    return fact_no

user = int(input("Enter the Number: "))
print("Factorial of the input number: ", factorial(user))